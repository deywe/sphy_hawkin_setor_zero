# SPHY Zero Sector: Hawking Paradox Resolution

This repository contains the formal proof, forensic datasets, and visual auditing tools for the **SPHY Theory** resolution of the Hawking Information Paradox. By replacing static metrics with **Stationary Phase Hamiltonians**, we demonstrate that information is not lost during black hole evaporation but is preserved within the **Zero Sector** as a state of infinite coherent compression.

## 📑 Contents

*   **`Harpia_setor_zero.py`**: A high-fidelity 3D Visual Auditor built on the Ursina Engine. It renders the informational field as a dynamic 3D mesh, demonstrating "Phase Tension" in real-time.
*   **`zero_sector_audit.parquet`**: A forensic dataset containing field snapshots and veracity ($\eta$) metrics.
*   **`requirements.txt`**: Dependency list for the Harpia QOS environment.
*   **Scientific Article**: Formal mathematical proof using Confinement Hamiltonian Operators.

---

## 🔍 Visual Auditor & SHA-256 Validation

The included auditor (`Harpia_setor_zero.py`) is designed for **Digital Forensic Validation**. It does not merely animate data; it validates the integrity of every single frame against a cryptographic hash.

*   **Real-time Integrity**: The auditor reads the `.parquet` file and re-calculates the SHA-256 signature of the field data frame-by-frame.
*   **Visual Confirmation**: If the calculated hash matches the signed metadata, the system displays `INTEGRITY: SHA256 VALIDATED`.
*   **Phase Tension Visualization**: Users can observe how the field stabilizes into a "Stationary Node" as Veracity ($\eta$) approaches $1.0$, effectively silencing the "Hawking Noise".

---

## 📊 Dataset (Parquet)

The `zero_sector_audit.parquet` file provides the raw data for independent verification. It utilizes a columnar storage format for high-performance analysis of the following features:
*   **Field Snapshots**: 500-point arrays representing the state of the informational wave.
*   **Veracity ($\eta$)**: The coupling constant defining the proximity to the Zero Sector.
*   **SHA-256 Signatures**: Unique cryptographic identifiers for each state, ensuring the dataset has not been tampered with.

---

## 🚀 Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/deywe/sphy_hawkin_setor_zero/
    cd sphy_hawkin_setor_zero
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the 3D Auditor**:
    ```bash
    python3 Harpia_setor_zero.py
    
```

---

## 🏛️ Theoretical Framework

The resolution of the paradox lies in the **Transition Hamiltonian ($\hat{H}_{\eta}$)**. Unlike traditional Hawking-Bekenstein entropy, SPHY theory posits that information suffers a phase transition into a **Zero Sector Hamiltonian ($\hat{H}_{Z}$)**. In this state, translational degrees of freedom collapse into pure rotational nodes, preserving the system's total information as a latent vibration in the vacuum fabric.

**"The black hole is not a cosmic trash can; it is a vault secured by phase."**
