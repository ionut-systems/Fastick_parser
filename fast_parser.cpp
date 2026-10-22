#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <iomanip>
#include <charconv>

int main(int argc, char* argv[]) {
    std::string fichier = (argc >= 2) ? argv[1] : "simulation_ticks.csv";

    auto debut = std::chrono::high_resolution_clock::now();

    std::ifstream file(fichier, std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        std::cerr << "Erreur : Impossible d'ouvrir le fichier " << fichier << std::endl;
        return 1;
    }

    std::streamsize taille = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> buffer(taille);
    file.read(buffer.data(), taille);
    file.close();

    long long nb_ticks = 0;
    double somme_prix = 0.0;
    double volume_total = 0.0;

    const char* ptr = buffer.data();
    const char* end = ptr + taille;

    while (ptr < end && *ptr != '\n') ++ptr;
    if (ptr < end && *ptr == '\n') ++ptr;

    while (ptr < end) {
        if (*ptr == '\r' || *ptr == '\n') {
            ++ptr;
            continue;
        }

        while (ptr < end && *ptr != ',') ++ptr;
        if (ptr >= end) break;
        ++ptr;

        // Parser le prix directement depuis l'adresse memoire
        double prix = 0.0;
        auto res_prix = std::from_chars(ptr, end, prix);
        if (res_prix.ec != std::errc()) {
            while (ptr <  end && *ptr != '\n') ++ptr;
            if (ptr < end) ++ptr;
            continue;
        }
        ptr = res_prix.ptr;
        if (ptr >= end || *ptr != ',') {
            while (ptr < end && *ptr != '\n') ++ptr;
            if (ptr < end) ++ptr;
            continue;
        }
        ++ptr;

        double volume = 0.0;
        auto res_vol = std::from_chars(ptr, end, volume);
        if (res_vol.ec != std::errc()) {
            while (ptr < end && *ptr != '\n') ++ptr;
            if (ptr < end) ++ptr;
            continue;
        }
        ptr = res_vol.ptr;

        somme_prix += prix;
        volume_total += volume;
        nb_ticks++;
        
        if (nb_ticks >= 10000) {
            break;
        }

        while (ptr < end && *ptr != '\n') ++ptr;
        if (ptr < end && *ptr == '\n') ++ptr;
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duree = end_time - debut;
    double prix_moyen = (nb_ticks > 0) ? (somme_prix / nb_ticks) : 0.0;

    std::cout << "=== RAPPORT FASTICK C++ ===" << std::endl;
    std::cout << "ticks traites : " << nb_ticks << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << " Prix moyen : " << prix_moyen << " | Volume total : " << volume_total << std::endl;
    std::cout << "Temps d'execution: " << duree.count() << " ms" << std::endl;
    
    return 0;
    }