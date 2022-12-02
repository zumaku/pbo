#include <iostream>
using namespace std;

class Mahasiswa{
    public:
        string nama;
        int nim;
        char kelas;

        Mahasiswa(string namaku, int nimku, char kelasku){
            nama = namaku;
            nim = nimku;
            kelas = kelasku;
        }

        void ubahNama(string namaBaru){
            nama = namaBaru;
        }

        void ubahNim(int nimku){
            nim = nimku;
        }

        void ubahKelas(char kelasku){
            kelas = kelasku;
        }

        void cetak(){
            cout<<"Nama : "<<nama<<endl;
            cout<<"Nim : "<<nim<<endl;
            cout<<"Kelas : "<<kelas<<endl<<endl;
        }
};

int main(){

    Mahasiswa fadli("Zul Fadli", 101, 'B');
    fadli.cetak();


    return 0;
}