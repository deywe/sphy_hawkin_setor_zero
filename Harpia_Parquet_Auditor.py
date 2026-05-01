import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import hashlib
import sys

def generate_sha256(data_array):
    """Gera o hash SHA256 para validação de integridade."""
    return hashlib.sha256(data_array.tobytes()).hexdigest()

def run_auditor(file_path='zero_sector_audit.parquet'):
    # 1. Carregamento dos dados
    try:
        df = pd.read_parquet(file_path)
        print(f"--- [HARPIA OS] FILE LOADED: {file_path} ---")
        print(f"Total Frames Found: {len(df)}")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # 2. Configuração do Visualizador
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#050505')
    x_axis = np.linspace(-10, 10, len(df.iloc[0]['field_snapshot']))
    
    line, = ax.plot([], [], color='#00f2ff', lw=1.5, label='Audited Phase Field')
    validation_text = ax.text(-9.5, 1.2, '', color='#00ff41', fontsize=10, family='monospace')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('#050505')
    ax.set_title("SPHY THEORY | INDEPENDENT DATA AUDIT (SHA256 VALIDATION)", color='white')
    ax.legend(loc='upper right', facecolor='#1a1a1a', labelcolor='white')

    def update(frame):
        row = df.iloc[frame]
        current_data = np.array(row['field_snapshot'])
        stored_hash = row['sha256_signature']
        
        # Auditoria em tempo real: Recalcula o hash e compara
        computed_hash = generate_sha256(current_data)
        integrity = "PASSED" if computed_hash == stored_hash else "FAILED"
        color = "#00ff41" if integrity == "PASSED" else "#ff0000"

        line.set_data(x_axis, current_data)
        validation_text.set_text(
            f"FRAME: {frame}\n"
            f"VERACITY (η): {row['veracity']:.4f}\n"
            f"EXPECTED HASH: {stored_hash[:24]}...\n"
            f"INTEGRITY CHECK: {integrity}"
        )
        validation_text.set_color(color)
        
        return line, validation_text

    ani = FuncAnimation(fig, update, frames=len(df), interval=50, repeat=True)
    
    print("--- MONITORING FIELD INTEGRITY... ---")
    plt.show()

if __name__ == "__main__":
    # Se você quiser abrir um arquivo específico: python auditor.py meu_arquivo.parquet
    target_file = sys.argv[1] if len(sys.argv) > 1 else 'zero_sector_audit.parquet'
    run_auditor(target_file)
