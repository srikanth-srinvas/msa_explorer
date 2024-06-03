import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog, QPushButton
from msa_utils import read_fasta_msa
from visualization import plot_conservation_heatmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.msa_data = None
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("MSA Explorer and Visualizer")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.load_button = QPushButton("Load MSA File", self)
        self.visualize_button = QPushButton("Create Visualization", self)

        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.visualize_button)

        self.load_button.clicked.connect(self.load_msa_file)
        self.visualize_button.clicked.connect(self.create_visualization)

    def load_msa_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select MSA File", "", "FASTA files (*.fasta)")

        if filepath:
            try:
                self.msa_data = read_fasta_msa(filepath)
            except Exception as e:
                # Handle errors gracefully
                pass

    def create_visualization(self):
        if self.msa_data:
            plot_conservation_heatmap(self.msa_data)
        else:
            # Display a message if no MSA data is loaded
            pass

def run_gui():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()
