"""
plot.py  -  Ve bieu do phan tich Tai Xiu
Chay: python plot.py
      python plot.py ket_qua.csv ban_ghi.csv   (neu ten file khac)
Tu dong doc von ban dau va so van tu chinh file CSV, khong can sua code.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Doc ten file tu tham so dong lenh hoac dung mac dinh
ten_ket_qua = sys.argv[1] if len(sys.argv) > 1 else 'ket_qua.csv'
ten_ban_ghi = sys.argv[2] if len(sys.argv) > 2 else 'ban_ghi.csv'

print(f"Doc du lieu tu: {ten_ket_qua}, {ten_ban_ghi}")
# Thu cac encoding khac nhau de tranh loi tren Windows
for enc in ['utf-8', 'utf-8-sig', 'cp1258', 'latin-1']:
    try:
        ket_qua = pd.read_csv(ten_ket_qua, encoding=enc)
        ban_ghi = pd.read_csv(ten_ban_ghi, encoding=enc)
        print(f"  Encoding: {enc}")
        break
    except Exception:
        continue

# Dam bao Van_Moc la so nguyen
ban_ghi['Van_Moc'] = pd.to_numeric(ban_ghi['Van_Moc'], errors='coerce').fillna(0).astype(int)

# ── Tu dong lay VON_BD tu cot Von_Ban_Dau trong ket_qua
VON_BD     = float(ket_qua['Von_Ban_Dau'].iloc[0])
SO_VAN_MAX = float(ban_ghi['Van_Moc'].max())

print(f"  Von ban dau : {VON_BD:,.0f}")
print(f"  So van max  : {SO_VAN_MAX:,.0f}")

# ── Ham format truc tu dong theo do lon du lieu
def smart_fmt_tien(von):
    if von >= 1_000_000_000:
        return lambda x, _: f'{x/1_000_000_000:.1f}B'
    elif von >= 1_000_000:
        return lambda x, _: f'{x/1_000_000:.1f}M' if x >= 1_000_000 else f'{x/1_000:.0f}K'
    elif von >= 1_000:
        return lambda x, _: f'{x/1_000:.1f}K'
    else:
        return lambda x, _: f'{x:.0f}'

def smart_fmt_van(so_van):
    if so_van >= 1_000_000:
        return lambda x, _: f'{x/1_000_000:.1f}M' if x >= 1_000_000 else (f'{x/1_000:.0f}K' if x >= 1000 else str(int(x)))
    elif so_van >= 1_000:
        return lambda x, _: f'{x/1_000:.1f}K' if x >= 1000 else str(int(x))
    else:
        return lambda x, _: str(int(x))

def fmt_tien_nhan(x):
    if abs(x) >= 1_000_000_000: return f'{x/1_000_000_000:.1f}B'
    if abs(x) >= 1_000_000:     return f'{x/1_000_000:.1f}M'
    if abs(x) >= 1_000:         return f'{x/1_000:.1f}K'
    return f'{x:.0f}'

def fmt_van_nhan(x):
    if x >= 1_000_000: return f'{x/1_000_000:.1f}M'
    if x >= 1_000:     return f'{x/1_000:.0f}K'
    return str(int(x))

FMT_TIEN = smart_fmt_tien(VON_BD)
FMT_VAN  = smart_fmt_van(SO_VAN_MAX)

plt.rcParams['figure.dpi'] = 130
plt.rcParams['font.size'] = 9

# ── Mau sac va nhan
MAU_CT = {
    'Co_Dinh':       '#2196F3',
    'Dat_Nguoc':     '#4CAF50',
    '1-3-2-6':       '#FF9800',
    'Fibonacci':     '#9C27B0',
    'Gap_Doi_Thua':  '#F44336',
    'Gap_Doi_Thang': '#E91E63',
    'Tang_Giam_1DV': '#795548',
}
MAU_PB = {
    'TaiXiu':      '#1565C0',
    'Cham':        '#2E7D32',
    'Tong':        '#BF360C',
    'TX_va_Cham':  '#6A1B9A',
    'TX_va_Tong':  '#00838F',
    'Cham_va_Tong':'#F57F17',
    'TatCa':       '#37474F',
}
TEN_VIET = {
    'Co_Dinh':       'Co Dinh',
    'Dat_Nguoc':     'Dat Nguoc',
    '1-3-2-6':       '1-3-2-6',
    'Fibonacci':     'Fibonacci',
    'Gap_Doi_Thua':  'Gap Doi Thua',
    'Gap_Doi_Thang': 'Gap Doi Thang',
    'Tang_Giam_1DV': 'Tang/Giam 1DV',
}
TEN_PB_VIET = {
    'TaiXiu':      'Chi Tai/Xiu',
    'Cham':        'Chi Cham',
    'Tong':        'Chi Tong',
    'TX_va_Cham':  'TX + Cham',
    'TX_va_Tong':  'TX + Tong',
    'Cham_va_Tong':'Cham + Tong',
    'TatCa':       'Tat Ca',
}
CT_ORDER = ['Co_Dinh','Dat_Nguoc','1-3-2-6','Fibonacci',
            'Gap_Doi_Thua','Gap_Doi_Thang','Tang_Giam_1DV']
PB_ORDER = ['TaiXiu','Cham','Tong','TX_va_Cham',
            'TX_va_Tong','Cham_va_Tong','TatCa']

# ── Gioi han ban_ghi: chi lay den 40% so van max de thay su phan hoa
GIOI_HAN_VAN = int(SO_VAN_MAX * 0.9)
ban_ghi_cut = ban_ghi[ban_ghi['Van_Moc'] <= GIOI_HAN_VAN].copy()
if len(ban_ghi_cut) < 5:
    ban_ghi_cut = ban_ghi.copy()
    print("  [Canh bao] Khong loc duoc, dung toan bo ban_ghi")
print(f"  Bieu do duong von hien thi: 0 -> {fmt_van_nhan(ban_ghi_cut['Van_Moc'].max())} van")

# ═══════════════════════════════════════
#  BIEU DO 1: Bar ngang - tat ca 49
# ═══════════════════════════════════════
print("\nVe bieu do 1...")
fig1, ax1 = plt.subplots(figsize=(20, 18))
fig1.patch.set_facecolor('#F8F9FA')
ax1.set_facecolor('#FFFFFF')

# -1 = chua chay tui -> hien thi = SO_VAN_MAX, them (*) vao nhan
ket_qua_plot = ket_qua.copy()
ket_qua_plot['Van_Hien_Thi'] = ket_qua_plot['TB_Van_Het_Tien'].apply(
    lambda x: SO_VAN_MAX if x < 0 else x)
df_sorted = ket_qua_plot.sort_values('Van_Hien_Thi', ascending=True)
colors_bar = [MAU_CT.get(r['Ten_Chien_Thuat'], '#999') for _, r in df_sorted.iterrows()]
ax1.barh(range(len(df_sorted)), df_sorted['Van_Hien_Thi'],
         color=colors_bar, height=0.7, edgecolor='white', linewidth=0.4)
ax1.set_yticks(range(len(df_sorted)))
ax1.set_yticklabels(
    [f"{TEN_PB_VIET.get(r['Ten_Phan_Bo'],'?')} + {TEN_VIET.get(r['Ten_Chien_Thuat'],'?')}"
       + (" (*)" if r['TB_Van_Het_Tien'] < 0 else "")
     for _, r in df_sorted.iterrows()], fontsize=20)
ax1.xaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
ax1.set_xlabel('So van tru duoc (trung binh)', fontsize=13)
ax1.set_title(
    f'BIEU DO 1: Moi chien thuat tru duoc bao nhieu van truoc khi chay tui?\n'
    f'(Von ban dau: {fmt_tien_nhan(VON_BD)} | Tong so van: {fmt_van_nhan(SO_VAN_MAX)})',
    fontsize=20, fontweight='bold', pad=10)
legend_patches = [plt.Rectangle((0,0),1,1, color=MAU_CT[ct], label=TEN_VIET[ct])
                  for ct in CT_ORDER]
ax1.legend(handles=legend_patches, title='Chien Thuat Cuoc',
           loc='lower right', fontsize=16, title_fontsize=18,
           borderpad=1.5, labelspacing=1.2)
moc = SO_VAN_MAX * 0.4
ax1.axvline(x=moc, color='red', linestyle='--', linewidth=1, alpha=0.6)
ax1.text(moc * 1.01, len(df_sorted)-1, f'40%\n({fmt_van_nhan(moc)})', color='red', fontsize=7)
ax1.grid(axis='x', alpha=0.3, linewidth=0.5)
plt.tight_layout()
plt.savefig('bieu_do_1_so_van_tru_duoc.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
print("  => bieu_do_1_so_van_tru_duoc.png")

# ═══════════════════════════════════════
#  BIEU DO 2: Duong von - nhom PHAN BO
# ═══════════════════════════════════════
print("Ve bieu do 2...")
# Tăng nhẹ figsize từ (16, 13) lên (18, 15) để chữ to không bị chen lấn
fig2, axes2 = plt.subplots(3, 3, figsize=(18, 15))
fig2.patch.set_facecolor('#F8F9FA')
fig2.suptitle(
    f'BIEU DO 2: Duong von theo thoi gian - nhom theo cach phan bo cuoc\n'
    f'(Von ban dau: {fmt_tien_nhan(VON_BD)} | Hien thi den {fmt_van_nhan(ban_ghi_cut["Van_Moc"].max())} van)',
    fontsize=18, fontweight='bold', y=1.02) # Tăng từ 11 -> 18

for idx, pb in enumerate(PB_ORDER):
    ax = axes2[idx//3][idx%3]
    ax.set_facecolor('#FAFAFA')
    ax.axhline(y=VON_BD, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    for ct in CT_ORDER:
        col = f'{pb}_{ct}'
        if col in ban_ghi_cut.columns:
            ax.plot(ban_ghi_cut['Van_Moc'].values, ban_ghi_cut[col].values,
                    color=MAU_CT[ct], linewidth=1.3, label=TEN_VIET[ct], alpha=0.85)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(FMT_TIEN))
    ax.set_title(TEN_PB_VIET[pb], fontsize=14, fontweight='bold') # 9.5 -> 14
    ax.set_xlabel('So van', fontsize=12)                          # 7.5 -> 12
    ax.set_ylabel('Von con lai', fontsize=12)                     # 7.5 -> 12
    ax.tick_params(labelsize=11)                                  # 7 -> 11
    ax.grid(alpha=0.2, linewidth=0.4)

for idx in range(len(PB_ORDER), 9):
    axes2[idx//3][idx%3].set_visible(False)

ax_leg2 = axes2[2][1]; ax_leg2.set_visible(True); ax_leg2.set_facecolor('#F0F4FF')
ax_leg2.legend(handles=[plt.Line2D([0],[0], color=MAU_CT[ct], linewidth=2.5, label=TEN_VIET[ct]) for ct in CT_ORDER],
               loc='center', fontsize=14, title='Chien Thuat', title_fontsize=15, frameon=False) # 9.5, 10 -> 14, 15
ax_leg2.set_xticks([]); ax_leg2.set_yticks([])
ax_leg2.set_title('Chu thich mau', fontsize=14, fontweight='bold') # 9.5 -> 14

ax_note2 = axes2[2][2]; ax_note2.set_visible(True); ax_note2.set_facecolor('#FFF8E1')
ax_note2.text(0.5,0.5,'Nhan xet:\n\n- Moi CT deu ve 0\n\n- Co Dinh & Dat Nguoc\n  song lau nhat\n\n- Gap Doi & Fibonacci\n  chet rat som\n\n- Tang/Giam 1DV\n  chet nhanh nhat',
              transform=ax_note2.transAxes, ha='center', va='center', fontsize=13, linespacing=1.6, # 9 -> 13
              bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E1', alpha=0.9))
ax_note2.set_xticks([]); ax_note2.set_yticks([])
ax_note2.set_title('Ghi chu', fontsize=14, fontweight='bold') # 9.5 -> 14

plt.tight_layout()
plt.savefig('bieu_do_2_duong_von_theo_phan_bo.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
print("  => bieu_do_2_duong_von_theo_phan_bo.png")

# ═══════════════════════════════════════
#  BIEU DO 3: Duong von - nhom CHIEN THUAT
# ═══════════════════════════════════════
print("Ve bieu do 3...")
# Tăng nhẹ figsize từ (16, 13) lên (18, 15)
fig3, axes3 = plt.subplots(3, 3, figsize=(18, 15))
fig3.patch.set_facecolor('#F8F9FA')
fig3.suptitle(
    f'BIEU DO 3: Duong von theo thoi gian - nhom theo chien thuat cuoc\n'
    f'(Von ban dau: {fmt_tien_nhan(VON_BD)} | Hien thi den {fmt_van_nhan(ban_ghi_cut["Van_Moc"].max())} van)',
    fontsize=18, fontweight='bold', y=1.02) # 11 -> 18

for idx, ct in enumerate(CT_ORDER):
    ax = axes3[idx//3][idx%3]
    ax.set_facecolor('#FAFAFA')
    ax.axhline(y=VON_BD, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
    for pb in PB_ORDER:
        col = f'{pb}_{ct}'
        if col in ban_ghi_cut.columns:
            ax.plot(ban_ghi_cut['Van_Moc'].values, ban_ghi_cut[col].values,
                    color=MAU_PB[pb], linewidth=1.3, label=TEN_PB_VIET[pb], alpha=0.85)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(FMT_TIEN))
    ax.set_title(TEN_VIET[ct], fontsize=14, fontweight='bold', color=MAU_CT[ct]) # 9.5 -> 14
    ax.set_xlabel('So van', fontsize=12)                                         # 7.5 -> 12
    ax.set_ylabel('Von con lai', fontsize=12)                                    # 7.5 -> 12
    ax.tick_params(labelsize=11)                                                 # 7 -> 11
    ax.grid(alpha=0.2, linewidth=0.4)

for idx in range(len(CT_ORDER), 9):
    axes3[idx//3][idx%3].set_visible(False)

ax_leg3 = axes3[2][1]; ax_leg3.set_visible(True); ax_leg3.set_facecolor('#F0F4FF')
ax_leg3.legend(handles=[plt.Line2D([0],[0], color=MAU_PB[pb], linewidth=2.5, label=TEN_PB_VIET[pb]) for pb in PB_ORDER],
               loc='center', fontsize=14, title='Cach Phan Bo', title_fontsize=15, frameon=False) # 9.5, 10 -> 14, 15
ax_leg3.set_xticks([]); ax_leg3.set_yticks([])
ax_leg3.set_title('Chu thich mau', fontsize=14, fontweight='bold') # 9.5 -> 14

ax_note3 = axes3[2][2]; ax_note3.set_visible(True); ax_note3.set_facecolor('#E8F5E9')
ax_note3.text(0.5,0.5,'Nhan xet:\n\n- Chi Tai/Xiu song lau\n  nhat o da so CT cuoc\n\n- Chi Tong & Chi Cham\n  chet rat som\n\n- Da cua khong giup\n  song lau hon',
              transform=ax_note3.transAxes, ha='center', va='center', fontsize=13, linespacing=1.6, # 9 -> 13
              bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9', alpha=0.9))
ax_note3.set_xticks([]); ax_note3.set_yticks([])
ax_note3.set_title('Ghi chu', fontsize=14, fontweight='bold') # 9.5 -> 14

plt.tight_layout()
plt.savefig('bieu_do_3_duong_von_theo_chien_thuat.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
print("  => bieu_do_3_duong_von_theo_chien_thuat.png")

# ═══════════════════════════════════════
#  BIEU DO 4: Heatmap 7x7
# ═══════════════════════════════════════
print("Ve bieu do 4...")
matrix = np.zeros((7, 7))
for i, pb in enumerate(PB_ORDER):
    for j, ct in enumerate(CT_ORDER):
        row = ket_qua_plot[(ket_qua_plot['Ten_Phan_Bo']==pb) & (ket_qua_plot['Ten_Chien_Thuat']==ct)]
        if not row.empty:
            matrix[i, j] = float(row['Van_Hien_Thi'].values[0])
fig4, ax4 = plt.subplots(figsize=(11, 7))
fig4.patch.set_facecolor('#F8F9FA')
im = ax4.imshow(matrix, cmap='RdYlGn', aspect='auto', vmin=0, vmax=matrix.max())
ax4.set_xticks(range(7))
ax4.set_xticklabels([TEN_VIET[ct] for ct in CT_ORDER], fontsize=9, rotation=20, ha='right')
ax4.set_yticks(range(7))
ax4.set_yticklabels([TEN_PB_VIET[pb] for pb in PB_ORDER], fontsize=9)
for i in range(7):
    for j in range(7):
        val = matrix[i,j]
        ax4.text(j, i, fmt_van_nhan(val), ha='center', va='center',
                 fontsize=8.5, fontweight='bold',
                 color='black' if val > matrix.max()*0.5 else 'white')
cbar = fig4.colorbar(im, ax=ax4, shrink=0.8)
cbar.set_label('So van tru duoc', fontsize=9)
cbar.ax.yaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
ax4.set_xlabel('Chien Thuat Cuoc', fontsize=10, labelpad=8)
ax4.set_ylabel('Cach Phan Bo', fontsize=10)
ax4.set_title(
    f'BIEU DO 4: Heatmap so van tru duoc - 7x7 to hop\n'
    f'(Xanh = song lau | Do = chay tui som | Von: {fmt_tien_nhan(VON_BD)})',
    fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig('bieu_do_4_heatmap.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
print("  => bieu_do_4_heatmap.png")

# ═══════════════════════════════════════
#  BIEU DO 5: Top 7 vs Bot 7
# ═══════════════════════════════════════
print("Ve bieu do 5...")
df_s = ket_qua_plot.sort_values('Van_Hien_Thi', ascending=False).copy()
df_s['Nhan'] = df_s.apply(
    lambda r: f"{TEN_PB_VIET.get(r['Ten_Phan_Bo'],'?')}\n+{TEN_VIET.get(r['Ten_Chien_Thuat'],'?')}"
              + ("\n(*)" if r['TB_Van_Het_Tien'] < 0 else ""), axis=1)

top7 = df_s.head(7)
bot7 = df_s.tail(7).sort_values('Van_Hien_Thi', ascending=True)

# Tăng figsize từ (14, 6) lên (18, 8)
fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(18, 8))
fig5.patch.set_facecolor('#F8F9FA')
fig5.suptitle('BIEU DO 5: Top 7 song lau nhat vs Top 7 chet nhanh nhat\n(*) = chua chay tui sau het so van mo phong',
              fontsize=18, fontweight='bold', y=1.05) # 11 -> 18, thêm y để cách tiêu đề

# --- TOP 7 ---
bars_top = ax5a.barh(range(7), top7['Van_Hien_Thi'],
                     color=[MAU_CT.get(ct,'#999') for ct in top7['Ten_Chien_Thuat']],
                     height=0.6, edgecolor='white')
ax5a.set_yticks(range(7))
ax5a.set_yticklabels(top7['Nhan'].values, fontsize=13) # 8.5 -> 13
ax5a.xaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
ax5a.set_title('TOP 7 - Song lau nhat', fontsize=16, fontweight='bold', color='#2E7D32') # 10 -> 16
ax5a.set_xlabel('So van tru duoc', fontsize=14) # Thêm fontsize
ax5a.tick_params(axis='x', labelsize=12) # Tăng font số trục x
ax5a.set_facecolor('#F1F8E9'); ax5a.grid(axis='x', alpha=0.3)

for bar, (_, row) in zip(bars_top, top7.iterrows()):
    label = fmt_van_nhan(row['Van_Hien_Thi']) + (" (*)" if row['TB_Van_Het_Tien'] < 0 else "")
    ax5a.text(bar.get_width()*1.01, bar.get_y()+bar.get_height()/2,
              label, va='center', fontsize=12) # 8 -> 12

# --- BOT 7 ---
bars_bot = ax5b.barh(range(7), bot7['Van_Hien_Thi'],
                     color=[MAU_CT.get(ct,'#999') for ct in bot7['Ten_Chien_Thuat']],
                     height=0.6, edgecolor='white')
ax5b.set_yticks(range(7))
ax5b.set_yticklabels(bot7['Nhan'].values, fontsize=13) # 8.5 -> 13
ax5b.xaxis.set_major_formatter(mticker.FuncFormatter(FMT_VAN))
ax5b.set_title('TOP 7 - Chet nhanh nhat', fontsize=16, fontweight='bold', color='#C62828') # 10 -> 16
ax5b.set_xlabel('So van tru duoc', fontsize=14) # Thêm fontsize
ax5b.tick_params(axis='x', labelsize=12) # Tăng font số trục x
ax5b.set_facecolor('#FFEBEE'); ax5b.grid(axis='x', alpha=0.3)

for bar, (_, row) in zip(bars_bot, bot7.iterrows()):
    ax5b.text(max(bar.get_width()*1.05, bar.get_width()+0.5),
              bar.get_y()+bar.get_height()/2, fmt_van_nhan(row['Van_Hien_Thi']), va='center', fontsize=12) # 8 -> 12

plt.tight_layout()
plt.savefig('bieu_do_5_top_bot.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
print("  => bieu_do_5_top_bot.png")

print("\nHoan thanh! Da tao 5 file PNG.")