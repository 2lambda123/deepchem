from deepchem.molnet.load_function.bace_datasets import load_bace_classification, load_bace_regression
from deepchem.molnet.load_function.bbbc_datasets import load_bbbc001, load_bbbc002
from deepchem.molnet.load_function.bbbp_datasets import load_bbbp
from deepchem.molnet.load_function.cell_counting_datasets import load_cell_counting
from deepchem.molnet.load_function.chembl_datasets import load_chembl
from deepchem.molnet.load_function.clearance_datasets import load_clearance
from deepchem.molnet.load_function.clintox_datasets import load_clintox
from deepchem.molnet.load_function.delaney_datasets import load_delaney
from deepchem.molnet.load_function.hiv_datasets import load_hiv
from deepchem.molnet.load_function.hopv_datasets import load_hopv
from deepchem.molnet.load_function.kaggle_datasets import load_kaggle
from deepchem.molnet.load_function.lipo_datasets import load_lipo
from deepchem.molnet.load_function.muv_datasets import load_muv
from deepchem.molnet.load_function.nci_datasets import load_nci
from deepchem.molnet.load_function.pcba_datasets import load_pcba, load_pcba_146, load_pcba_2475
from deepchem.molnet.load_function.pdbbind_datasets import load_pdbbind_grid, load_pdbbind, load_pdbbind_from_dir
from deepchem.molnet.load_function.ppb_datasets import load_ppb
from deepchem.molnet.load_function.qm7_datasets import load_qm7
from deepchem.molnet.load_function.qm7_datasets import load_qm7_from_mat, load_qm7b_from_mat
from deepchem.molnet.load_function.qm8_datasets import load_qm8
from deepchem.molnet.load_function.qm9_datasets import load_qm9
from deepchem.molnet.load_function.sampl_datasets import load_sampl
from deepchem.molnet.load_function.sider_datasets import load_sider
from deepchem.molnet.load_function.sweetlead_datasets import load_sweet
from deepchem.molnet.load_function.tox21_datasets import load_tox21
from deepchem.molnet.load_function.toxcast_datasets import load_toxcast
from deepchem.molnet.load_function.uspto_datasets import load_uspto
from deepchem.molnet.load_function.uv_datasets import load_uv
from deepchem.molnet.load_function.factors_datasets import load_factors
from deepchem.molnet.load_function.kinase_datasets import load_kinase
from deepchem.molnet.load_function.thermosol_datasets import load_thermosol
from deepchem.molnet.load_function.hppb_datasets import load_hppb
from deepchem.molnet.load_function.chembl25_datasets import load_chembl25

from deepchem.molnet.run_benchmark import run_benchmark
from deepchem.molnet import run_benchmark_models

# Deprecation warnings
from deepchem.applications.genomics import simulate_motif_density_localization as motif_density_localization
from deepchem.applications.genomics import simulate_motif_counting as motif_counting
from deepchem.applications.genomics import simple_motif_embedding as motif_embedding
from deepchem.applications.genomics import motif_density as density
from deepchem.applications.genomics import simulate_single_motif_detection as single_motif_detection


def simulate_motif_density_localization(*args, **kwargs):
  warnings.warn(
      "This function has been deprecated and now resides in deepchem.applications.genomics ",
      DeprecationWarning)
  motif_density_localization(*args, **kwargs)


def simulate_motif_counting(*args, **kwargs):
  warnings.warn(
      "This function has been deprecated and now resides in deepchem.applications.genomics ",
      DeprecationWarning)
  motif_counting(*args, **kwargs)


def simple_motif_embedding(*args, **kwargs):
  warnings.warn(
      "This function has been deprecated and now resides in deepchem.applications.genomics ",
      DeprecationWarning)
  motif_embedding(*args, **kwargs)


def motif_density(*args, **kwargs):
  warnings.warn(
      "This function has been deprecated and now resides in deepchem.applications.genomics ",
      DeprecationWarning)
  density(*args, **kwargs)


def simulate_single_motif_detection(*args, **kwargs):
  warnings.warn(
      "This function has been deprecated and now resides in deepchem.applications.genomics ",
      DeprecationWarning)
  single_motif_detection(*args, **kwargs)
