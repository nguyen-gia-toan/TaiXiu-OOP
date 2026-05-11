#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <iomanip>
#include <map>
#include <cmath>
#include <chrono>

using namespace std;

string TEN_CHIEN_THUAT[] = {
    "Co_Dinh",
    "Gap_Doi_Thua",
    "Gap_Doi_Thang",
    "Dat_Nguoc",
    "Fibonacci",
    "1-3-2-6",
    "Tang_Giam_1DV"
};


string TEN_PHAN_BO[] = {
    "TaiXiu",
    "Cham",
    "Tong",
    "TX_va_Cham",
    "TX_va_Tong",
    "Cham_va_Tong",
    "TatCa"
};


double tyLeThuongTong(int tong) {
    if (tong == 4  || tong == 17) return 50.0;
    if (tong == 5  || tong == 16) return 18.0;
    if (tong == 6  || tong == 15) return 14.0;
    if (tong == 7  || tong == 14) return 12.0;
    if (tong == 8  || tong == 13) return  8.0;
    return 6.0;
}

struct KetQuaVan {
    int mat1, mat2, mat3;
    int tong;
    bool laTai;
    bool laBao;
};

class XucXac {
private:
    mt19937& rng;

public:
    XucXac(mt19937& boRNG) : rng(boRNG) {}

    int tung() {
        uniform_int_distribution<int> tao_so_ngau_nhien(1, 6);
        return tao_so_ngau_nhien(rng);
    }
};

class NhaCai {
private:
    XucXac vien1, vien2, vien3;

public:
    NhaCai(mt19937& boRNG)
        : vien1(boRNG),
          vien2(boRNG),
          vien3(boRNG)
    {}

    KetQuaVan moBat() {
        KetQuaVan ketQua;
        ketQua.mat1 = vien1.tung();
        ketQua.mat2 = vien2.tung();
        ketQua.mat3 = vien3.tung();
        ketQua.tong = ketQua.mat1 + ketQua.mat2 + ketQua.mat3;
        ketQua.laBao = (ketQua.mat1 == ketQua.mat2 && ketQua.mat2 == ketQua.mat3);
        ketQua.laTai = (ketQua.tong >= 11);
        return ketQua;
    }
};

class ConBac {
private:
    string ten;
    int ChienThuat;
    int cachPhanBo;
    double vonHienTai;
    double vonBanDau;
    double donViCuoc;
    double cuocHienTai;
    int fibIdx;
    int buoc1326;
    bool ketQuaTruoc;
    long long soVanDaChoi;
    long long soVanThang;
    long long soVanThua;
    long long soVanBao;
    double vonCaoNhat;
    double vonThapNhat;
    bool daHetTien;
    long long vanHetTien;

    static const vector<double> DAY_FIBONACCI;

public:
    ConBac(const string& tenNguoiChoi, int chienThuat, int phanBo,
           double vonKhoiDau, double cuocCoBan) 
    {
        ten = tenNguoiChoi;
        ChienThuat = chienThuat;
        cachPhanBo = phanBo;
        vonHienTai = vonKhoiDau;
        vonBanDau = vonKhoiDau;
        donViCuoc = cuocCoBan;
        cuocHienTai = cuocCoBan;
        fibIdx = 0;
        buoc1326 = 0;
        ketQuaTruoc = true;
        soVanDaChoi = 0;
        soVanThang = 0;
        soVanThua = 0;
        soVanBao = 0;
        vonCaoNhat = vonKhoiDau;
        vonThapNhat = vonKhoiDau;
        daHetTien = false;
        vanHetTien = -1;
    }

    void datCuoc(const KetQuaVan& ketQua) {
        if (daHetTien) return;

        if (vonHienTai < donViCuoc) {
            daHetTien = true;
            vanHetTien = soVanDaChoi;
            return;
        }

        double tienCuoc = min(cuocHienTai, vonHienTai);
        vonHienTai -= tienCuoc;
        soVanDaChoi++;

        double thuVe = 0.0;
        double tienCuocTX    = tienCuoc;
        double tienCuocCham  = tienCuoc;
        double tienCuocTong  = tienCuoc;

        if (cachPhanBo == 3 || cachPhanBo == 4 || cachPhanBo == 5) {
            tienCuocTX   = tienCuoc / 2.0;
            tienCuocCham = tienCuoc / 2.0;
            tienCuocTong = tienCuoc / 2.0;
        } else if (cachPhanBo == 6) {
            tienCuocTX   = tienCuoc / 3.0;
            tienCuocCham = tienCuoc / 3.0;
            tienCuocTong = tienCuoc / 3.0;
        }

        double thuVeTX = 0.0;
        if (cachPhanBo == 0 || cachPhanBo == 3 || cachPhanBo == 4 || cachPhanBo == 6) {
            if (ketQua.laBao) {
                soVanBao++;
            } else if (ketQua.laTai) {
                thuVeTX = tienCuocTX * 2.0;
            }
        }

        double thuVeCham = 0.0;
        if (cachPhanBo == 1 || cachPhanBo == 3 || cachPhanBo == 5 || cachPhanBo == 6) {
            int soVienRa6 = 0;
            if (ketQua.mat1 == 6) soVienRa6++;
            if (ketQua.mat2 == 6) soVienRa6++;
            if (ketQua.mat3 == 6) soVienRa6++;

            if (soVienRa6 > 0) {
                thuVeCham = tienCuocCham + tienCuocCham * soVienRa6;
            }
        }

        double thuVeTong = 0.0;
        if (cachPhanBo == 2 || cachPhanBo == 4 || cachPhanBo == 5 || cachPhanBo == 6) {
            if (!ketQua.laBao && ketQua.tong == 10) {
                thuVeTong = tienCuocTong + tienCuocTong * tyLeThuongTong(10);
            }
        }

        thuVe = thuVeTX + thuVeCham + thuVeTong;
        vonHienTai += thuVe;

        bool thang = (thuVe > tienCuoc);
        if (thang) soVanThang++;
        else       soVanThua++;

        vonCaoNhat = max(vonCaoNhat, vonHienTai);
        vonThapNhat = min(vonThapNhat, vonHienTai);

        ketQuaTruoc = ketQua.laTai;
        capNhatChienThuat(thang);
    }

private:
    void capNhatChienThuat(bool VuaThang) {
        double CUOC_1326[] = {1.0, 3.0, 2.0, 6.0};

        switch (ChienThuat) {
            case 0:
                cuocHienTai = donViCuoc;
                break;
            case 1:
                if (VuaThang) cuocHienTai = donViCuoc;
                else cuocHienTai = cuocHienTai * 2.0;
                break;
            case 2:
                if (VuaThang) cuocHienTai = cuocHienTai * 2.0;
                else cuocHienTai = donViCuoc;
                break;
            case 3:
                cuocHienTai = donViCuoc;
                break;
            case 4:
                if (!VuaThang) {
                    fibIdx = min(fibIdx + 1, (int)DAY_FIBONACCI.size() - 1);
                } else {
                    fibIdx = max(0, fibIdx - 2);
                }
                cuocHienTai = donViCuoc * DAY_FIBONACCI[fibIdx];
                break;
            case 5:
                if (VuaThang) buoc1326 = (buoc1326 + 1) % 4;
                else buoc1326 = 0;
                cuocHienTai = donViCuoc * CUOC_1326[buoc1326];
                break;
            case 6:
                if (!VuaThang) cuocHienTai += donViCuoc;
                else cuocHienTai -= donViCuoc;
                if (cuocHienTai < donViCuoc) cuocHienTai = donViCuoc;
                break;
        }

        if (cuocHienTai > vonHienTai && vonHienTai > 0)
            cuocHienTai = vonHienTai;
        if (cuocHienTai < donViCuoc)
            cuocHienTai = donViCuoc;
    }

public:
    string getTen() const { return ten; }
    int getChienThuat() const { return ChienThuat; }
    int getPhanBo() const { return cachPhanBo; }
    double getVon() const { return vonHienTai; }
    double getVonBanDau() const { return vonBanDau; }
    double getVonCaoNhat() const { return vonCaoNhat; }
    double getVonThapNhat() const { return vonThapNhat; }
    long long getSoVanChoi() const { return soVanDaChoi; }
    long long getSoVanThang() const { return soVanThang; }
    long long getSoVanThua() const { return soVanThua; }
    long long getSoVanBao() const { return soVanBao; }
    bool isHetTien() const { return daHetTien; }
    long long getVanHetTien() const { return vanHetTien; }

    double phanTramConLai() const {
        return vonHienTai / vonBanDau * 100.0;
    }

    double loiNhuan() const {
        return vonHienTai - vonBanDau;
    }

    double tyLeThang() const {
        if (soVanDaChoi == 0) return 0.0;
        return 100.0 * soVanThang / soVanDaChoi;
    }
};

const vector<double> ConBac::DAY_FIBONACCI =
    {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765};

struct ThongKeTichLuy {
    double tongVonCuoi = 0;
    double tongLoiNhuan = 0;
    double tongPhanTram = 0;
    double tongTyLeThang = 0;
    long long tongVanThang = 0;
    long long tongVanThua = 0;
    long long tongVanBao = 0;
    double tongVonCaoNhat = 0;
    double tongVonThapNhat = 0;
    int soLanHetTien = 0;
    long long tongVanHetTien = 0; 
};

struct KetQuaHienThi {
    string ten;
    double tbVonCuoi;
    double tbPhanTram;
    double tyLeHetTien;
};

class MoPhong {
private:
    long long soVan;
    double    vonBanDau;
    double    donViCuoc;
    int       SoMoc;

public:
    MoPhong(long long tongSoVan  = 100000,
              double vonKhoiDau    = 300000000.0,
              double cuocCoBan     = 30000.0,
              int    soMoc         = 256)
        : soVan(tongSoVan),
          vonBanDau(vonKhoiDau),
          donViCuoc(cuocCoBan),
          SoMoc(soMoc)
    {}

    void phanTichXacSuat(const string& tenFile, long long soVanXS = 500000) {
        mt19937 rng(42);
        XucXac xucXac(rng);

        map<int, long long> demTong;
        long long demMat[7] = {0};
        long long demBao = 0, demTai = 0, demXiu = 0;

        for (long long i = 0; i < soVanXS; i++) {
            int m1 = xucXac.tung();
            int m2 = xucXac.tung();
            int m3 = xucXac.tung();
            int tong = m1 + m2 + m3;

            demTong[tong]++;
            demMat[m1]++;
            demMat[m2]++;
            demMat[m3]++;

            if (m1 == m2 && m2 == m3) demBao++;
            if (tong >= 11) demTai++; else demXiu++;
        }

        ofstream f(tenFile);
        f << fixed << setprecision(4);
        f << "Loai,So_Van,Xac_Suat_Pct\n";
        f << "Tai,"  << demTai << "," << 100.0 * demTai / soVanXS << "\n";
        f << "Xiu,"  << demXiu << "," << 100.0 * demXiu / soVanXS << "\n";
        f << "Bao,"  << demBao << "," << 100.0 * demBao / soVanXS << "\n\n";

        long long tongMat = soVanXS * 3;
        f << "Mat_Xuc_Xac,So_Lan_Xuat_Hien,Xac_Suat_%\n";
        for (int m = 1; m <= 6; m++) {
            f << "Mat_" << m << "," << demMat[m] << "," << 100.0 * demMat[m] / tongMat << "\n";
        }
        f << "\n";

        f << "Tong_Diem,So_Van,Xac_Suat_Pct,Ty_Le_Thuong,Loi_Nhuan_Khi_Thang\n";
        for (auto it = demTong.begin(); it != demTong.end(); ++it) {
            int t = it->first;
            long long c = it->second;
            double xs = 100.0 * c / soVanXS;
            double tyLe = tyLeThuongTong(t);
            double loiNhuanKyVong = xs / 100.0 * tyLe - (1.0 - xs / 100.0);
            f << t << "," << c << "," << xs << "," << tyLe << "," << setprecision(6) << loiNhuanKyVong << "\n";
        }
    }

    void ChayMoPhongNhieuLan(const string& tenFileKetQua, const string& tenFilebanghi, int soLanChay) {

        vector<ThongKeTichLuy> acc(49);
        vector<vector<double>> banghiTong(SoMoc + 1, vector<double>(49, 0.0));
        long long DiemMoc = soVan / SoMoc;

        for (int lan = 1; lan <= soLanChay; lan++) {
            auto hienTai = chrono::steady_clock::now().time_since_epoch().count() + lan;
            mt19937 rng((unsigned)hienTai);
            NhaCai nhaCai(rng);

            vector<ConBac> danhSach;
            danhSach.reserve(49);
            for (int pb = 0; pb < 7; pb++) {
                for (int ct = 0; ct < 7; ct++) {
                    string ten = TEN_PHAN_BO[pb] + "_" + TEN_CHIEN_THUAT[ct];
                    danhSach.push_back(ConBac(ten, ct, pb, vonBanDau, donViCuoc));
                }
            }

            vector<vector<double>> banghiLanNay(SoMoc + 1, vector<double>(49, vonBanDau));

            for (long long van = 0; van < soVan; van++) {
                KetQuaVan ketQua = nhaCai.moBat();
                for (ConBac& cb : danhSach) cb.datCuoc(ketQua);

                if (DiemMoc > 0 && (van + 1) % DiemMoc == 0) {
                    int moc = (int)((van + 1) / DiemMoc);
                    if (moc <= SoMoc) {
                        for (int i = 0; i < 49; i++) banghiLanNay[moc][i] = danhSach[i].getVon();
                    }
                }
            }

            for (int i = 0; i < 49; i++) {
                acc[i].tongVonCuoi += danhSach[i].getVon();
                acc[i].tongLoiNhuan += danhSach[i].loiNhuan();
                acc[i].tongPhanTram += danhSach[i].phanTramConLai();
                acc[i].tongTyLeThang += danhSach[i].tyLeThang();
                acc[i].tongVanThang += danhSach[i].getSoVanThang();
                acc[i].tongVanThua += danhSach[i].getSoVanThua();
                acc[i].tongVanBao += danhSach[i].getSoVanBao();
                acc[i].tongVonCaoNhat += danhSach[i].getVonCaoNhat();
                acc[i].tongVonThapNhat += danhSach[i].getVonThapNhat();
                if (danhSach[i].isHetTien()) {
                    acc[i].soLanHetTien++;
                    acc[i].tongVanHetTien += danhSach[i].getVanHetTien();
                }
            }
            
            for (int moc = 0; moc <= SoMoc; moc++) {
                for (int i = 0; i < 49; i++) {
                    banghiTong[moc][i] += banghiLanNay[moc][i];
                }
            }
        }

        ofstream f(tenFileKetQua);
        f << "Ten_Phan_Bo,Ten_Chien_Thuat,Ten_Phuong_Phap,Von_Ban_Dau,TB_Von_Cuoi,TB_Loi_Nhuan,TB_Phan_Tram,TB_Ty_Le_Thang,TB_Van_Thang,TB_Van_Thua,TB_Van_Bao,TB_Von_Cao_Nhat,TB_Von_Thap_Nhat,Ty_Le_Het_Tien_Pct,TB_Van_Het_Tien\n";

        vector<KetQuaHienThi> dsTop5;

        for (int pb = 0; pb < 7; pb++) {
            for (int ct = 0; ct < 7; ct++) {
                int i = pb * 7 + ct;
                
                double tbVonCuoi = acc[i].tongVonCuoi / soLanChay;
                double tbLoiNhuan = acc[i].tongLoiNhuan / soLanChay;
                double tbPhanTram = acc[i].tongPhanTram / soLanChay;
                double tbTyLeThang = acc[i].tongTyLeThang / soLanChay;
                double tbVanThang = (double)acc[i].tongVanThang / soLanChay;
                double tbVanThua = (double)acc[i].tongVanThua / soLanChay;
                double tbVanBao = (double)acc[i].tongVanBao / soLanChay;
                double tbVonCaoNhat = acc[i].tongVonCaoNhat / soLanChay;
                double tbVonThapNhat = acc[i].tongVonThapNhat / soLanChay;
                double tyLeHetTien = 100.0 * acc[i].soLanHetTien / soLanChay;
                double tbVanHetTien = (acc[i].soLanHetTien > 0) ? ((double)acc[i].tongVanHetTien / acc[i].soLanHetTien) : -1;

                string ten = TEN_PHAN_BO[pb] + "_" + TEN_CHIEN_THUAT[ct];

                f << TEN_PHAN_BO[pb] << "," << TEN_CHIEN_THUAT[ct] << "," << ten
                  << "," << fixed << setprecision(0) << vonBanDau << "," 
                  << tbVonCuoi << "," << tbLoiNhuan << "," << setprecision(4) << tbPhanTram << "," 
                  << tbTyLeThang << "," << tbVanThang << "," << tbVanThua << "," << tbVanBao << "," 
                  << setprecision(0) << tbVonCaoNhat << "," << tbVonThapNhat << "," 
                  << tyLeHetTien << "," << tbVanHetTien << "\n";

                dsTop5.push_back({ten, tbVonCuoi, tbPhanTram, tyLeHetTien});
            }
        }

        ofstream fbg(tenFilebanghi);
        fbg << "Van_Moc";
        for (int i = 0; i < 49; i++) fbg << "," << dsTop5[i].ten; 
        fbg << "\n";
        
        for (int moc = 0; moc <= SoMoc; moc++) {
            fbg << (long long)moc * DiemMoc;
            for (int i = 0; i < 49; i++) {
                fbg << "," << fixed << setprecision(0) << (banghiTong[moc][i] / soLanChay);
            }
            fbg << "\n";
        }

    }

    void ChayAll(int soLanChay = 50) {
        remove("ket_qua.csv");
        remove("ban_ghi.csv");
        phanTichXacSuat("xac_suat.csv");
        ChayMoPhongNhieuLan("ket_qua.csv", "ban_ghi.csv", soLanChay);
    }
};

int main() {
    long long soVan = 1000000;
    double vonKhoiDau = 300000000.0;
    double cuocCoBan = 30000.0;
    int soMoc = 1000000;
    
    cout << " Thong so mo phong:\n";
    cout << "   So van     : " << soVan << "\n";
    cout << "   Von ban dau: " << fixed << setprecision(0) << vonKhoiDau << " dong\n";
    cout << "   Cuoc co so : " << fixed << setprecision(0) << cuocCoBan << " dong\n";
    cout << "====================================================\n";

    MoPhong MoPhong(soVan, vonKhoiDau, cuocCoBan, soMoc);
    MoPhong.ChayAll(50);
    
    return 0;
}