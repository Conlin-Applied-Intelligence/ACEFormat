# A Compact ENDF (ACE) Format Specification

**Contributors**:\
Jeremy Lloyd Conlin (*Los Alamos National Laboratory*)\
Wim Haeck (*Los Alamos National Laboratory*)\
Paul Romano (*Argonne National Laboratory*)

LA-UR-19-29016

<a id="sec:Introduction"></a>

# Introduction

The ACE format consists of two *types* and many *classes* of data. The data are kept in an ACE Table. The term ACE Table and ACE file are often used interchangeably.

## Types of ACE-Formatted Data

There are two types of ACE-formatted data; simply called Type 1 and Type 2.

Type 1  
Standard formatted tables. These tables contain ASCII text and are machine independent; they are readable on every machine.

Type 2  
Standard unformatted tables. These tables are binary and can be generated from the Type 1 files. They are more compact and faster to read than the Type 1 ACE Tables but are machine/platform dependent; they are not readable on every machine.

Traditionally Type 2 ACE files were more commonly used because they were smaller in size and faster to read. However due to the fact that they are not portable across machines and platforms they have fallen out of fashion.

## Classes of ACE-Formatted Data

There are many classes of ACE-formatted data:

1.  continuous-energy neutron (see Section <a href="#sec:ContinuousEnergyNeutron" data-reference-type="ref" data-reference="sec:ContinuousEnergyNeutron">4</a>),

2.  discrete-reaction neutron,

3.  neutron dosimetry (see Section <a href="#sec:Dosimetry" data-reference-type="ref" data-reference="sec:Dosimetry">5</a>),

4.  $S(\alpha, \beta)$ thermal scattering (see Section <a href="#sec:ThermalScattering" data-reference-type="ref" data-reference="sec:ThermalScattering">6</a>),

5.  continuous-energy photoatomic (see Section <a href="#sec:ContinuousEnergyPhoton" data-reference-type="ref" data-reference="sec:ContinuousEnergyPhoton">7</a>),

6.  continuous-energy electron interaction,

7.  continuous-energy photonuclear interaction,

8.  multigroup-energy neutron, and

9.  multigroup-energy photoatomic.

Each of these classes of data are described later in this document.

An ACE Table is an entity that contains evaluation-dependent data about one of the many classes of data for a specific material—an target isotope, isomer, or element. For a given `ZAID`, the data contained on a Type 1 and Type 2 tables are identical. Simulations run with one type of data should produce identical results as those run with the other type of data.

## ACE Libraries

A collection of ACE data tables that derive from a single set of evaluation files are typically grouped together in a “library”—not to be confused from the evaluation library from which they derive. Multiple ACE data tables can concatenated into the same logical file on the computer, although this has fallen somewhat out of fashion due to the large amount of data on each ACE table derived from modern evaluation files. Applications that use ACE-formatted data should produce the same results regardless of whether the tables are contained in one logical file on the computer or spread across many.

# ACE Tables

An ACE Table consists of a Header followed by an array (`XSS`) containing the actual data. The Header and `XSS` array are the same regardless of whether the ACE Table is Type 1 or Type 2. Each line in a Type 1 ACE Table is 80 characters or less.

<a id="sec:ACEHeader"></a>

## ACE Header

The first section of an ACE Table is the Header. The ACE Header contains metadata[^1] about the ACE Table. The Header consists of four parts:

1.  Opening,

2.  `IZAW` array,

3.  `NXS` array, and

4.  `JXS` array.

An example of an ACE Table Header (from $^{1}\mathrm{H}$ in the ENDf71x library) is given in Figure <a href="#fig:HeaderExample" data-reference-type="ref" data-reference="fig:HeaderExample">1</a> with each part highlighted a different color.

<figure id="fig:HeaderExample" data-latex-placement="h!">
<div class="sourceCode" id="cb1" data-frame="single" data-fontsize="\footnotesize" data-commandchars="\\\{\}" data-numbers="left" data-numbersep="2pt"><pre class="sourceCode numberSource numberLines"><code class="sourceCode"><span id="cb1-1"><a href="#cb1-1" aria-label="1"></a>1001.80c    0.999167  2.5301E-08   12/17/12</span>
<span id="cb1-2"><a href="#cb1-2" aria-label="2"></a>H1 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)      mat 125</span>
<span id="cb1-3"><a href="#cb1-3" aria-label="3"></a>      0         0.      0         0.      0         0.      0         0.</span>
<span id="cb1-4"><a href="#cb1-4" aria-label="4"></a>      0         0.      0         0.      0         0.      0         0.</span>
<span id="cb1-5"><a href="#cb1-5" aria-label="5"></a>      0         0.      0         0.      0         0.      0         0.</span>
<span id="cb1-6"><a href="#cb1-6" aria-label="6"></a>      0         0.      0         0.      0         0.      0         0.</span>
<span id="cb1-7"><a href="#cb1-7" aria-label="7"></a>    17969     1001      590        3        0        1        1        0</span>
<span id="cb1-8"><a href="#cb1-8" aria-label="8"></a>        0        1        1        0        0        0        0        0</span>
<span id="cb1-9"><a href="#cb1-9" aria-label="9"></a>        1        0     2951     2954     2957     2960     2963     4352</span>
<span id="cb1-10"><a href="#cb1-10" aria-label="10"></a>     4353     5644     5644     5644     6234     6235     6236     6244</span>
<span id="cb1-11"><a href="#cb1-11" aria-label="11"></a>     6245     6245     6246    16721        0    16722        0        0</span>
<span id="cb1-12"><a href="#cb1-12" aria-label="12"></a>        0        0        0        0        0    16723    16724    16725</span></code></pre></div>
<figcaption>Header example. The (Legacy) Opening (lines 1–2) is in <span>red</span>, the <code>IZAW</code> array (lines 3–6) is in <span>blue</span>, the <code>NXS</code> array (lines 7–8) is in <span>teal</span>, and the <code>JXS</code> array (lines 9–12) is in <span>violet</span>.</figcaption>
</figure>

#### Legacy Header Opening

There are two slightly different formats for the Header Opening. The most common one found is called here the Legacy Opening and is the one demonstrated in the Header example in Figure <a href="#fig:HeaderExample" data-reference-type="ref" data-reference="fig:HeaderExample">1</a>.

The Legacy Opening consists of several variables given over two 80-character lines. The variables and the Fortran format for reading the variable is given in Table [1](#tab:LegacyHeader) <a id="tab:LegacyHeader"></a>

| Line | Variable | Format | Description |
|---:|:---|:---|:---|
| 1 | HZ | `A10` | `ZAID` (see Section <a href="#sec:ZAID" data-reference-type="ref" data-reference="sec:ZAID">3.1</a>) |
| 1 | AW | `E12.0` | Atomic weight ratio |
| 1 | TZ | `E12.0` | Temperature |
| 1 | — | `1X` | (blank space) |
| 1 | HD | `A10` | Processing date |
| 2 | HK | `A70` | Descriptive string |
| 2 | HM | `A10` | 10-character material identifier |

Variables in the Legacy Opening part of the ACE Header.

#### 2.0.1 Header Opening

There is a limitation to the number of unique `ZA` IDs for a given `ZA`; 100 different IDs, in fact, for each class of ACE Table. To overcome this limitation, a new Header Opening(Conlin et al. 2012) was developed in 2012 and updated a few years later to correct some errors.

<a id="tab:2.0Header"></a>

| Line | Variable | Format | Description |
|---:|:---|:---|:---|
| 1 | VERS | `A10` | Version format string |
| 1 | — | `1X` | (blank space) |
| 1 | HZ | `A24` | `SZAID` (see Section <a href="#sec:SZAID" data-reference-type="ref" data-reference="sec:SZAID">3.2</a>) |
| 1 | — | `1X` | (blank space) |
| 1 | SRC | `A24` | Evaluation source |
| 2 | AW | `E12.0` | Atomic weight ratio |
| 2 | — | `1X` | (blank space) |
| 2 | TZ | `E12.0` | Temperature |
| 2 | — | `1X` | (blank space) |
| 2 | HD | `A10` | Processing date |
| 2 | — | `1X` | (blank space) |
| 2 | N | `I4` | Number of comment lines to follow |
| 3–(`N`+2) | — | `A70` | `N` comment lines |

Variables in the 2.0.1 Opening part of the ACE Header.

<figure id="fig:HeaderOpeningExample" data-latex-placement="h!">
<pre data-frame="single" data-fontsize="\footnotesize" data-commandchars="\\\{\}"><code>2.0.1                    1001.800nc         ENDF/B-VIII.0-B1
    0.999167   2.5301e-08 2018-05-02    2
  1001.00c    0.999167  2.5301E-08   05/02/18
H1 Lib80x (jlconlin)  Ref. see jlconlin (ref 01/29/2018 07:54)           mat 125</code></pre>
<figcaption>Header Opening example. The Legacy Opening is shown in <span>blue</span> while the 2.0.1 Opening consists of the <span>red</span> and the <span>blue</span> portions.</figcaption>
</figure>

Note that a Legacy Header Opening can be contained in the comment section of the 2.0.1 Header Opening. This was designed explicitly to allow backwards compatibility while application codes were modified to be able to handle. An example of this is shown in Figure <a href="#fig:HeaderOpeningExample" data-reference-type="ref" data-reference="fig:HeaderOpeningExample">2</a>. Codes that cannot read the 2.0.1 Header can be told (typically via an xsdir(Conlin et al. 2012) entry) to start reading the ACE Table several lines after the beginning of the 2.0.1 Header.

Following the Opening of the Header are three arrays, `IZAW`, `NXS`, and `JXS` respectively. They are each described below. Immediately following the `JXS` array is the `XSS`array.

### `IZAW` Array

The `IZAW` array follows on the lines immediately following the Header. It consists of 16 pairs of `ZA`’s (`IZ`) and atomic weight ratios (`AW`). The `IZ` entries are still needed for $S(\alpha, \beta)$ Tables to indicate for which isotope(s) the scattering data are appropriate.

The 16 pairs of numbers are spread over 4 lines. The Fortran format for reading/writing the numbers on one line is: `4(I7,F11.0)`.

### `NXS` Array

The `NXS` array comes on the 2 lines after the `IZAW` array. The `NXS` array has 16 integer elements; 8 on each line. The Fortran format for reading/writing the numbers on each line is: `8I9`. The first element of the `NXS` array indicates how many numbers are in the `XSS` array. The remainder of the `NXS` array elements (usually) indicate how many of different pieces of data there is.

### `JXS` Array

The `JXS` array comes on the 4 lines after the `NXS` array. The `JXS` array has 32 integer elements; 8 on each line. The Fortran format for reading/writing the numbers on each line is: `8I9`. The `JXS` array contains indices to the `XSS` array where difference pieces of data begins.

The specific definition of the elements of the `NXS` and `JXS` arrays are dependent on the class of data in the Table and are defined in the section of this document that describes each class of data.[^2] Note that not all elements of the arrays are (currently) being used, allowing for future expansion.

## The `XSS` Array

After the ACE Header comes the `XSS` array. It is typically *very* large with hundreds of thousands of elements. It is broken up into blocks with the blocks being dependent on the class of data that is contained in the table. The description and definition of each of these blocks can be found in the descriptions later in this document.

The data is written with 4 floating-point numbers on each 80-character line. All data in the `XSS` array can be read using the Fortran format: `4E20.0` for each line.

<figure id="fig:XSSExample" data-latex-placement="h!">
<pre data-frame="single" data-fontsize="\footnotesize" data-numbersep="2pt"><code>2.0.1                    1001.710nc              ENDFB-VII.1
    0.999167   2.5301E-08   12/17/12    3
The next two lines are the first two lines of &#39;old-style&#39; ACE.
  1001.80c    0.999167  2.5301E-08   12/17/12
H1 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)      mat 125
      0         0.      0         0.      0         0.      0         0.
      0         0.      0         0.      0         0.      0         0.
      0         0.      0         0.      0         0.      0         0.
      0         0.      0         0.      0         0.      0         0.
    17969     1001      590        3        0        1        1        0
        0        1        1        0        0        0        0        0
        1        0     2951     2954     2957     2960     2963     4352
     4353     5644     5644     5644     6234     6235     6236     6244
     6245     6245     6246    16721        0    16722        0        0
        0        0        0        0        0    16723    16724    16725
   1.00000000000E-11   1.03125000000E-11   1.06250000000E-11   1.09375000000E-11
   1.12500000000E-11   1.15625000000E-11   1.18750000000E-11   1.21875000000E-11
   1.25000000000E-11   1.28125000000E-11   1.31250000000E-11   1.34375000000E-11
   1.37500000000E-11   1.43750000000E-11   1.50000000000E-11   1.56250000000E-11
   1.62500000000E-11   1.68750000000E-11   1.75000000000E-11   1.81250000000E-11
   1.87500000000E-11   1.93750000000E-11   2.00000000000E-11   2.09375000000E-11
   2.18750000000E-11   2.28125000000E-11   2.37500000000E-11   2.46875000000E-11
   2.56250000000E-11   2.65625000000E-11   2.75000000000E-11   2.84375000000E-11
   2.93750000000E-11   3.03125000000E-11   3.12500000000E-11   3.21875000000E-11
   3.31250000000E-11   3.40625000000E-11   3.50000000000E-11   3.59375000000E-11</code></pre>
<figcaption>ACE Header with beginning of <code>XSS</code> array for <span class="math inline"><sup>1</sup>H</span>. Note this uses the 2.0.1 Header with backwards compatibility with the Legacy Header.</figcaption>
</figure>

<a id="sec:UniqueIdentifier"></a>

# Unique ACE Table Identifier

**TODO:** This needs to be done. Each ACE Table needs to have an identifier to uniquely distinguish the data that is contained in the Table.

<a id="sec:ZAID"></a>

## `ZAID`

<a id="sec:SZAID"></a>

## `SZAID`

With the introduction of the 2.0.1 ACE Header, the identifier was modified to better specify the metastable state of the material as well as expand the available space for identifiers.

The new identifier is referred to as a `SZAID`[^3].

<a id="sec:ContinuousEnergyNeutron"></a>

# Continuous-Energy and Discrete Neutron Transport Tables

The format of individual blocks found on neutron transport tables is identical for continuous-energy and discrete-reaction ACE Tables; the format for both are described in this section. The blocks of data are:

1.  **[`ESZ` Block](#sec:ESZBlock)** — contains the main energy grid for the Table and the total, absorption, and elastic cross sections as well as the average heating numbers. The [`ESZ` Block](#sec:ESZBlock) always exists. See Section <a href="#sec:ESZBlock" data-reference-type="ref" data-reference="sec:ESZBlock">4.3.1</a>.

2.  **[`NU` Block](#sec:NUBlock)** — contains prompt, delayed and/or total $\overline{\nu}$ as a function of incident neutron energy. The [`NU` Block](#sec:NUBlock) exists only for fissionable isotopes; that is, if `JXS(2)`$\neq0$. See Section <a href="#sec:NUBlock" data-reference-type="ref" data-reference="sec:NUBlock">4.3.2</a>.

3.  **[`MTR` Block](#sec:MTRBlock)** — contains a list of ENDF MT numbers for all neutron reactions other than elastic scattering. The [`MTR` Block](#sec:MTRBlock) exists for all isotopes that have reactions other than elastic scattering; that is, all isotopes with `NXS(4)`$\neq0$. See Section <a href="#sec:MTRBlock" data-reference-type="ref" data-reference="sec:MTRBlock">4.3.4</a>.

4.  **[`LQR` Block](#sec:LQRBlock)** — contains a list of kinematic $Q$-values for all neutron reactions other than elastic scattering. The [`LQR` Block](#sec:LQRBlock) exists if `NXS(4)`$\neq0$. See Section <a href="#sec:LQRBlock" data-reference-type="ref" data-reference="sec:LQRBlock">4.3.5</a>.

5.  **[`TYR` Block](#sec:TYRBlock)** — contains information about the type of reaction for all neutron reactions other than elastic scattering. Information for each reaction includes the number of secondary neutrons and whether secondary neutron angular distributions are in the laboratory or center-of-masssystem. The [`TYR` Block](#sec:TYRBlock) exists if `NXS(4)`$\neq0$. See Section <a href="#sec:TYRBlock" data-reference-type="ref" data-reference="sec:TYRBlock">4.3.6</a>.

6.  **[`LSIG` Block](#sec:LSIGBlock)** — contains a list of cross section locators for all neutron reacitons other than elastic scattering. The [`LSIG` Block](#sec:LSIGBlock) exists if `NXS(4)`$\neq0$. See Section <a href="#sec:LSIGBlock" data-reference-type="ref" data-reference="sec:LSIGBlock">4.3.7</a>

7.  **[`SIG` Block](#sec:SIGBlock)** — contains cross sections for all reactions other than elastic scattering. The [`SIG` Block](#sec:SIGBlock) exists if `NXS(4)`$\neq0$. See Section <a href="#sec:SIGBlock" data-reference-type="ref" data-reference="sec:SIGBlock">4.3.8</a>.

8.  **[`LAND` Block](#sec:LANDBlock)** — contains a list of angular-distribution locators for all reactions producing secondary neutrons. The [`LAND` Block](#sec:LANDBlock) always exists. See Section <a href="#sec:LANDBlock" data-reference-type="ref" data-reference="sec:LANDBlock">4.3.9</a>.

9.  **[`AND` Block](#sec:ANDBlock)** — contains list angular distributions for all reactions producing secondary neutrons. The [`AND` Block](#sec:ANDBlock) always exists. See Section <a href="#sec:ANDBlock" data-reference-type="ref" data-reference="sec:ANDBlock">4.3.10</a>.

10. **[`LDLW` Block](#sec:LDLWBlock)** — contains a list of energy distributions for all reactions producing secondary neutrons except for elastic scattering. The [`LDLW` Block](#sec:LDLWBlock) exists if `NXS(5)`$\neq0$. See Section <a href="#sec:LDLWBlock" data-reference-type="ref" data-reference="sec:LDLWBlock">4.3.11</a>.

11. **[`DLW` Block](#sec:DLWBlock)** — contains energy distributions for all reactions producing secondary neutrons except for elastic scattering. The [`DLW` Block](#sec:DLWBlock) exists if `NXS(5)`$\neq0$. See Section <a href="#sec:DLWBlock" data-reference-type="ref" data-reference="sec:DLWBlock">4.3.12</a>.

12. **[`GPD` Block](#sec:GPDBlock)** — contains the total photon production cross section tabulated on the ESZ energy grid and a $30\times$ matrix of secondary photon energies. The [`GPD` Block](#sec:GPDBlock) exists only for those older evaluations that provide coupled neutron/photon information; that is, if `JXS(12)`$\neq0$. See Section <a href="#sec:GPDBlock" data-reference-type="ref" data-reference="sec:GPDBlock">4.3.13</a>.

13. **[`MTRP` Block](#sec:MTRPBlock)** — contains a list of MT numbers for all photon production reactions. The term “photon production reaction” is used for any information describing a specific neutron-in, photon-out reaction. The [`MTR` Block](#sec:MTRBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:MTRBlock" data-reference-type="ref" data-reference="sec:MTRBlock">4.3.4</a>.

14. **[`LSIGP` Block](#sec:LSIGPBlock)** — contains a list of cross section locators for all photon production reactions. The [`LSIGP` Block](#sec:LSIGPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:LSIGBlock" data-reference-type="ref" data-reference="sec:LSIGBlock">4.3.7</a>.

15. **[`SIGP` Block](#sec:SIGPBlock)** — contains cross sections for all photon production reactions. The [`SIGP` Block](#sec:SIGPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:SIGPBlock" data-reference-type="ref" data-reference="sec:SIGPBlock">4.3.14</a>.

16. **[`LANDP` Block](#sec:LANDPBlock)** — contains a list of angular-distribution locators for all photon production reactions. The [`LANDP` Block](#sec:LANDPBlock) exist if `NXS(6)`$\neq0$. See Section <a href="#sec:LANDBlock" data-reference-type="ref" data-reference="sec:LANDBlock">4.3.9</a>

17. **[`ANDP` Block](#sec:ANDPBlock)** — contains photon angular distributions for all photon production reactions. The [`ANDP` Block](#sec:ANDPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:ANDBlock" data-reference-type="ref" data-reference="sec:ANDBlock">4.3.10</a>.

18. **[`LDLWP` Block](#sec:LDLWPBlock)** — contains a list of energy-distribution locators for all photon production reactions. The [`LDLWP` Block](#sec:LDLWPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:LDLWBlock" data-reference-type="ref" data-reference="sec:LDLWBlock">4.3.11</a>.

19. **[`DLWP` Block](#sec:DLWPBlock)** — contains photon energy distributions for all photon production reactions. The [`DLWP` Block](#sec:DLWPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:DLWBlock" data-reference-type="ref" data-reference="sec:DLWBlock">4.3.12</a>.

20. **[`YP` Block](#sec:YPBlock)** — contains a list of MT identifiers of neutron reaction cross sections required as photon production yield multipliers. The [`YP` Block](#sec:YPBlock) exists if `NXS(6)`$\neq0$. See Section <a href="#sec:YPBlock" data-reference-type="ref" data-reference="sec:YPBlock">4.3.15</a>.

21. **[`FIS` Block](#sec:FISBlock)** — contains the total fission cross section tabulated on the ESZ energy grid. The [`FIS` Block](#sec:FISBlock) exists if `JXS(21)`$\neq0$. See Section <a href="#sec:FISBlock" data-reference-type="ref" data-reference="sec:FISBlock">4.3.16</a>.

22. **[`UNR` Block](#sec:UNRBlock)** — contains the unresolved resonance range probability tables. The [`UNR` Block](#sec:UNRBlock) exists if `JXS(23)`$\neq0$. See Section <a href="#sec:UNRBlock" data-reference-type="ref" data-reference="sec:UNRBlock">4.3.17</a>.

23. **[`PTYPE` Block](#sec:PTYPEBlock)** — contains a list of particle types for which production data will be given. The [`PTYPE` Block](#sec:PTYPEBlock) exists if `JXS(30)`$\neq0$. See Section <a href="#sec:PTYPEBlock" data-reference-type="ref" data-reference="sec:PTYPEBlock">4.3.18</a>.

24. **[`NTRO` Block](#sec:NTROBlock)** — contains the number of reactions that produce the corresponding particle type given in the [`PTYPE` Block](#sec:PTYPEBlock). The [`NTRO` Block](#sec:NTROBlock) exists if `JXS(31)`$\neq0$. See Section <a href="#sec:NTROBlock" data-reference-type="ref" data-reference="sec:NTROBlock">4.3.19</a>.

25. **[`IXS` Block](#sec:IXSBlock)** — particle production data locators for each particle type given in the [`PTYPE` Block](#sec:PTYPEBlock). The [`IXS` Block](#sec:IXSBlock) exists if `JXS(32)`$\neq 0$. See Section <a href="#sec:IXSBlock" data-reference-type="ref" data-reference="sec:IXSBlock">4.3.20</a>.

26. **[`HPD` Block](#sec:HPDBlock)** — total particle production cross section and average heating numbers for the current particle type. The [`HPD` Block](#sec:HPDBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) \neq 0$. See Section <a href="#sec:HPDBlock" data-reference-type="ref" data-reference="sec:HPDBlock">4.3.21</a>.

27. **[`MTRH` Block](#sec:MTRHBlock)** — contains a list of ENDF MT numbers for all reactions that produce the current particle. The [`MTR` Block](#sec:MTRBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 1 \neq 0$. See Section <a href="#sec:MTRBlock" data-reference-type="ref" data-reference="sec:MTRBlock">4.3.4</a>.

28. **[`TYRH` Block](#sec:TYRHBlock)** — contains the reaction types for all reactions that produce the current particle. The [`TYRH` Block](#sec:TYRHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 2 \neq 0$. See Section <a href="#sec:TYRBlock" data-reference-type="ref" data-reference="sec:TYRBlock">4.3.6</a>.

29. **[`LSIGH` Block](#sec:LSIGHBlock)** — contains the cross section locators for all reactions that produce the current particle. The [`LSIGH` Block](#sec:LSIGHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 3 \neq 0$. See Section <a href="#sec:LSIGBlock" data-reference-type="ref" data-reference="sec:LSIGBlock">4.3.7</a>.

30. **[`SIGH` Block](#sec:SIGHBlock)** — contains the cross section data for all reactions that produce the current particle. The [`SIGH` Block](#sec:SIGHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 4 \neq 0$. See Section <a href="#sec:SIGPBlock" data-reference-type="ref" data-reference="sec:SIGPBlock">4.3.14</a>.

31. **[`LANDH` Block](#sec:LANDHBlock)** — contains the angular distribution locators for all reactions that produce the current particle. The [`LANDH` Block](#sec:LANDHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 5 \neq 0$. See Section <a href="#sec:LANDBlock" data-reference-type="ref" data-reference="sec:LANDBlock">4.3.9</a>.

32. **[`ANDH` Block](#sec:ANDHBlock)** — contains the angular distribution data for all reactions that produce the current particle. The [`ANDH` Block](#sec:ANDHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 6 \neq 0$. See Section <a href="#sec:ANDBlock" data-reference-type="ref" data-reference="sec:ANDBlock">4.3.10</a>.

33. **[`LDLWH` Block](#sec:LDLWHBlock)** — contains the energy distribution locators for all reactions that produce the current particle. The [`LDLWH` Block](#sec:LDLWHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 7 \neq 0$. See Section <a href="#sec:LDLWBlock" data-reference-type="ref" data-reference="sec:LDLWBlock">4.3.11</a>.

34. **[`DLWH` Block](#sec:DLWHBlock)** — contains the energy distribution data for all reactions that produce the current particle. The [`DLWH` Block](#sec:DLWHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 8 \neq 0$. See Section <a href="#sec:DLWBlock" data-reference-type="ref" data-reference="sec:DLWBlock">4.3.12</a>.

35. **[`YH` Block](#sec:YHBlock)** — contains the particle production yield multiplier for all reactions that produce the current particle. The [`YH` Block](#sec:YHBlock) for a given particle type $i$ exists if $\texttt{JXS(32)}+10*(i-1) + 9 \neq 0$. See Section <a href="#sec:DLWBlock" data-reference-type="ref" data-reference="sec:DLWBlock">4.3.12</a>.

<a id="sec:NXSContinuousEnergyNeutron"></a>

## `NXS` Array

$\dagger$  
<a id="tn:2.0.0"></a> These values were introduced with the new 2.0.0 Header(Conlin et al. 2012).

$\ddagger$  
<a id="tn:Reserved"></a> These entries are reserved for the use of transport codes (i.e., MCNP).

<a id="tab:NXSContinuousEnergyNeutron"></a>

| Element | Name | Description |
|---:|:---|:---|
| 1 | — | Length of second block of data (`XSS` array) |
| 2 | `ZA` | $1000*Z+A$ |
| 3 | `NES` | Number of energies |
| 4 | `NTR` | Number of reactions excluding elastic scattering |
| 5 | `NR` | Number of reactions having secondary neutrons excluding elastic scattering |
| 6 | `NTRP` | Number of photon production reactions |
| 7 | `NTYPE` | Number of particle types for which production data is given |
| 8 | `NPCR` | Number of delayed neutron precurser families |
| 9 | `S` | Excited state<sup>[note](#tn:2.0.0)</sup> |
| 10 | `Z` | Atomic number<sup>[note](#tn:2.0.0)</sup> |
| 11 | `A` | Atomic mass number<sup>[note](#tn:2.0.0)</sup> |
|  | … |  |
| 14 |  | Reserved<sup>[note](#tn:Reserved)</sup> |
| 15 |  | Reserved<sup>[note](#tn:Reserved)</sup> |
| 16 |  | Reserved<sup>[note](#tn:Reserved)</sup> |

`NXS` array element definitions for continuous-energy neutron ACE Table.

<a id="sec:JXSContinuousEnergyNeutron"></a>

## `JXS` Array

<a id="tab:JXSContinuousEnergyNeutron"></a>

| Element | Name | Location Description |
|---:|:---|:---|
| 1 | `ESZ` | Energy table |
| 2 | `NU` | Fission $\nu$ data |
| 3 | `MTR` | `MT` array |
| 4 | `LQR` | $Q$-value array |
| 5 | `TYR` | Reaction type array |
| 6 | `LSIG` | Table of cross section locators |
| 7 | `SIG` | Cross sections |
| 8 | `LAND` | Table of angular distribution locators |
| 9 | `AND` | Angular distributions |
| 10 | `LDLW` | Table of energy distribution locators |
| 11 | `DLW` | Energy distributions |
| 12 | `GPD` | Photon production data |
| 13 | `MTRP` | Photon production `MT` array |
| 14 | `LSIGP` | Table of photon production cross section locators |
| 15 | `SIGP` | Photon production cross sections |
| 16 | `LANDP` | Table of photon production angular distribution locators |
| 17 | `ANDP` | Photon production angular distributions |
| 18 | `LDLWP` | Table of photon production energy distribution locators |
| 19 | `DLWP` | Photon production energy distributions |
| 20 | `YP` | Table of yield multipliers |
| 21 | `FIS` | Total fission cross section |
| 22 | `END` | Last word of the conventional table (last word of photon production data) |
| 23 | `LUNR` | Probability tables |
| 24 | `DNU` | Delayed $\overline{\nu}$ data |
| 25 | `BDD` | Basic delayed neutron precursor data ($\lambda$’s, probabilities) |
| 26 | `DNEDL` | Table of delayed neutron energy distribution locators |
| 27 | `DNED` | Delayed neutron energy distributions |
|  | … |  |
| 30 | `PTYPE` | Particle type array |
| 31 | `NTRO` | Array containing the number of particle production reactions |
| 32 | `NEXT` | Table of particle production locators (IXS array) |

`JXS` array element definitions for continuous-energy neutron ACE Table.

## Format of Individual Data Blocks

<a id="sec:ESZBlock"></a>

### <span class="sans-serif">ESZ</span> Block

The [`ESZ` Block](#sec:ESZBlock) provides the common incident energy table for all reactions defined in the ACE Table, cross section tables for fundamental cross sections (total, absorption, and elastic scattering) and average heating numbers. The format of the [`ESZ` Block](#sec:ESZBlock) is given in Table [5](#tab:ESZBlock). The starting index `ESZ` for this block is given by `JXS(1)`.

$\dagger$  
<a id="tn:DisappearanceXS"></a> The disappearance cross section is defined in (Trkov et al. 2011, Appendix B) as `MT`101

<a id="tab:ESZBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{ESZ}}$ | $E(l), l=1,\ldots, N_{E}$ | Energies |
| $S_{\mathrm{ESZ}}$ + $N_{E}$ | $\sigma_{t}(l), l=1,\ldots, N_{E}$ | Total cross section |
| $S_{\mathrm{ESZ}}$ + $2N_{E}$ | $\sigma_{a}(l), l=1,\ldots, N_{E}$ | Total neutron disappearance cross section<sup>[note](#tn:DisappearanceXS)</sup> |
| $S_{\mathrm{ESZ}}$ + $3N_{E}$ | $\sigma_{el}(l), l=1,\ldots, N_{E}$ | Elastic cross section |
| $S_{\mathrm{ESZ}}$ + $4N_{E}$ | $H_{ave}(l), l=1,\ldots, N_{E}$ | Average Heating numbers |

`ESZ` Block.

  
$S_{\mathrm{ESZ}}$ is index of the `XSS` array where the [`ESZ` Block](#sec:ESZBlock) starts, `JXS(1)`, and $N_{E}$ is the number of energy energy points, `NXS(3)`.

<a id="sec:NUBlock"></a>

### <span class="sans-serif">NU</span> and <span class="sans-serif">DNU</span> Blocks

<a id="sec:DNUBlock"></a>

The [`NU` Block](#sec:NUBlock) is used to specify prompt and/or total $\bar{\nu}$ and is present only if `JXS(2)` \> 0. Delayed $\bar{\nu}$ data is specified in the [`DNU` Block](#sec:DNUBlock) (which is only present if `JXS(24)` \> 0) but it shares some of the tables defined in this section.

When it is present, there are two possibilities for the [`NU` Block](#sec:NUBlock):

1.  **Either prompt or total $\bar{\nu}$ is given (but not both).** (`XSS(``JXS(2)``)` \> 0)\
    A single $\bar{\nu}$ array is given and it begins at location `XSS(KNU)` where `KNU` = `JXS(2)`.

2.  **Both prompt and total $\bar{\nu}$ are given.** (`XSS(``JXS(2)``)` \< 0). Two $\bar{\nu}$ arrays are given, one for prompt $\bar{\nu}$ and another for total $\bar{\nu}$. The absolute value of `XSS(``JXS(2)``)` is the location of the total $\bar{\nu}$ array so that the locations for the two $\bar{\nu}$ arrays are as follows:

    - The prompt $\bar{\nu}$ array begins at `XSS(KNU)` where `KNU` = `JXS(2)` + 1.

    - The total $\bar{\nu}$ array begins at `XSS(KNU)` where `KNU` = `JXS(2)` + ABS(`XSS(``JXS(2)``)`) + 1.

There are two possible forms for these $\bar{\nu}$ arrays; either polynomial (see Table [6](#tab:NUBlockPolynomial)) or tabulated (see Table [7](#tab:NUBlockTabulated)). The format is specified by the `LNU` flag located in the `XSS` array at index `KNU` where `KNU` is defined above.

<a id="tab:NUBlockPolynomial"></a>

| Location in `XSS` | Parameter                 | Description              |
|:------------------|:--------------------------|:-------------------------|
| `KNU`             | `LNU`=1                   | Polynomial function flag |
| `KNU`+1           | $N_{C}$                   | Number of coefficients   |
| `KNU`+2           | $C(l), l=1,\ldots, N_{C}$ | Coefficients             |

`NU` Block—Polynomial function form.

When using the polynomial function form of the $\bar{\nu}$ array, $\bar{\nu}$ is reconstructed as <a id="eq:nubarPolynomialReconstruction"></a> $$\ensuremath{\bar{\nu}}(E) = \sum_{l=1}^{N_{C}} C(l)E^{l-1},\tag{1}$$ where the energy, $E$, is given in MeV.

$\dagger$  
<a id="tn:scheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

<a id="tab:NUBlockTabulated"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `KNU` | `LNU`=2 | Tabulated data flag |
| `KNU`+1 | $N_{R}$ | Number of interpolation regions |
| `KNU`+2 | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `KNU`+2+$N_{R}$ | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:scheme)</sup> |
| `KNU`+2+$2N_{R}$ | $N_{E}$ | Number of energies |
| `KNU`+3+$2N_{R}$ | $E(l),l=1,\ldots,N_{E}$ | Tabulated energy points |
| `KNU`+3+$2N_{R}+N_{E}$ | $\ensuremath{\bar{\nu}}(l),l=1,\ldots,N_{E}$ | Tabulated $\bar{\nu}$ values |

`NU` Block—Tabulated form.

For the [`DNU` Block](#sec:DNUBlock), the delayed $\bar{\nu}$ array begins at `XSS(KNU)` where `KNU` = `JXS(24)`. Delayed $\bar{\nu}$ must be given in the tabulated form as described in Table [7](#tab:NUBlockTabulated). The polynomial form is not allowed in the [`DNU` Block](#sec:DNUBlock).

<a id="sec:BDDBlock"></a>

### <span class="sans-serif">BDD</span> Block

The [`BDD` Block](#sec:BDDBlock) is used to specify basic delayed neutron precursor data and is present only if `JXS(25)` \> 0. For every precursor group (the total number of precursor groups is given in `NXS(8)`), a decay constant is given along with the partial probability that a delayed fission neutron is born from the current group. This data is given in the format given in table Table [8](#tab:DelayedPrecursorDistribution). The starting index `BDD` for this block is given by `JXS(25)`.

$\dagger$  
<a id="tn:schemeDelayedPrecursors"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

<a id="tab:DelayedPrecursorDistribution"></a>

<table>
<caption>Delayed <span class="math inline"><em>ν̄</em></span> precursor distribution..</caption>
<thead>
<tr>
<th style="text-align: left;">Location in <code>XSS</code></th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for precursor group 1</strong></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code></span></td>
<td style="text-align: left;"><code>DEC</code><span class="math inline"><sub>1</sub></span></td>
<td style="text-align: left;">Decay constant for the group 1</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 1</span></td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;">Number of interpolation regions</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 2</span></td>
<td style="text-align: left;"><code>NBT</code><span class="math inline">(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;">ENDF interpolation parameters<sup><a href="#tn:schemeDelayedPrecursors">note</a></sup></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 2 + <em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;"><code>INT</code><span class="math inline">(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;">ENDF interpolation scheme</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 2 + 2<em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Number of energies</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 3 + 2<em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>E</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Tabulated energy points</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><code>BDD</code> + 3 + 2<em>N</em><sub><em>R</em></sub> + <em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>P</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Corresponding probabilities</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for precursor group 2—same format as for group 1</strong></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for precursor group <code>NPCR</code> = <code>NXS(8)</code>—same format as for group 1</strong></td>
</tr>
</tbody>
</table>

<a id="sec:MTRBlock"></a>

### <span class="sans-serif">MTR</span>, <span class="sans-serif">MTRP</span> and <span class="sans-serif">MTRH</span> Blocks

<a id="sec:MTRPBlock"></a><a id="sec:MTRHBlock"></a>

The format of the [`MTR` Block](#sec:MTRBlock) (for incident neutron reactions), [`MTRP` Block](#sec:MTRPBlock) (for photon production reactions) and [`MTRH` Block](#sec:MTRHBlock) (for particle production reactions), is given in Table [10](#tab:MTRBlock) and provides a list of `MT` numbers for which data is available in other blocks of the ACE Table. The starting index depends on whether it is the [`MTR` Block](#sec:MTRBlock), [`MTRP` Block](#sec:MTRPBlock) or [`MTRH` Block](#sec:MTRHBlock) and are given in Table [9](#tab:LMT_NMT). For the particle production [`MTRH` Block](#sec:MTRHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:LMT_NMT"></a>

| Block  | `LMT`                         | `NMT`                  |
|:-------|:------------------------------|:-----------------------|
| `MTR`  | `JXS(3)`                      | `NXS(4)`               |
| `MTRP` | `JXS(13)`                     | `NXS(6)`               |
| `MTRH` | `XSS(``JXS(32)``+10*(i-1)+1)` | `XSS(``JXS(31)``+i-1)` |

`LMT` and `NMT` values for the [`MTR` Block](#sec:MTRBlock) and [`MTRH` Block](#sec:MTRHBlock).

<a id="tab:MTRBlock"></a>

| Location in `XSS` | Parameter             | Description                    |
|:------------------|:----------------------|:-------------------------------|
| `LMT`             | `MT`$_{1}$            | First ENDF Reaction available  |
| `LMT`+1           | `MT`$_{2}$            | Second ENDF Reaction available |
| …                 |                       |                                |
| `LMT`+`NMT`-1     | `MT`$_{\texttt{NMT}}$ | Last ENDF reaction available   |

`MTR `<span class="nodecor">`&`</span>` MTRP` Block.

For the [`MTR` Block](#sec:MTRBlock) and [`MTRH` Block](#sec:MTRHBlock), `MT`$_{1},\ldots,\texttt{MT}_{\texttt{NMT}}$ are standard ENDF `MT`numbers; that is, `MT`=16=$(n,2n)$; `MT`=17=$(n,3n)$; etc. For a complete listing of `MT` numbers, see (Trkov et al. 2011, Appendix B). It is important to note here that the order in which these MT numbers are given is not arbitrary. The first `NXS(5)` values will be the MT numbers of reactions that produce secondary particles of the same type as the incident particle (i.e. there is secondary particle distribution data for the incident particle type for these reactions). The next $\texttt{NXS(4)} - \texttt{NXS(5)}$ values will then be the MT numbers for reactions that do not produce a secondary particle of the same type as the incident particle.

For the [`MTR` Block](#sec:MTRBlock), every `MT` number may appear only once. In the [`MTRH` Block](#sec:MTRHBlock), it is possible for a given `MT`number to appear twice if the same particle is also produced as the residual after the reaction (e.g. d + t -\> d + d).

For the [`MTRP` Block](#sec:MTRPBlock), the `MT` numbers are somewhat arbitrary. To understand the scheme used for numbering the photon production `MT`s, it is necessary to realize that in the ENDF format, more than one photon can be produced by a particular neutron reaction that is itself specified by a single `MT`. Each of these photons is produced with an individual energy-dependent cross section. For example, `MT`102 (radiative capture) might be responsible for 40 photons, each with its own cross section, angular distribution, and energy distribution. We need 40 photon `MT`s to represent the data; the `MT`s are numbered <span class="sans-serif">102001</span>, <span class="sans-serif">102002</span>, …, <span class="sans-serif">102040</span>. Therefore, if ENDF `MT` $N$ is responsible for $M$ photons, we shall number the photon `MT`s <span class="sans-serif">1000\*$N$+1</span>, <span class="sans-serif">1000\*$N$+2</span>, …, <span class="sans-serif">1000\*$N$+$M$</span>.

<a id="sec:LQRBlock"></a>

### <span class="sans-serif">LQR</span> Block

The format of the [`LQR` Block](#sec:LQRBlock), containing the reaction-specific $Q$-values, is given in Table [11](#tab:LQRBlock). The index at the start of the [`LQR` Block](#sec:LQRBlock), $S_{\mathrm{LQR}}$=`JXS(4)`. The number of reactions, `NMT`, is the same through the ACE Table, `NMT`=`NXS(4)`.

<a id="tab:LQRBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{LQR}}$ | $Q_{1}$ | $Q$-value for reaction `MT`$_{1}$ |
| $S_{\mathrm{LQR}}$+1 | $Q_{2}$ | $Q$-value for reaction `MT`$_{2}$ |
| … |  |  |
| $S_{\mathrm{LQR}}$+`NMT`-1 | $Q_{\texttt{NMT}}$ | $Q$-value for reaction `MT`$_{\texttt{NMT}}$ |

`LQR` Block.

<a id="sec:TYRBlock"></a>

### <span class="sans-serif">TYR</span> and <span class="sans-serif">TYRH</span> Blocks

<a id="sec:TYRHBlock"></a>

The format of the [`TYR` Block](#sec:TYRBlock) (for incident neutron reactions) and [`TYRH` Block](#sec:TYRHBlock) (for particle production reactions) is given in Table [13](#tab:TYRBlock). The starting index `LTYR` depends on whether it is the [`TYR` Block](#sec:TYRBlock) or [`TYRH` Block](#sec:TYRHBlock) and is given in Table [12](#tab:TYR_NMT). For the particle production [`TYRH` Block](#sec:TYRHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:TYR_NMT"></a>

| Block  | `LTYR`                        | `NMT`                  |
|:-------|:------------------------------|:-----------------------|
| `TYR`  | `JXS(5)`                      | `NXS(4)`               |
| `TYRH` | `XSS(``JXS(32)``+10*(i-1)+2)` | `XSS(``JXS(31)``+i-1)` |

`LTYR` and `NMT` values for the [`TYR` Block](#sec:TYRBlock) and [`TYRH` Block](#sec:TYRHBlock).

<a id="tab:TYRBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{LTYR}}$ | `TY`$_{1}$ | Particle release for reaction `MT`$_{1}$ |
| $S_{\mathrm{LTYR}}$+1 | `TY`$_{2}$ | Particle release for reaction `MT`$_{2}$ |
| … |  |  |
| $S_{\mathrm{LTYR}}$+`NMT`-1 | `TY`$_{\texttt{NMT}}$ | Particle release for reaction `MT`$_{\texttt{NMT}}$ |

`TYR` Block.

The possible values of `TY` are $\pm 1$, $\pm 2$, $\pm 3$, $\pm 4$, $\pm 19$, 0, and integers greater than 100 in absolute value; the sign indicates the system for scattering:

negative  
center-of-mass,

positive  
lab.

Thus if `TY`$_{i}$=+3, three particles are released for reaction `MT`$_{i}$ and the data on the cross section tables used to determine the exiting neutrons’ angles are given in the lab frame of reference. `TY`=19 indicates fission (only used in the [`TYR` Block](#sec:TYRBlock)). The number of secondary neutrons released is determined from the fission $\bar{\nu}$ data found in the [`NU` Block](#sec:NUBlock). `TY`$_{i}$=0 indicates absorption; no particles are released. $\left|\texttt{TY}_{i}\right|>100$ signifies reactions other than fission that have energy-dependent multiplicities (currently only used in the [`TYR` Block](#sec:TYRBlock)). The number of secondary particles released is determined from the yield data found in the [`DLW` Block](#sec:DLWBlock) or [`DLWH` Block](#sec:DLWHBlock). The `MT`$_{i}$s are given in the [`MTR` Block](#sec:MTRBlock) or [`MTRH` Block](#sec:MTRHBlock).

As the elastic scattering reaction is not included in the [`TYR` Block](#sec:TYRBlock), the reference frame used for this reaction is not given in the [`TYR` Block](#sec:TYRBlock) nor anywhere else in the ACE file. The reference frame for elastic scattering is always assumed to be the center-of-masssystem, since this is the way the data has to be given in the ENDF evaluation (Trkov et al. 2011, sec. 4.4.1).

<a id="sec:LSIGBlock"></a>

### <span class="sans-serif">LSIG</span>, <span class="sans-serif">LSIGP</span> and <span class="sans-serif">LSIGH</span> Blocks

<a id="sec:LSIGHBlock"></a><a id="sec:LSIGPBlock"></a>

The [`LSIG` Block](#sec:LSIGBlock) (for incident neutron cross sections), [`LSIGP` Block](#sec:LSIGPBlock) (for photon production cross sections) and [`LSIGH` Block](#sec:LSIGHBlock) (for particle production cross sections), give the locators for the cross section array for each reaction `MT`. A locator is a *relative* index in the `XSS` array where some piece of data can be found. In this case, the data are the cross section values. The format of the [`LSIG` Block](#sec:LSIGBlock), [`LSIGP` Block](#sec:LSIGPBlock) and [`LSIGH` Block](#sec:LSIGHBlock) is given in Table [15](#tab:LSIGBlock). The format for the incident neutron cross section arrays is given in Section <a href="#sec:SIGBlock" data-reference-type="ref" data-reference="sec:SIGBlock">4.3.8</a>, the format for the photon production cross sections is given in Section <a href="#sec:SIGPBlock" data-reference-type="ref" data-reference="sec:SIGPBlock">4.3.14</a> and the format for the particle production cross sections is given in Section <a href="#sec:SIGPBlock" data-reference-type="ref" data-reference="sec:SIGPBlock">4.3.14</a>.

The starting index `LXS` depends on whether it is the [`LSIG` Block](#sec:LSIGBlock), [`LSIGP` Block](#sec:LSIGPBlock) or [`LSIGH` Block](#sec:LSIGHBlock) and are given in Table [14](#tab:LXS_NMT). For the particle production [`LSIGH` Block](#sec:LSIGHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:LXS_NMT"></a>

| Block   | `LXS`                         | `NMT`                  |
|:--------|:------------------------------|:-----------------------|
| `LSIG`  | `JXS(6)`                      | `NXS(4)`               |
| `LSIGP` | `JXS(14)`                     | `NXS(6)`               |
| `LSIGH` | `XSS(``JXS(32)``+10*(i-1)+3)` | `XSS(``JXS(31)``+i-1)` |

`TYR` and `NMT` values for the [`TYR` Block](#sec:TYRBlock) and [`TYRH` Block](#sec:TYRHBlock).

The `MT`s are given in the [`MTR` Block](#sec:MTRBlock), the [`MTRP` Block](#sec:MTRPBlock) and [`MTRH` Block](#sec:MTRHBlock) respectively for the [`LSIG` Block](#sec:LSIGBlock), the [`LSIGP` Block](#sec:LSIGPBlock) and [`LSIGH` Block](#sec:LSIGHBlock) respectively. $\mathtt{LOCA}_{i}$ must be monotonically increasing. All locators (`LOCA`) are *relative* to `SIG`=`JXS(7)` for the [`LSIG` Block](#sec:LSIGBlock), *relative* to `SIGP`=`JXS(14)` for the [`LSIGP` Block](#sec:LSIGPBlock) and *relative* to `ANDH`=`XSS(``JXS(32)``+10*(i-1)+4)` for the [`LSIGH` Block](#sec:LSIGHBlock) for particle index $i$.

<a id="tab:LSIGBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LXS` | $\mathtt{LOCA}_{1}$ | Location of cross sections for reaction `MT`$_{1}$ |
| `LXS`+1 | $\mathtt{LOCA}_{2}$ | Location of cross sections for reaction `MT`$_{2}$ |
| … |  |  |
| `LXS`+`NMT`-1 | $\mathtt{LOCA}_{\texttt{NMT}}$ | Location of cross sections for reaction `MT`$_{\texttt{NMT}}$ |

`LSIG `<span class="nodecor">`&`</span>` LSIGP` Block.

<a id="sec:SIGBlock"></a>

### <span class="sans-serif">SIG</span> Block

The [`SIG` Block](#sec:SIGBlock) contains the incident neutron cross section data (photon production cross sections are given in the [`SIGP` Block](#sec:SIGPBlock) and particle production cross sections are given in [`SIGH` Block](#sec:SIGHBlock)). The format of the [`SIG` Block](#sec:SIGBlock) is given in Table [16](#tab:SIGBlock). The starting index `LXS` of the [`SIG` Block](#sec:SIGBlock) is given by `JXS(7)`. The cross section data for each reaction begins at an index defined by the corresponding relative locator from the [`LSIG` Block](#sec:LSIGBlock), which are given in Table [17](#tab:CrossSectionArray).

<a id="tab:SIGBlock"></a>

| Location in `XSS` | Description |
|:---|:---|
| `LXS`+$\mathtt{LOCA}_{1}$-1 | Cross section array for reaction `MT`$_{1}$ |
| `LXS`+$\mathtt{LOCA}_{2}$-1 | Cross section array for reaction `MT`$_{2}$ |
| … |  |
| `LXS`+$\mathtt{LOCA}_{\texttt{NMT}}$-1 | Cross section array for reaction `MT`$_{\texttt{NMT}}$ |

[`SIG` Block](#sec:SIGBlock).

  
The number of cross section arrays `NMT`=`NXS(4)`.

<a id="tab:CrossSectionArray"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LXS` + $\mathtt{LOCA}_{i}$-1 | $\texttt{IE}_{i}$ | Energy grid index for reaction `MT`$_{i}$ |
| `LXS` + $\mathtt{LOCA}_{i}$ | $N_{E,i}$ | Number of consecutive entries for `MT`$_{i}$ |
| `LXS` + $\mathtt{LOCA}_{i}$+1 | $\sigma_{i}[E(l)]$ for | Cross section for reaction `MT`$_{i}$ |
|  | $l=\texttt{IE}_{i},\ldots,\texttt{IE}_{i}+N_{E,i}-1$ |  |

Cross section array for the $i$-th reaction..

  
The energy grid, $E(l)$ is given in the [`ESZ` Block](#sec:ESZBlock).

The energy grid index $\texttt{IE}_{i}$ corresponds to the first energy in the grid at which a cross section is given. The `MT`$_{i}$s are defined in the [`MTR` Block](#sec:MTRBlock).

<a id="sec:LANDBlock"></a>

### <span class="sans-serif">LAND</span>, <span class="sans-serif">LANDP</span> and <span class="sans-serif">LANDH</span> Blocks

<a id="sec:LANDPBlock"></a><a id="sec:LANDHBlock"></a>

The [`LAND` Block](#sec:LANDBlock) (for incident neutron reactions), [`LANDP` Block](#sec:LANDPBlock) (for photon production reactions) and [`LANDH` Block](#sec:LANDHBlock) (for particle production reactions), give the locators for the angular distribution array for each reaction `MT`. A locator is a *relative* index in the `XSS` array where some piece of data can be found. In this case, the data are the angular distributions. The format of the [`LAND` Block](#sec:LANDBlock), [`LANDP` Block](#sec:LANDPBlock) and [`LANDH` Block](#sec:LANDHBlock) is given in Table [19](#tab:LANDBlock) and Table [20](#tab:LANDPBlock).

The starting index `LAND` depends on whether it is the [`LAND` Block](#sec:LANDBlock), [`LANDP` Block](#sec:LANDPBlock) or [`LANDH` Block](#sec:LANDHBlock) and is given in Table [18](#tab:LAND_NMT). For the particle production [`LANDH` Block](#sec:LANDHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:LAND_NMT"></a>

| Block   | `LAND`                        | `NMT`                  |
|:--------|:------------------------------|:-----------------------|
| `LAND`  | `JXS(8)`                      | `NXS(5)`               |
| `LANDP` | `JXS(16)`                     | `NXS(6)`               |
| `LANDH` | `XSS(``JXS(32)``+10*(i-1)+5)` | `XSS(``JXS(31)``+i-1)` |

`LAND` and `NMT` values for the [`TYR` Block](#sec:TYRBlock) and [`TYRH` Block](#sec:TYRHBlock).

The `MT`s are given in the [`MTR` Block](#sec:MTRBlock), the [`MTRP` Block](#sec:MTRPBlock) and [`MTRH` Block](#sec:MTRHBlock) respectively for the [`LAND` Block](#sec:LANDBlock), the [`LANDP` Block](#sec:LANDPBlock) and [`LANDH` Block](#sec:LANDHBlock) respectively. $\mathtt{LOCB}_{i}$ must be monotonically increasing. All locators (`LOCB`) are *relative* to `AND`=`JXS(9)` for the [`LAND` Block](#sec:LANDBlock), *relative* to `ANDP`=`JXS(17)` for the [`LANDP` Block](#sec:LANDPBlock) and *relative* to `ANDH`=`XSS(``JXS(32)``+10*(i-1)+6)` for the [`LANDH` Block](#sec:LANDHBlock) for particle index $i$.

<a id="tab:LANDBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LAND` | $\mathtt{LOCB}_{1}$ | Location of angular distributions for elastic scattering |
| `LAND`+1 | $\mathtt{LOCB}_{2}$ | Location of angular distributions for reaction `MT`$_{1}$ |
| … |  |  |
| `LAND`+`NMT` | $\mathtt{LOCB}_{\texttt{NMT}+1}$ | Location of angular distributions for reaction `MT`$_{\texttt{NMT}}$ |

`LAND` Block.

<a id="tab:LANDPBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LAND` | $\mathtt{LOCB}_{1}$ | Location of angular distributions for reaction `MT`$_{1}$ |
| `LAND`+1 | $\mathtt{LOCB}_{2}$ | Location of angular distributions for reaction `MT`$_{2}$ |
| … |  |  |
| `LAND`+`NMT`-1 | $\mathtt{LOCB}_{\texttt{NMT}}$ | Location of angular distributions for reaction `MT`$_{\texttt{NMT}}$ |

`LANDP `<span class="nodecor">`and`</span>` LANDH` Block.

<a id="sec:ANDBlock"></a>

### <span class="sans-serif">AND</span>, <span class="sans-serif">ANDP</span> and <span class="sans-serif">ANDH</span> Blocks

<a id="sec:ANDPBlock"></a><a id="sec:ANDHBlock"></a>

The [`AND` Block](#sec:ANDBlock), [`ANDP` Block](#sec:ANDPBlock) and [`ANDH` Block](#sec:ANDHBlock) contains angular distribution data for all reactions that produce secondary particles (neutrons for the [`AND` Block](#sec:ANDBlock), photons for the [`ANDP` Block](#sec:ANDPBlock) and a specific particle for the [`ANDH` Block](#sec:ANDHBlock)). The format of these blocks is given in Table [22](#tab:ANDBlock) and Table [23](#tab:ANDPBlock). The angular distribution data begins at the index specified by the locator `LOCB` from the [`LAND` Block](#sec:LANDBlock), [`LANDP` Block](#sec:LANDPBlock) or [`LANDH` Block](#sec:LANDHBlock). If $\mathtt{LOCB}_{i}$=0, no angular distribution data are given for reaction $i$ and isotropic scattering is assumed in either the lab or center-of-mass system. If $\mathtt{LOCB}_{i}$=-1 no angular distribution data is given for reaction $i$ (this can only happen for the the [`AND` Block](#sec:ANDBlock) or [`ANDH` Block](#sec:ANDHBlock)). In this case, the angular distribution data are specified through `law=44` in the [`DLW` Block](#sec:DLWBlock) or [`DLWH` Block](#sec:DLWHBlock).

The starting index `LAND` depends on whether it is the [`AND` Block](#sec:ANDBlock), [`ANDP` Block](#sec:ANDPBlock) or [`ANDH` Block](#sec:ANDHBlock) and are given in Table [21](#tab:AND_NMT). For the particle production [`LANDH` Block](#sec:LANDHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:AND_NMT"></a>

| Block  | `LAND`                        | `NMT`                  |
|:-------|:------------------------------|:-----------------------|
| `AND`  | `JXS(9)`                      | `NXS(5)`               |
| `ANDP` | `JXS(17)`                     | `NXS(6)`               |
| `ANDH` | `XSS(``JXS(32)``+10*(i-1)+6)` | `XSS(``JXS(31)``+i-1)` |

`LAND` and `NMT` values for the [`AND` Block](#sec:ANDBlock) and [`ANDH` Block](#sec:ANDHBlock).

<a id="tab:ANDBlock"></a>

| Location in `XSS` | Description |
|:---|:---|
| `LAND`+$\mathtt{LOCB}_{1}$-1 | Angular distribution array for elastic scattering |
| `LAND`+$\mathtt{LOCB}_{2}$-1 | Angular distribution array for reaction `MT`$_{1}$ |
| … |  |
| `LAND`+$\mathtt{LOCB}_{\texttt{NMT}+1}$-1 | Angular distribution array for reaction `MT`$_{\texttt{NMT}}$ |

[`AND` Block](#sec:ANDBlock).

  
The format for the angular distribution of the $i$-th array is given in Table [24](#tab:AngularDistributionArray).

<a id="tab:ANDPBlock"></a>

| Location in `XSS` | Description |
|:---|:---|
| `LAND`+$\mathtt{LOCB}_{1}$-1 | Angular distribution array for reaction `MT`$_{1}$ |
| … |  |
| `LAND`+$\mathtt{LOCB}_{\texttt{NMT}}$-1 | Angular distribution array for reaction `MT`$_{\texttt{NMT}}$ |

[`ANDP` Block](#sec:ANDPBlock) and [`ANDH` Block](#sec:ANDHBlock).

  
The format for the angular distribution of the $i$-th array is given in Table [24](#tab:AngularDistributionArray).

<a id="tab:AngularDistributionArray"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LAND`+$\mathtt{LOCB}_{i}$-1 | $N_{E}$ | Number of energies at which angular distributions are tabulated. |
| `LAND`+$\mathtt{LOCB}_{i}$ | $E(l),l=1,\ldots,N_{E}$ | Energy grid |
| … |  |  |
| `LAND`+$\mathtt{LOCB}_{i}$$+N_{E}$ | $L_{C}(l),l=1,\ldots,N_{E}$ | Location of tables associated with $E(l)$ |

Angular distribution array for the $i$-th reaction.

The angular distribution arrays (Table [24](#tab:AngularDistributionArray)) contains additional locators, $L_{C}$; the sign of these locators is a flag:

- if $\mathtt{LOCC}_{l}$=0, then distribution is isotropic and no further data is needed;

- if $\mathtt{LOCC}_{l}$\>0, then $\ensuremath{\mathtt{LOCC}_{l}}$ points to a 32 equiprobable bin distribution (see Table [25](#tab:32EquiprobableBinDistribution));

- if $\mathtt{LOCC}_{l}$\<0, then $\ensuremath{\mathtt{LOCC}_{l}}$ points to a tabulated angular distribution (see Table [26](#tab:TabulatedAngularDistribution)).

<a id="tab:32EquiprobableBinDistribution"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LAND`+\|$\mathtt{LOCC}_{l}$\|-1 | $P(1,K)$ | 32 equiprobable cosine bins for scattering |
|  | $K=1,\ldots,33$ | at energy $E(l)$. |

Format for the 32 equiprobable bin distribution.

$\dagger$  
<a id="tn:ANDInterpolationFlag"></a>

<a id="tab:TabulatedAngularDistribution"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LAND`+$|\ensuremath{\mathtt{LOCC}_{l}}|-1$ | `JJ` | Interpolation flag<sup>[note](#tn:ANDInterpolationFlag)</sup> |
| `LAND`+$|\ensuremath{\mathtt{LOCC}_{l}}|$ | $N_{P}$ | Number of points in the distribution |
| `LAND`+$|\ensuremath{\mathtt{LOCC}_{l}}|+1$ | $CS_{\mathrm{out}}(j),j=1,\ldots,N_{P}$ | Cosine scattering angular grid |
| `LAND`+$|\ensuremath{\mathtt{LOCC}_{l}}|+1+N_{P}$ | $\ensuremath{\mathrm{PDF}}(j),j=1,\ldots,N_{P}$ | Probability density function |
| `LAND`+$|\ensuremath{\mathtt{LOCC}_{l}}|+1+2N_{P}$ | $\ensuremath{\mathrm{CDF}}(j),j=1,\ldots,N_{P}$ | Cumulative density function |

Format for the tabulated angular distribution..

The [`AND` Block](#sec:ANDBlock) and [`ANDH` Block](#sec:ANDHBlock) can use both options (either a 32 equiprobable bin or tabulated distribution). The [`ANDP` Block](#sec:ANDPBlock) on the other hand can only use 32 equiprobable bin distributions.

<a id="sec:LDLWBlock"></a>

### <span class="sans-serif">LDLW</span>, <span class="sans-serif">LDLWP</span>, <span class="sans-serif">DNEDL and <span class="sans-serif">LDLWH</span></span> Blocks

<a id="sec:LDLWPBlock"></a><a id="sec:DNEDLBlock"></a><a id="sec:LDLWHBlock"></a>

The [`LDLW` Block](#sec:LDLWBlock), [`LDLWP` Block](#sec:LDLWPBlock) and [`LDLWH` Block](#sec:LDLWHBlock) give the locators for the energy distribution for every reaction that produces secondary neutron, secondary photons or other secondary particles (respectively). The [`DNEDL` Block](#sec:DNEDLBlock) on the other hand gives the locators for the delayed neutron energy distribution for each precursor group.

The format of the [`LDLW` Block](#sec:LDLWBlock) (for secondary neutrons), the [`LDLW` Block](#sec:LDLWBlock) (for secondary photons), the [`LDLWH` Block](#sec:LDLWHBlock) (for secondary particles) and the [`DNEDL` Block](#sec:DNEDLBlock) (for delayed neutrons) is given in Table [28](#tab:LDLWBlock). The format for the distributions is given in Section <a href="#sec:DLWBlock" data-reference-type="ref" data-reference="sec:DLWBlock">4.3.12</a>.

The starting index `LED` depends on whether it is the [`LDLW` Block](#sec:LDLWBlock), [`LDLWP` Block](#sec:LDLWPBlock), [`LDLWH` Block](#sec:LDLWHBlock) or [`DNEDL` Block](#sec:DNEDLBlock) and are given in Table [27](#tab:LED_NMT). For the particle production [`LDLWH` Block](#sec:LDLWHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`. These blocks are given only if the starting index, `LED`, is different from zero.

<a id="tab:LED_NMT"></a>

| Block   | `LED`                         | `NMT`                  |
|:--------|:------------------------------|:-----------------------|
| `LDLW`  | `JXS(10)`                     | `NXS(5)`               |
| `LDLWP` | `JXS(18)`                     | `NXS(6)`               |
| `LDLWH` | `XSS(``JXS(32)``+10*(i-1)+7)` | `XSS(``JXS(31)``+i-1)` |
| `DNEDL` | `JXS(26)`                     | `NXS(8)`               |

LED and NMT values for the [`LDLW` Block](#sec:LDLWBlock), the [`LDLWP` Block](#sec:LDLWPBlock), the [`LDLWH` Block](#sec:LDLWHBlock) and [`DNEDL` Block](#sec:DNEDLBlock).

<a id="tab:LDLWBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LED` | $\mathtt{LOCC}_{1}$ | Location of energy distribution data for reaction `MT`$_{1}$ or group 1 (if delayed neutron) |
| `LED`+1 | $\mathtt{LOCC}_{2}$ | Location of energy distribution data for reaction `MT`$_{2}$ or group 2 (if delayed neutron) |
| … |  |  |
| `LED`+`NMT`-1 | $\mathtt{LOCC}_{\texttt{NMT}}$ | Location of energy distribution data for reaction `MT`$_{\texttt{NMT}}$ or group `NMT` (if delayed neutron) |

`LDLW` Block.

  
The $\mathtt{LOCC}_{i}$ must be monotonically increasing.

The `MT`s are given in the [`MTR` Block](#sec:MTRBlock), the [`MTRP` Block](#sec:MTRPBlock) and [`MTRH` Block](#sec:MTRHBlock) respectively for the [`LDLW` Block](#sec:LDLWBlock), the [`LDLWP` Block](#sec:LDLWPBlock) and [`LDLWH` Block](#sec:LDLWHBlock) respectively. $\mathtt{LOCC}_{i}$ must be monotonically increasing. All locators (`LOCC`) are *relative* to `JED`=`JXS(19)` for the [`LDLW` Block](#sec:LDLWBlock), *relative* to `JED`=`JXS(19)` for the [`LDLWP` Block](#sec:LDLWPBlock) and *relative* to `JED`=`XSS(``JXS(32)``+10*(i-1)+8)` for the [`LDLWH` Block](#sec:LDLWHBlock) for particle index $i$.

<a id="sec:DLWBlock"></a>

### <span class="sans-serif">DLW</span>, <span class="sans-serif">DLWP</span>, <span class="sans-serif">DLWH</span> and <span class="sans-serif">DNED</span> Blocks

<a id="sec:DLWHBlock"></a><a id="sec:DLWPBlock"></a><a id="sec:DNEDBlock"></a>

The [`DLW` Block](#sec:DLWBlock) contains secondary neutron energy distributions for all reactions producing secondary neutrons (except for elastic scattering), the [`DLWP` Block](#sec:DLWPBlock) contains secondary photon energy distributions for all photon-producing reactions, the [`DLWH` Block](#sec:DLWHBlock) contains secondary particle energy distributions for all secondary particle producing reactions and the [`DNED` Block](#sec:DNEDBlock) contains the energy distributions for the delayed neutrons. The [`DLW` Block](#sec:DLWBlock), [`DLWP` Block](#sec:DLWPBlock), [`DLWH` Block](#sec:DLWHBlock) and [`DNED` Block](#sec:DNEDBlock) block have the same format (although there may be restrictions on which laws are allowed in these blocks). The energy distributions are given starting with a locator, `LOCC`, which were given in the [`LDLW` Block](#sec:LDLWBlock), [`LDLWP` Block](#sec:LDLWPBlock) or [`DNEDL` Block](#sec:DNEDLBlock). The locators are relative to the `JED` parameter. The value for `JED` and `NMT` (the number of reactions or the number of delayed precursor groups) is dependent on whether it is the [`DLW` Block](#sec:DLWBlock), [`DLWP` Block](#sec:DLWPBlock), [`DLWH` Block](#sec:DLWHBlock) or [`DNED` Block](#sec:DNEDBlock). These values are given in Table [29](#tab:JED_NMT). For the particle production [`DLWH` Block](#sec:DLWHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:JED_NMT"></a>

| Block  | `JED`                         | `NMT`                  |
|:-------|:------------------------------|:-----------------------|
| `DLW`  | `JXS(11)`                     | `NXS(5)`               |
| `DLWP` | `JXS(19)`                     | `NXS(6)`               |
| `DLWH` | `XSS(``JXS(32)``+10*(i-1)+8)` | `XSS(``JXS(31)``+i-1)` |
| `DNED` | `JXS(27)`                     | `NXS(8)`               |

`JED` and `NMT` for the [`DLW` Block](#sec:DLWBlock), [`DLWP` Block](#sec:DLWPBlock) and [`DLWH` Block](#sec:DLWHBlock).

<a id="tab:DLWBlock"></a>

| Location in `XSS` | Description |
|:---|:---|
| `JED`+$\mathtt{LOCC}_{1}$-1 | Energy distribution array for reaction `MT`$_{1}$ or group 1 (if delayed neutron) |
| `JED`+$\mathtt{LOCC}_{2}$-1 | Energy distribution array for reaction `MT`$_{2}$ or group 2 (if delayed neutron) |
| … |  |
| `JED`+$\mathtt{LOCC}_{\texttt{NMT}}$-1 | Energy distribution array for reaction `MT`$_{\texttt{NMT}}$ or group `NMT` (if delayed neutron) |

[`DLW` Block](#sec:DLWBlock).

The $i$-th array has the form shown in

$\dagger$  
<a id="tn:LNW"></a> If `LNW`$_{i}=0$ then `LAW`$_{1}$ is used regardless of other circumstances.

$\ddagger$  
<a id="tn:EnergyDistributionInterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ast$  
<a id="tn:EnergyDistributionProbability"></a> If the particle energy $E<E(1)$, then $P(E)=P(1)$. If $E>E(N_{E})$, then $P(E)=P(N_{E})$. If more than one law is given, then `LAW`$_{1}$ is used only if $\xi<P(E)$ where $\xi$ is a random number between 0 and 1.

<a id="tab:EnergyDistributionArray"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `JED`+$\mathtt{LOCC}_{i}$-1 | `LNW`$_{1}$ | Location of next law<sup>[note](#tn:LNW)</sup> relative to `JED` |
| `JED`+$\mathtt{LOCC}_{i}$ | `LAW`$_{1}$ | Name of this law |
| `JED`+$\mathtt{LOCC}_{i}$+1 | `IDAT`$_{1}$ | Location of data for this law relative to `JED` |
| `JED`+$\mathtt{LOCC}_{i}$+2 | $N_{R}$ | Number of interpolation regions to define law applicability regime |
| `JED`+$\mathtt{LOCC}_{i}$+3 | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `JED`+$\mathtt{LOCC}_{i}$+3+$N_{R}$ | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:EnergyDistributionInterpolationScheme)</sup> |
| `JED`+$\mathtt{LOCC}_{i}$+3+$2N_{R}$ | $N_{E}$ | Number of energies |
| `JED`+$\mathtt{LOCC}_{i}$+4+$2N_{R}$ | $E(l),l=1,\ldots,N_{E}$ | Tabulated energy points |
| `JED`+$\mathtt{LOCC}_{i}$+4+$2N_{R}+N_{E}$ | $P(l),l=1,\ldots,N_{E}$ | Probability of law validity<sup>[note](#tn:EnergyDistributionProbability)</sup> |
| `JED`+`IDAT`$_{1}-1$ | `LDAT`$(l),l,\ldots,L$ | Law data for `LAW`$_{1}$. |
| `JED`+`LNW`$_{1}-1$ | `LNW`$_{2}$ | Location of next law relative to `JED` |
| `JED`+`LNW`$_{1}$ | `LAW`$_{2}$ | Name of this law |
| `JED`+`LNW`+1 | `IDAT`$_{2}$ | Location of data for this law relative to `JED` |
| … |  |  |

Format for the secondary energy distribution..

The format for the law data depends on the law. The length, $L$, of the law data array, `LDAT`, is determined from parameters with `LDAT`. The various `LDAT` arrays and their formats are given in the following tables. Laws 2 (Table [33](#tab:LAW2)) and 4 (Table [35](#tab:LAW4)) are used to describe spectra of secondary photons from neutron collisions. All laws—except for Law 2—are used to describe the spectra of scattered neutrons.

In the following tables, we provide relative locations of data in the `LDAT` array rather than the absolute locations in the `XSS` array. Table [31](#tab:EnergyDistributionArray) defines the starting location of the `LDAT` array within the `XSS` array.

**TODO: add law=33 and other charged particle related laws, specify which laws are used for which type of outgoing particle**

<a id="sec:LAW1"></a>

#### `LAW`=1—Tabular Equiprobable Energy Bins

$\dagger$  
<a id="tn:LAW1InterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ddagger$  
<a id="tn:EoutTables"></a> $E_{\mathrm{out}}$ tables consist of `NET` boundaries of `NET`-1 equally likely energy intervals. Linear-linear interpolation is used between intervals.

<a id="tab:LAW1"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Number of interpolation regions between tables of $E_{\mathrm{out}}$ |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:LAW1InterpolationScheme)</sup> |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of incident energies tabulated |
| `LDAT`(3+$2N_{R}$) | $E_{\mathrm{in}}(l),l=1,\ldots,N_{E}$ | List of incident energies for which $E_{\mathrm{out}}$ is tabulated |
| `LDAT`(3+$2N_{R}+N_{E}$) | `NET` | Number of outgoing energies in each $E_{\mathrm{out}}$ table |
| `LDAT`(4+$2*N_{R}+N_{E}$) | $E_{\mathrm{out}_{1}}(l),l=1,\ldots,\texttt{NET}$ | $E_{\mathrm{out}}$ tables<sup>[note](#tn:EoutTables)</sup> |
|  | $E_{\mathrm{out}_{2}}(l),l=1,\ldots,\texttt{NET}$ |  |
|  | … |  |
|  | $E_{\mathrm{out}_{N_{E}}}(l),l=1,\ldots,\texttt{NET}$ |  |

`LAW`=1 (From ENDF Law 1).

<a id="sec:LAW2"></a>

#### `LAW`=2—Discrete Photon Energy

<a id="tab:LAW2"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | `LP` | Indicator of whether the photon is a primary or non-primary photon |
| `LDAT`(2) | `EG` | Photon energy or binding energy |

`LAW`=2—Discrete Photon Energy.

  
If `LP`=0 or `LP`=1, the photon energy is `EG`. If `LP`=2, the photon energy is $$\texttt{EG}+\left(\frac{\texttt{AWR}}{\texttt{AWR}+1}\right)E_{N}$$ where `AWR` is the atomic weight ratio and $E_{N}$ is the incident neutron energy.

<a id="sec:LAW3"></a>

#### `LAW`=3—Level Scattering

<a id="tab:LAW3"></a>

| Location  | Parameter | Description     |
|:----------|:----------|:----------------|
| `LDAT`(1) |           | $(A+1)/A|Q|$    |
| `LDAT`(2) |           | $(A/(A+1))^{2}$ |

`LAW`=3—Level Scattering.

The outgoing center-of-mass energy is calculated as: $$E_{\mathrm{out}}^{\mathrm{CM}} = \texttt{LDAT}(2)*(E-\texttt{LDAT}(1)),\tag{2}$$ where $$\begin{aligned}
E_{\mathrm{out}}^{\mathrm{CM}} &= \textnormal{outgoing center-of-mass\ energy} \\
  E &= \textnormal{incident energy} \\
  A &= \textnormal{atomic weight ratio} \\
  Q &= Q\textnormal{-value}
\end{aligned}$$

The outgoing neutron energy in the laboratory system is: <a id="eq:Law3EoutLAB"></a> $$E_{\mathrm{out}}^{\mathrm{LAB}} = E_{\mathrm{out}}^{\mathrm{CM}} +\left\{ E+2\mu_{\mathrm{CM}}(A+1)(E\cdot E_{\mathrm{out}}^{\mathrm{CM}})^{1/2} \right\}/(A+1)^{2}\tag{3}$$ where $\mu_{\mathrm{CM}}$ is the cosine of the center-of-mass scattering angle

<a id="sec:LAW4"></a>

#### `LAW`=4—Continuous Tabular Distribution

$\dagger$  
<a id="tn:LAW4InterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ddagger$  
<a id="tn:LAW4Locators"></a> Relative to `JXS(11)` (neutron reactions), `JXS(19)` (photon-producing reactions), or `JXS(27)` (delayed neutrons).

<a id="tab:LAW4"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | The number of interpolation regions |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:LAW4InterpolationScheme)</sup> |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of energies at which distributions are tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident neutron energies |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\texttt{L}(l),l=1,\ldots,N_{E}$ | Locations of distributions<sup>[note](#tn:LAW4Locators)</sup> |

`LAW`=4 (From ENDF-6 `LAW`=1).

The data associated with each incident neutron energy begins at the location $\texttt{L}(l)$. The format for the data is given in Table [36](#tab:LAW4Distribution), where for $E(1)$ let `K`=3+$2N_{R}+2N_{E}$. <a id="tab:LAW4Distribution"></a>

<table>
<caption>Secondary energy distribution for each incident energy in <code>LAW</code>=4..</caption>
<thead>
<tr>
<th style="text-align: left;">Location</th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>1</strong><strong>)</strong></span></strong></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>)</td>
<td style="text-align: left;"><span class="math inline"><code>INTT</code><sup>′</sup></span></td>
<td style="text-align: left;">Interpolation parameter</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+1)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Number of points in the distribution</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+2)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>out</sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Outgoing energy grid</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + <em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">PDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Probability Density Function</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 2<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">CDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Cumulative Density Function</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>2</strong><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>N</strong><sub><strong>E</strong></sub><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
</tbody>
</table>

<a id="par:INTT"></a>

#### Combined interpolation parameter.

The first element in the data is $\texttt{INTT}'$ or the interpolation parameter, which is a combination of two other parameters:

1.  the number of discrete photon lines, $N_{D}$, and

2.  the interpolation scheme for the subsequent data, `INTT`, which has two valid values:

    `INTT`=1  
    histogram distribution, and

    `INTT`=2  
    linear-linear distribution.

Given the definition of $N_{D}$ and `INTT`, the interpolation parameter, $\texttt{INTT}'$, is defined as the combination of $N_{D}$ and `INTT`: <a id="eq::INTT'"></a> $$\texttt{INTT}' = 10N_{D}+\texttt{INTT}.\tag{4}$$ Since $N_D$ describe the number of *discrete* photon lines, the remaining ($N_{p}-N_{D}$) values describe a continuous distribution. In this way, the distribution may be discrete, continuous, or a discrete distribution superimposed upon a continuous background.

<a id="sec:LAW5"></a>

#### `LAW`=5—General Evaporation Spectrum

<a id="tab:LAW5"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Interpolation scheme between $T$’s |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of incident energies tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident energy table |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\theta(l),l=1,\ldots,N_{E}$ | Effective temperature tabulated on incident energies |
| `LDAT`(3+$2N_{R}+2N_{E}$) | `NET` | Number of $X$’s tabulated |
| `LDAT`(4+$2N_{R}+2N_{E}$) | $X(l),l=1,\ldots,\texttt{NET}$ | Equiprobable bins |

`LAW`=5 (From ENDF-6, `MF`=5, `LF`=5).

<a id="eq:LAW5"></a>

$$E_{\mathrm{out}} = X(\xi)\theta(E)\tag{5}$$ where:

$X(\xi)$  
is a randomly sampled table of $X$’s;

$\theta(E)$  
is the effective temperature tabulated on incident energy; and

$E$  
is the incident energy.

<a id="sec:LAW7"></a>

#### `LAW`=7—Simple Maxwellian Fission Spectrum

<a id="tab:LAW7"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Interpolation scheme between $T$’s |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of incident energies tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident energy table |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\theta(l),l=1,\ldots,N_{E}$ | Effective temperature tabulated on incident energies |
| `LDAT`(3+$2N_{R}+2N_{E}$) | $U$ | Restriction energy |

`LAW`=7 (From ENDF-6, `MF`=5, `LF`=7).

The outgoing energy, $E_{\mathrm{out}}$, can be calculated as <a id="eq:LAW7f"></a> $$f(E\rightarrow E_{\mathrm{out}}) = \frac{\sqrt{E_{\mathrm{out}}}}{I}\ e^{-E_{\mathrm{out}}/\theta(E)}\tag{6}$$ where:

$I$  
is the normalization constant <a id="eq:LAW7I"></a> $$I = \theta^{{3/2}} \frac{\sqrt{\pi}}{2} \erf\left( \sqrt{(E-U)/\theta} \right) - \sqrt{(E-U)/\theta}\ e^{-(E-U)/\theta},\tag{7}$$

$\theta$  
is tabulated as a function of incident energy, $E$; and

$U$  
is a constant introduced to define the proper upper limit for the final particle energy such that $0\leq E_{\mathrm{out}} \leq (E-U)$.

<a id="sec:LAW9"></a>

#### `LAW`=9—Evaporation Spectrum

<a id="tab:LAW9"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Interpolation scheme between $T$’s |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of incident energies tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident energy table |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\theta(l),l=1,\ldots,N_{E}$ | Effective temperature tabulated on incident energies |
| `LDAT`(3+$2N_{R}+2N_{E}$) | $U$ | Restriction energy |

`LAW`=9 (From ENDF-6, `MF`=5, `LF`=9).

The outgoing energy, $E_{\mathrm{out}}$, can be calculated as <a id="eq:LAW9f"></a> $$f(E\rightarrow E_{\mathrm{out}}) = \frac{\sqrt{E_{\mathrm{out}}}}{I}\ e^{-E_{\mathrm{out}}/\theta(E)}\tag{8}$$ where:

$I$  
is the normalization constant <a id="eq:LAW9I"></a> $$I = \theta^{2}\left[ 1-e^{-(E-U)/\theta}\left( 1+\frac{E-U}{\theta} \right) \right],\tag{9}$$

$\theta$  
is tabulated as a function of incident energy, $E$; and

$U$  
is a constant introduced to define the proper upper limit for the final particle energy such that $0\leq E_{\mathrm{out}} \leq (E-U)$.

**Note:** Equation [8](#eq:LAW9f) is the same as Equation [6](#eq:LAW7f); just the definitions of $I$ in Equation [7](#eq:LAW7I) and Equation [9](#eq:LAW9I) are different.

<a id="sec:LAW11"></a>

#### `LAW`=11—Energy Dependent Watt Spectrum

<a id="tab:LAW11"></a>

<table>
<caption><code>LAW</code>=11 (From ENDF-6, <code>MF</code>=5, <code>LF</code>=11).</caption>
<thead>
<tr>
<th style="text-align: left;">Location</th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><code>LDAT</code>(1)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;">Interpolation scheme between <span class="math inline"><em>a</em></span>’s</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2)</td>
<td style="text-align: left;"><code>NBT</code><span class="math inline"><sub><em>a</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2+<span class="math inline"><em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span>)</td>
<td style="text-align: left;"><code>INT</code><span class="math inline"><sub><em>a</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>E</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;">Number of incident energies tabulated for <span class="math inline"><em>a</em>(<em>E</em><sub>in</sub>)</span> table</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(3+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>a</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub><em>a</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;">Incident energy table</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(3+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>a</em></sub></sub> + <em>N</em><sub><em>E</em><sub><em>a</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>a</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em><sub><em>a</em></sub></sub></span></td>
<td style="text-align: left;">Tabulated <span class="math inline"><em>a</em></span>’s</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">let <span class="math inline"><code>L</code> = 3 + 2(<em>N</em><sub><em>R</em><sub><em>a</em></sub></sub> + <em>N</em><sub><em>E</em><sub><em>a</em></sub></sub>)</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;">Interpolation scheme between <span class="math inline"><em>b</em></span>’s</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1)</td>
<td style="text-align: left;"><code>NBT</code><span class="math inline"><sub><em>b</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1+<span class="math inline"><em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span>)</td>
<td style="text-align: left;"><code>INT</code><span class="math inline"><sub><em>b</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>E</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;">Number of incident energies tabulated for <span class="math inline"><em>b</em>(<em>E</em><sub>in</sub>)</span> table</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+2+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>b</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub><em>b</em></sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;">Incident energy table</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+2+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>b</em></sub></sub> + <em>N</em><sub><em>E</em><sub><em>b</em></sub></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>b</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;">Tabulated <span class="math inline"><em>b</em></span>’s</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+2+<span class="math inline">2<em>N</em><sub><em>R</em><sub><em>b</em></sub></sub> + 2<em>N</em><sub><em>E</em><sub><em>b</em></sub></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>U</em></span></td>
<td style="text-align: left;">Rejection energy</td>
</tr>
</tbody>
</table>

The outgoing energy, $E_{\mathrm{out}}$, can be calculated as <a id="eq:LAW11f"></a> $$f(E\rightarrow E_{\mathrm{out}}) = \frac{e^{-E_{\mathrm{out}}/a}}{I} \sinh\left( \sqrt{bE_{\mathrm{out}}} \right)\tag{10}$$ where:

<div class="description">

is the normalization constant <a id="eq:LAW11I"></a> $$\begin{aligned}
I = \frac{1}{2}\sqrt{\frac{\pi a^{3}b}{4}}e^{(ab/4)} \left[ \erf\left( \sqrt{\frac{E-U}{a}} - \sqrt{\frac{ab}{4}} \right) + \erf\left( \sqrt{\frac{E-U}{a}} + \sqrt{\frac{ab}{4}} \right) \right] \\
      - a e^{-(E-U)/a} \sinh \sqrt{b(E-U)};
\end{aligned}\tag{11}$$

are tabulated energy-dependent parameters; and

is a constant introduced to define the proper upper limit for the final particle energy such that $0\leq E_{\mathrm{out}} \leq (E-U)$.

</div>

<a id="sec:LAW22"></a>

#### `LAW`=22—Tabular Linear Functions of Incident Energy Out

<a id="tab:LAW22"></a>

<table>
<caption><code>LAW</code>=22 (From UK Law 2).</caption>
<thead>
<tr>
<th style="text-align: left;">Location</th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><code>LDAT</code>(1)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;">Interpolation parameters</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2)</td>
<td style="text-align: left;"><code>NBT</code><span class="math inline">(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2+<span class="math inline"><em>N</em><sub><em>R</em></sub></span>)</td>
<td style="text-align: left;"><code>INT</code><span class="math inline">(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>R</em></sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(2+<span class="math inline">2<em>N</em><sub><em>R</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Number of incident energies tabulated</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(3+<span class="math inline">2<em>N</em><sub><em>R</em></sub>)</span></td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>in</sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Tabulated incident energies for <span class="math inline"><em>E</em><sub>out</sub></span> tables</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(3+<span class="math inline">2<em>N</em><sub><em>R</em></sub> + <em>N</em><sub><em>E</em></sub>)</span></td>
<td style="text-align: left;"><span class="math inline"><code>LOCE</code>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>E</em></sub></span></td>
<td style="text-align: left;">Locators of <span class="math inline"><em>E</em><sub>out</sub></span> tables</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Data for <span class="math inline"><em>E</em><sub>in</sub>(1)</span> Let <span class="math inline"><code>L</code> = 3 + 2<em>N</em><sub><em>R</em></sub> + 2<em>N</em><sub><em>E</em></sub></span>:</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>)</td>
<td style="text-align: left;"><span class="math inline"><code>NF</code><sub>1</sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1)</td>
<td style="text-align: left;"><span class="math inline"><em>P</em><sub>1<em>k</em></sub>, <em>k</em> = 1, …, <code>NF</code><sub>1</sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1+<code>NF</code><span class="math inline"><sub>1</sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>T</em><sub>1<em>k</em></sub>, <em>k</em> = 1, …, <code>NF</code><sub>1</sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>L</code>+1+2<code>NF</code><span class="math inline"><sub>1</sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>C</em><sub>1<em>k</em></sub>, <em>k</em> = 1, …, <code>NF</code><sub>1</sub></span></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Data for <span class="math inline"><em>E</em><sub>in</sub>(2)</span>:</td>
</tr>
<tr>
<td style="text-align: left;">…</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Tables of $P_{ik}, C_{ik}$, and $T_{ik}$ are given at a number of incident energies, $E_{\mathrm{in}}$. If $$E_{\mathrm{in}}(l) \leq E < E_{\mathrm{in}}(l+1)\tag{12}$$ then the secondary neutron energy is: <a id="eq:LAW22Eout"></a> $$E_{\mathrm{out}} = C_{ik}\left( E-T_{ik} \right),\tag{13}$$ where $k$ is chosen according to <a id="eq:LAW22Sum"></a> $$\sum_{j=1}^{k} P_{ij} < \xi \leq \sum_{k=1}^{k+1}P_{ij}\tag{14}$$ for a given random number, $\xi\in[0,1)$.

<a id="sec:LAW24"></a>

#### `LAW`=24—Tabular Energy Multipliers

<a id="tab:LAW24"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Interpolation scheme between $T$’s |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ |  |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of incident energies tabulated |
| `LDAT`(3+$2N_{R}$) | $E_{\mathrm{in}}(l),l=1,\ldots,N_{E}$ | List of incident energies for which $T$ is tabulated |
| `LDAT`(3+$2N_{R}+N_{E}$) | `NET` | Number of outgoing values in each table |
| `LDAT`(4+$2N_{R}+N_{E}$) | $T_{1}(l),l=1,\ldots,\texttt{NET}$ | Tables have `NET` boundaries with `NET`-1 equally likely intervals. Linear-linear interpolation is used between intervals. |
|  | $T_{2}(l),l=1,\ldots,\texttt{NET}$ |  |
|  | … |  |
|  | $T_{N_{E}}(l),l=1,\ldots,\texttt{NET}$ |  |

`LAW`=24 (From UK Law 6).

The outgoing energy, $E_{\mathrm{out}}$ can be calculated as: <a id="eq:LAW24"></a> $$E_{\mathrm{out}} = T_{k}(l)*E\tag{15}$$ where:

$T_{k}(l)$  
is sampled from the tables and

$E$  
is the incident energy.

<a id="sec:LAW44"></a>

#### `LAW`=44—Kalbach-87 Formalism

$\dagger$  
<a id="tn:LAW44InterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ddagger$  
<a id="tn:LAW44Locators"></a> Relative to `JXS(11)` (neutron reactions), `JXS(19)` (photon-producing reactions), or `JXS(27)` (delayed neutrons).

<a id="tab:LAW44"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Interpolation scheme between tables of $E_{\mathrm{out}}$ |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:LAW44InterpolationScheme)</sup> |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of energies at which distributions are tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident neutron energies |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\texttt{L}(l),l=1,\ldots,N_{E}$ | Locations of distributions<sup>[note](#tn:LAW44Locators)</sup> |

`LAW`=44 (From ENDF-6 `MF`=6 `LAW`=1, `LANG`=2).

The data associated with each incident neutron energy begins at the location $\texttt{L}(l)$. The format for the data is given in Table [44](#tab:LAW44Distribution), where for $E(1)$ let `K`=3+$2N_{R}+2N_{E}$. <a id="tab:LAW44Distribution"></a>

<table>
<caption>Secondary energy distribution for each incident energy in <code>LAW</code>=44.</caption>
<thead>
<tr>
<th style="text-align: left;">Location</th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>1</strong><strong>)</strong></span></strong></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>)</td>
<td style="text-align: left;"><span class="math inline"><code>INTT</code><sup>′</sup></span></td>
<td style="text-align: left;">Interpolation parameter</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+1)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Number of points in the distribution</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+2)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>out</sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Outgoing energy grid</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + <em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">PDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Probability Density Function</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 2<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">CDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Cumulative Density Function</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 3<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>R</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Precompound fraction <span class="math inline"><em>r</em></span></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 4<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>A</em>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Angular distribution slope value <span class="math inline"><em>a</em></span></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>2</strong><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>N</strong><sub><strong>E</strong></sub><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
</tbody>
</table>

The interpolation parameter, $\texttt{INTT}'$ has the same definition as in `LAW`=4, described in Paragraph <a href="#par:INTT" data-reference-type="ref" data-reference="par:INTT">4.3.12.5</a>.

The angular distributions for neutrons are sampled from: <a id="eq:LAW44p"></a> $$p(\mu,E_{\mathrm{in}},E_{\mathrm{out}}) = \frac{1}{2}\frac{a}{\sinh(a)}\left[ \cosh(a\mu)+r\sinh(a\mu) \right].\tag{16}$$

<a id="sec:LAW61"></a>

#### `LAW`=61—Like `LAW`=44, but tabular angular distribution instead of Kalbach-87

$\dagger$  
<a id="tn:LAW61InterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ddagger$  
<a id="tn:LAW61Locators"></a> Relative to `JXS(11)` (neutron reactions), `JXS(19)` (photon-producing reactions), or `JXS(27)` (delayed neutrons).

<a id="tab:LAW61"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Number of interpolation regions |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:LAW61InterpolationScheme)</sup> |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of energies at which distributions are tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident neutron energies |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\texttt{L}(l),l=1,\ldots,N_{E}$ | Locations of distributions<sup>[note](#tn:LAW61Locators)</sup> |

`LAW`=61.

The data associated with each incident neutron energy begins at the location $\texttt{L}(l)$. The format for the data is given in Table [46](#tab:LAW61Distribution), where for $E(1)$ let `K`=3+$2N_{R}+2N_{E}$. <a id="tab:LAW61Distribution"></a>

<table>
<caption>Secondary energy distribution for each incident energy in <code>LAW</code>=61.</caption>
<thead>
<tr>
<th style="text-align: left;">Location</th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>1</strong><strong>)</strong></span></strong></td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>)</td>
<td style="text-align: left;"><span class="math inline"><code>INTT</code><sup>′</sup></span></td>
<td style="text-align: left;">Interpolation parameter</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+1)</td>
<td style="text-align: left;"><span class="math inline"><em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Number of points in the distribution</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+2)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>out</sub>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Outgoing energy grid</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + <em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">PDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Probability Density Function</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 2<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">CDF(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Cumulative Density Function</td>
</tr>
<tr>
<td style="text-align: left;"><code>LDAT</code>(<code>K</code>+<span class="math inline">2 + 3<em>N</em><sub><em>p</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><code>LC</code>(<em>l</em>), <em>l</em> = 1, …, <em>N</em><sub><em>p</em></sub></span></td>
<td style="text-align: left;">Location of tables associated with incident energies <span class="math inline"><em>E</em>(<em>l</em>)</span>. See Table <a href="#tab:LAW61AngularDistribution">47</a></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>2</strong><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><span><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>N</strong><sub><strong>E</strong></sub><strong>)</strong></span></strong></span>—same format for <span class="math inline"><em>E</em>(1)</span></td>
</tr>
</tbody>
</table>

The interpolation parameter, $\texttt{INTT}'$ has the same definition as in `LAW`=4, described in Paragraph <a href="#par:INTT" data-reference-type="ref" data-reference="par:INTT">4.3.12.5</a>.

The $J$-th array for the tabular angular distribution has the form shown in Table [47](#tab:LAW61AngularDistribution). For the angular distribution, the locators `L` are relative to `JXS(11)` for neutron reactions or `JXS(19)` for photon-producing reactions. Thus, $$\begin{aligned}
\texttt{L} &= \texttt{JXS(11)} + |\texttt{LC}(J)|-1\ \text{(for neutron reactions)}, \\
  \texttt{L} &= \texttt{JXS(19)} + |\texttt{LC}(J)|-1\ \text{(for photon-producing reactions)}. \\
\end{aligned}$$ <a id="tab:LAW61AngularDistribution"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(`L`+1) | `JJ` | Interpolation flag |
| `LDAT`(`L`+2) | $N_{P}$ | Number of points in the distribution |
| `LDAT`(`L`+3) | $CS_{\mathrm{out}}(j),j=1,\ldots,N_{P}$ | Cosine scattering angular grid |
| `LDAT`(`L`+3+$N_{P}$) | $\ensuremath{\mathrm{PDF}}(j),j=1,\ldots,N_{P}$ | Probability density function |
| `LDAT`(`L`+3+$2N_{P}$) | $\ensuremath{\mathrm{CDF}}(j),j=1,\ldots,N_{P}$ | Cumulative density function |

Angular distribution for `LAW`=61.

Valid values for the interpolation flag, `JJ`, are the same as for `INTT`:

`JJ`=1  
histogram distribution, and

`JJ`=2  
linear-linear distribution.

<a id="sec:LAW66"></a>

#### `LAW`=66—$N$-body phase space distribution

$\dagger$  
<a id="tn:LAW66InterpolationScheme"></a>

`INTT`=1  
histogram distribution,

`INTT`=2  
linear-linear distribution.

<a id="tab:LAW66"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | `NPSX` | Number of bodies in the phase space |
| `LDAT`(2) | $A_{P}$ | Total mass ratio for the `NPSX` particles. |
| `LDAT`(3) | `INTT` | Interpolation parameter<sup>[note](#tn:LAW66InterpolationScheme)</sup> |
| `LDAT`(4) | $N_{P}$ | Number of points in the distribution |
| `LDAT`(5) | $\xi_{\mathrm{out}}(j),j=1,\ldots,N_{P}$ | $\xi$ grid (between 0 and 1) |
| `LDAT`(5+$N_{P}$) | $\ensuremath{\mathrm{PDF}}(j),j=1,\ldots,N_{P}$ | Probability density function |
| `LDAT`(5+$2N_{P}$) | $\ensuremath{\mathrm{CDF}}(j),j=1,\ldots,N_{P}$ | Cumulative density function |

`LAW`=66 (From ENDF-6 `MF`=6 `LAW`=6).

The outgoing energy is <a id="eq:LAW66"></a> $$\begin{aligned}
E_{\mathrm{out}} &= T(\xi)E_{i}^{\mathrm{max}} \\
  \\ \text{where} \\
  E_{i}^{\mathrm{max}} &= \frac{A_{p}-1}{A_{p}}\left( \frac{A}{A+1}E_{\mathrm{in}}+Q \right) \\
  \\ \text{and $T(\xi)$ is sampled from:} \\
  P_{i}(\mu,E_{\mathrm{in}},T) &= C_{n}\sqrt{T}\left( E_{i}^{\mathrm{max}}-T \right)^{3n/2-4}
\end{aligned}\tag{17}$$

While MCNP will only use the values for `NPSX` and $A_{P}$ (given in `LDAT`(1) and `LDAT`(2)), NJOY does add the derived probability density function and cumulative density function for $T(\xi)$ starting at `LDAT`(3).

<a id="sec:LAW67"></a>

#### `LAW`=67—Laboratory Angle-Energy Law

$\dagger$  
<a id="tn:LAW67InterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

$\ddagger$  
<a id="tn:LAW67Locators"></a> Relative to `JXS(11)` (neutron reactions), `JXS(19)` (photon-producing reactions), or `JXS(27)` (delayed neutrons).

<a id="tab:LAW67"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(1) | $N_{R}$ | Number of interpolation regions |
| `LDAT`(2) | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `LDAT`(2+$N_{R}$) | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:LAW67InterpolationScheme)</sup> |
| `LDAT`(2+$2N_{R}$) | $N_{E}$ | Number of energies at which distributions are tabulated |
| `LDAT`(3+$2N_{R}$) | $E(l),l=1,\ldots,N_{E}$ | Incident neutron energies |
| `LDAT`(3+$2N_{R}+N_{E}$) | $\texttt{L}(l),l=1,\ldots,N_{E}$ | Locations of distributions<sup>[note](#tn:LAW67Locators)</sup> |

`LAW`=67 (From ENDF-6 `MF`=6 `LAW`=7).

The data associated with each distribution begins at location $\texttt{L}(l)$. The format for the data is given in Table [50](#tab:LAW67AngularDistribution), where for $E(1)$ let $\texttt{K}=3+2N_{R}+2N_{e}$.

$\dagger$  
<a id="tn:LAW67AngularInterpolationScheme"></a>

`INTMU`=1  
histogram distribution,

`INTMU`=2  
linear-linear distribution.

<a id="tab:LAW67AngularDistribution"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`(`K`) | `INTMU` | Interpolation scheme<sup>[note](#tn:LAW67AngularInterpolationScheme)</sup> |
| `LDAT`(`K`+1) | `NMU` | Number of secondary cosines |
| `LDAT`(`K`+2) | $\texttt{XMU}(l),l=1,\ldots,\texttt{NMU}$ | Secondary cosines |
| `LDAT`(`K`+2+`NMU`) | $\texttt{LMU}(l),l=1,\ldots,\texttt{NMU}$ | Locations of data for each secondary cosine. See Table [51](#tab:LAW67EnergyDistribution) |

Angular distribution for `LAW`=67.

The format for the secondary energy distribution (for each cosine bin, `XMU`) is given in Table [51](#tab:LAW67EnergyDistribution). For the energy distribution, the locators, `LMU`, are relative to `JXS(11)` or `JXS(19)`. Thus, $$\begin{aligned}
\texttt{L}_{l} &= \texttt{JXS(11)}+\texttt{LMU}(l)\ \text{(for neutron reactions)}, \\
  \texttt{L}_{l} &= \texttt{JXS(19)}+\texttt{LMU}(l)\ \text{(for photon-producing reactions)}.
\end{aligned}$$

$\dagger$  
<a id="tn:LAW67EnergyInterpolationScheme"></a>

`INTEP`=1  
histogram distribution,

`INTEP`=2  
linear-linear distribution.

<a id="tab:LAW67EnergyDistribution"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `LDAT`($\texttt{L}_{l}$) | `INTEP` | Interpolation parameter between secondary energies<sup>[note](#tn:LAW67EnergyInterpolationScheme)</sup> |
| `LDAT`($\texttt{L}_{l}+1$) | `NPEP` | Number of secondary energies |
| `LDAT`($\texttt{L}_{l}+2$) | $E_{P}(l),l=1,\ldots,\texttt{NPEP}$ | Secondary energy grid |
| `LDAT`($\texttt{L}_{l}+2+\texttt{NPEP}$) | $\ensuremath{\mathrm{PDF}}(l),l=1,\ldots,\texttt{NPEP}$ | Probability density function |
| `LDAT`($\texttt{L}_{l}+2+2\texttt{NPEP}$) | $\ensuremath{\mathrm{CDF}}(l),l=1,\ldots,\texttt{NPEP}$ | Cumulative density function |

Secondary energy distribution for each cosine bin in `LAW`=67.

#### Energy-Dependent Neutron Yields

There are additional numbers to be found for neutrons in the [`DLW` Block](#sec:DLWBlock) and [`DLWP` Block](#sec:DLWPBlock). For those reactions with entries in the [`TYR` Block](#sec:TYRBlock) that are greater than 100 in absolute value, there must be neutron yields, $Y(E)$ provided as a function of neutron energy. The neutron yields are handled similarly to the average number of neutrons per fission, $\nu(E)$ that is given for the fission reactions. These yields are a part of the coupled energy-angle distributions given in File 6 of ENDF-6 data.

The $i$-th array has the form given in Table [52](#tab:EnergyDependentNeutronYields), where $\texttt{KY}=\texttt{JED}+|\texttt{TY}_{i}|-101$.

$\dagger$  
<a id="tn:EDNYInterpolationScheme"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is assumed.

<a id="tab:EnergyDependentNeutronYields"></a>

| Location | Parameter | Description |
|:---|:---|:---|
| `KY` | $N_{R}$ | Number of interpolation regions |
| `KY`+1 | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters |
| `KY`+1+$N_{R}$ | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme<sup>[note](#tn:EDNYInterpolationScheme)</sup> |
| `KY`+1+2$N_{R}$ | $N_{E}$ | Number of energies |
| `KY`+2+2$N_{R}$ | $E(l),l=1,\ldots,N_{E}$ | Tabular energy points |
| `KY`+2+$N_{R}+N_{E}$ | $Y(l),l=1,\ldots,N_{E}$ | Corresponding energy-dependent yields |

Energy-Dependent Neutron Yields.

<a id="sec:GPDBlock"></a>

### <span class="sans-serif">GPD</span> Block

The [`GPD` Block](#sec:GPDBlock) contains the *total* photon production cross section, tabulated on the energy grid given in the [`ESZ` Block](#sec:ESZBlock), the size of which is given by `NXS(3)`. The [`GPD` Block](#sec:GPDBlock) only exists if `JXS(12)`$\neq0$ and is shown in Table [53](#tab:GPDBlockTotal).

<a id="tab:GPDBlockTotal"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{GPD}}$ | $\sigma_{\gamma}(l),l=1,\ldots,\texttt{NES}$ | Total photon production cross section |

`GPD` Block.

In addition to the total photon production cross section, the outgoing photon energies *may* be given.[^4] There are 30 groups for the incident neutron energies, the boundaries of which are shown in Table [54](#tab:DiscreteNeutronEnergyBoundaries). <a id="tab:DiscreteNeutronEnergyBoundaries"></a>

|          |                |          |                |
|---------:|---------------:|---------:|---------------:|
| Group \# | Upper Boundary | Group \# | Upper Boundary |
|          |          (MeV) |          |          (MeV) |
|        1 |       1.39E-10 |       16 |           .184 |
|        2 |        1.52E-7 |       17 |           .303 |
|        3 |        4.14E-7 |       18 |           .500 |
|        4 |        1.13E-6 |       19 |           .823 |
|        5 |        3.06E-6 |       20 |          1.353 |
|        6 |        8.32E-6 |       21 |          1.738 |
|        7 |        2.26E-5 |       22 |          2.232 |
|        8 |        6.14E-5 |       23 |          2.865 |
|        9 |        1.67E-4 |       24 |           3.68 |
|       10 |        4.54E-4 |       25 |           6.07 |
|       11 |       1.235E-3 |       26 |           7.79 |
|       12 |        3.35E-3 |       27 |           10\. |
|       13 |        9.23E-3 |       28 |           12\. |
|       14 |        2.48E-2 |       29 |           13.5 |
|       15 |        6.76E-2 |       30 |           15\. |

Discrete neutron energy boundaries.

For each incident neutron energy group, the outgoing photon energies are discretized into 20 equiprobable energy groups, thus creating a $30\times20$ matrix. The outgoing energies are given in the [`GPD` Block](#sec:GPDBlock), after the total photon production cross section as shown in Table [55](#tab:GPDBlockOutgoing). Note that this matrix is only used for older tables that do not provide expanded photon production data. The format of this Block is given in Table [55](#tab:GPDBlockOutgoing). The `XSS` array index at the start of the [`GPD` Block](#sec:GPDBlock), $S_{\mathrm{GPD}}$=`JXS(12)`. <a id="tab:GPDBlockOutgoing"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{GPD}}$+`NES` | $E_{1}(K),K=1,20$ | 20 equiprobable outgoing photon energies for incident neutron $E<E_{N}(2)$ |
| $S_{\mathrm{GPD}}$+`NES`+20 | $E_{2}(K),K=1,20$ | 20 equiprobable outgoing photon energies for incident neutron $E_{N}(2) \leq E < E_{N}(3)$ |
| … |  |  |
| $S_{\mathrm{GPD}}$+`NES`+(i-1)\*20 | $E_{i}(K),K=1,20$ | 20 equiprobable outgoing photon energies for incident neutron $E_{N}(i) \leq E < E_{N}(i+1)$ |
| … |  |  |
| $S_{\mathrm{GPD}}$+`NES`+(30-1)\*20 | $E_{N}(K),K=1,20$ | 20 equiprobable outgoing photon energies for incident neutron $E \geq E_{N}(30)$ |

Outgoing photon energies in [`GPD` Block](#sec:GPDBlock)..

<a id="sec:SIGPBlock"></a>

### <span class="sans-serif">SIGP</span> and <span class="sans-serif">SIGH</span> Blocks

<a id="sec:SIGHBlock"></a>

The [`SIGP` Block](#sec:SIGPBlock) contains the photon production cross section data and the [`SIGH` Block](#sec:SIGHBlock) contains the particle production cross section data. The format of the [`SIGP` Block](#sec:SIGPBlock) and [`SIGH` Block](#sec:SIGHBlock) is given in Table [57](#tab:SIGPBlock). The starting index depends on whether it is the [`LSIGP` Block](#sec:LSIGPBlock) or [`LSIGH` Block](#sec:LSIGHBlock) and are given in Table [56](#tab:SIG_NMT). For the particle production [`SIGH` Block](#sec:SIGHBlock), `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`.

<a id="tab:SIG_NMT"></a>

| Block  | `SIG`                         | `NMT`                  |
|:-------|:------------------------------|:-----------------------|
| `SIGP` | `JXS(15)`                     | `NXS(6)`               |
| `SIGH` | `XSS(``JXS(32)``+10*(i-1)+4)` | `XSS(``JXS(31)``+i-1)` |

`SIG` and `NMT` values for the [`SIGP` Block](#sec:SIGPBlock) and [`SIGH` Block](#sec:SIGHBlock).

The cross section data begins at the index specified by the locator, $\mathtt{LOCA}_{i}$, given in the [`LSIGP` Block](#sec:LSIGPBlock) or [`LSIGH` Block](#sec:LSIGHBlock). The `MT`s are defined in the [`MTRP` Block](#sec:MTRPBlock) or [`MTRH` Block](#sec:MTRHBlock). All indices to the `XSS` array are *relative* to `SIG`.

<a id="tab:SIGPBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `SIG`+$\mathtt{LOCA}_{1}$-1 | `MFTYPE`$_{1}$ | Cross section array for reaction `MT`$_{1}$ |
| `SIG`+$\mathtt{LOCA}_{2}$-1 | `MFTYPE`$_{2}$ | Cross section array for reaction `MT`$_{2}$ |
| … |  |  |
| `SIG`+$\mathtt{LOCA}_{\texttt{NMT}}$-1 | `MFTYPE`$_{\texttt{NMT}}$ | Cross section array for reaction `MT`$_{\texttt{NMT}}$ |

`SIGP` Block.

The format of the $i$-th cross section array has two possible forms depending on the first number in the array, `MFTYPE`.

1.  If `MFTYPE`=12 or `MFTYPE`=16, yield data taken from ENDF File 12 or 6, respectively (see Table [58](#tab:PhotonProductionArray)). With this format, the photon or particle production cross section can be constructed using Equation [18](#eq:PhotonProductionConstruction): <a id="eq:PhotonProductionConstruction"></a> $$\sigma_{i}(E) = Y(E)*\sigma_{\texttt{MTMULT}}(E).\tag{18}$$

2.  If `MFTYPE`=13, photon production cross section data from ENDF File 13 (see Table [59](#tab:PhotonProductionCrossSectionArray)). This form is only allowed for the [`SIGP` Block](#sec:SIGPBlock).

$\dagger$  
<a id="tn:PPANBT"></a> If $N_{R}=0$, `NBT` and `INT` are omitted and linear-linear interpolation is used.

<a id="tab:PhotonProductionArray"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `JXS(15)`+$\mathtt{LOCA}_{i}$-1 | `MFTYPE` | 12 or 16 |
| `JXS(15)`+$\mathtt{LOCA}_{i}$ | `MTMULT` | Neutron `MT` whose cross section should multiply the yield |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+1 | $N_{R}$ | Number of interpolation regions |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+2 | `NBT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation parameters<sup>[note](#tn:PPANBT)</sup> |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+2 | `INT`$(l), l=1,\ldots,N_{R}$ | ENDF interpolation scheme |
| \+$N_{R}$ |  |  |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+2 | $N_{E}$ | Number of energies at which the yield is tabulated |
| \+$2*N_{R}$ |  |  |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+3 | $E(l),l=1,\ldots,N_{E}$ | Energies |
| \+$2*N_{R}$ |  |  |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+3 | $Y(l),l=1,\ldots,N_{E}$ | Yields |
| \+$2*N_{R}+N_{E}$ |  |  |

Photon production array if `MFTYPE`=12 or 16.

<a id="tab:PhotonProductionCrossSectionArray"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `JXS(15)`+$\mathtt{LOCA}_{i}$-1 | `MFTYPE` | 13 |
| `JXS(15)`+$\mathtt{LOCA}_{i}$ | `IE` | Energy grid index |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+1 | $N_{E}$ | Number of consecutive entries |
| `JXS(15)`+$\mathtt{LOCA}_{i}$+2 | $\sigma_{\gamma,i}[E(K)],$ | Photon production cross sections for reaction `MT`$_{i}$ |
|  | $K=\texttt{IE},\ldots,\texttt{IE}+N_{E}-1$ |  |

Photon production cross section array if `MFTYPE`=13.

  
The `MT`$_{i}$s are defined in the [`MTRP` Block](#sec:MTRPBlock).

<a id="sec:YPBlock"></a>

### <span class="sans-serif">YP</span> and <span class="sans-serif">YH</span> Blocks

<a id="sec:YHBlock"></a>

The [`YP` Block](#sec:YPBlock) and [`YH` Block](#sec:YHBlock) contains a list of `MT` identifiers of cross sections that are used as yield multipliers in Equation [18](#eq:PhotonProductionConstruction) to calculate the photon production cross sections (for the [`YP` Block](#sec:YPBlock)) and the secondary particle production cross sections (for the [`YH` Block](#sec:YHBlock)) and are referenced by the `MTMULT` parameter in Table [58](#tab:PhotonProductionArray). The format of the [`YP` Block](#sec:YPBlock) and [`YH` Block](#sec:YHBlock) is given in Table [60](#tab:YPBlock).

The starting index `LY` depends on whether it is the [`YP` Block](#sec:YPBlock) or [`YH` Block](#sec:YHBlock). For the [`YP` Block](#sec:YPBlock), `LY` = `NXS(6)`. For the particle production [`YH` Block](#sec:YHBlock), `JED` = `XSS(``JXS(32)``+10*(i-1)+8)` in which `i` refers to the index of the corresponding particle type defined on the [`PTYPE` Block](#sec:PTYPEBlock) and is between 1 and `NTYPE`. These blocks are given only if the starting index `LY` is different from zero.

<a id="tab:YPBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LY` | `NYP` | Number of `MT`s to follow |
| `LY`+1 | $\texttt{MTY}(l),l=1,\ldots,\texttt{NYP}$ | `MT`s. |

`YP` Block.

<a id="sec:FISBlock"></a>

### <span class="sans-serif">FIS</span> Block

The [`FIS` Block](#sec:FISBlock) contains the total fission cross section. The [`FIS` Block](#sec:FISBlock) exists if $\texttt{JXS(21)}\neq0$, but is generally not provided; the total fission cross section is redundant as the total fission cross section is the summation of first-, second-, third-, and fourth-chance fission (`MT`=19, 20, 21, and 38); <a id="eq:FissionSummation"></a> $$\sigma_{f,\mathrm{t}}(E) = \sigma_{(n,f)} + \sigma_{(n,nf)} + \sigma_{(n,2nf)} + \sigma_{(n,3nf)}.\tag{19}$$ The format of the [`FIS` Block](#sec:FISBlock) is given in Table [61](#tab:FISBlock). <a id="tab:FISBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `JXS(21)` | `IE` | Energy grid index |
| `JXS(21)`+1 | $N_{E}$ | Number of consecutive entries |
| `JXS(21)`+2 | $\sigma_{f}[E(l)],K=\texttt{IE},\ldots,\texttt{IE}+N_{E}-1$ | Total fission cross sections |

`FIS` Block.

  
The energy $E(l)$ is given in the [`ESZ` Block](#sec:ESZBlock).

<a id="sec:UNRBlock"></a>

### <span class="sans-serif">UNR</span> Block

The [`UNR` Block](#sec:UNRBlock) contains the unresolved resonance range probability tables. It exists if $\texttt{JXS(23)}\neq0$ and begins at location `JXS(23)` in `XSS`. The [`UNR` Block](#sec:UNRBlock) has several flags that have special meaning:

<div class="description">

The `ILF` flag is the inelastic competition flag.

$\texttt{ILF}<0$  
The inelastic cross section is zero within the entire unresolved energy range.

$\texttt{ILF}>0$  
The value of `ILF` is a special `MT` number whose tabulation is the sum of the inelastic levels.

$\texttt{ILF}=0$  
The sum of the contribution of the inelastic reactions will be made using a balance relationship involving the smooth cross sections.

An exception to this scheme is typically made when there is only one inelastic level within the unresolved energy range, because the flag can then just be set to its `MT` number and the special tabulation is not needed.

The `IOA` is the other absorption flag for determining the contribution of “other absorptions” (no neutron out or destruction reactions).

$\texttt{IOA}<0$  
The “other absorption” cross section is zero within the entire unresolved resonance range.

$\texttt{IOA}>0$  
The value of `IOA` is a special `MT` number whose tabulation is the sum of the “other absorption” reactions.

$\texttt{IOA}=0$  
The sum of the contribution of the “other absorption” reactions will be made using a balanced relationship involving the smooth cross sections.

An exception to this scheme is typically made when there is only one “other absorption” reaction within the unresolved energy range, because the flag can then just be set to its `MT` number and the special tabulation is not needed.

The `IFF` is the factors flag.

$\texttt{IFF}=0$  
The tabulations in the probability tables are cross sections.

$\texttt{IFF}=1$  
The tabulations in the probability tables are factors that must be multiplied by the corresponding “smooth” cross sections to obtain the actual cross sections.

</div>

The format of the [`UNR` Block](#sec:UNRBlock) is given in Table [63](#tab:UNRBlock). The $P(i,j,k)$ values, where

- $i=1,\ldots,N$,

- $j=1,\ldots,6$,

- $k=1,\ldots,M$,

are what make up the probability tables. The argument $j$ has special meaning depending on its value as shown in Table [62](#tab:Argumentj). <a id="tab:Argumentj"></a>

| $j$ | Description                       |
|:----|:----------------------------------|
| 1   | cumulative probability            |
| 2   | total cross section/factor        |
| 3   | elastic cross section/factor      |
| 4   | fission cross section/factor      |
| 5   | $(n,\gamma)$ cross section/factor |
| 6   | neutron heating number/factor     |

Possible values for the $j$ argument.

$\dagger$  
<a id="tn:UNRInterpolationFlag"></a>

<a id="tab:UNRBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `JXS(23)` | $N$ | Number of incident energies where there is a probability table. |
| `JXS(23)`+1 | $M$ | Length of probability table. |
| `JXS(23)`+2 | `INT` | Interpolation parameter between tables.<sup>[note](#tn:UNRInterpolationFlag)</sup> |
| `JXS(23)`+3 | `ILF` | Inelastic competition flag. |
| `JXS(23)`+4 | `IOA` | Other absorption flag. |
| `JXS(23)`+5 | `IFF` | Factors flag. |
| `JXS(23)`+6 | $E(i),i=1,\ldots,N$ | Incident energies. |
| `JXS(23)`+6+$N$ | $P(i,j,k)$ | Probability tables. |

`UNR` Block.

The ordering of the probability table entries, $P(i,j,k)$ is given in Table [64](#tab:PTableOrder), which begins at $\texttt{PTABLE}=\texttt{JXS(23)}+6+N$.

$\dagger$  
<a id="tn:CumulativeProbabilities"></a> The cumulative probabilities are monotonically increasing from an implied (but not included) lower value of zero to the upper value of $P(i,1,k=M)=1.0$.

<a id="tab:PTableOrder"></a>

<table>
<caption>Order of probability table elements <span class="math inline"><em>P</em>(<em>i</em>, <em>j</em>, <em>k</em>)</span>.</caption>
<thead>
<tr>
<th style="text-align: left;">Location in <code>XSS</code></th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for <span class="math inline"><strong>E</strong><strong>(</strong><strong>1</strong><strong>)</strong></span></strong></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code></td>
<td style="text-align: left;"><span class="math inline">CDF<sub>1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;">Cumulative probabilities<sup><a href="#tn:CumulativeProbabilities">note</a></sup> for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code>+<span class="math inline"><em>M</em></span></td>
<td style="text-align: left;"><span class="math inline"><em>σ</em><sub><em>t</em>, 1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;">Total cross section/factors for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code>+<span class="math inline">2<em>M</em></span></td>
<td style="text-align: left;"><span class="math inline"><em>σ</em><sub><em>s</em>, 1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;">Elastic cross section/factors for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code>+<span class="math inline">3<em>M</em></span></td>
<td style="text-align: left;"><span class="math inline"><em>σ</em><sub><em>f</em>, 1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;">Fission cross section/factors for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code>+<span class="math inline">4<em>M</em></span></td>
<td style="text-align: left;"><span class="math inline"><em>σ</em><sub>(<em>n</em>, <em>γ</em>), 1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;"><span class="math inline">(<em>n</em>, <em>γ</em>)</span> cross section/factors for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>PTABLE</code>+<span class="math inline">5<em>M</em></span></td>
<td style="text-align: left;"><span class="math inline"><em>H</em><sub>1</sub>(<em>l</em>), <em>l</em> = 1, …, <em>M</em></span></td>
<td style="text-align: left;">Heating number/factors for energy <span class="math inline"><em>i</em> = 1</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for incident energy 2—same format for <span class="math inline"><em>E</em>(1)</span></strong></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;">…</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><strong>Data for incident energy <span class="math inline"><em>N</em></span>—same format for <span class="math inline"><em>E</em>(1)</span></strong></td>
</tr>
</tbody>
</table>

<a id="sec:PTYPEBlock"></a>

### <span class="sans-serif">PTYPE</span> Block

The [`PTYPE` Block](#sec:PTYPEBlock) is the first of the particle production blocks used for neutron and charged particle production data. These particle production blocks are given only if the number of particles `NTYPE` = `NXS(7)` is different from zero. If the [`PTYPE` Block](#sec:PTYPEBlock) is present, the [`PTYPE` Block](#sec:PTYPEBlock) starts at the index `LTYPE` = `JXS(30)`.

**Question:** The particle type can be neutron, when is this actually used?

The [`PTYPE` Block](#sec:PTYPEBlock) gives a list of particle types for which particle production data is available. This includes cross section data (given in the [`SIGH` Block](#sec:SIGHBlock)), angular distribution data (given in the [`ANDH` Block](#sec:ANDHBlock)) and secondary particle energy distribution data (given in the [`DLWH` Block](#sec:DLWHBlock)).

The format of the [`PTYPE` Block](#sec:PTYPEBlock) is given in Table [65](#tab:PTYPEBlock).

<a id="tab:PTYPEBlock"></a>

| Location in `XSS` | Parameter             | Description          |
|:------------------|:----------------------|:---------------------|
| `LTYPE`           | `IP`$_{1}$            | First particle type  |
| `LTYPE`+1         | `IP`$_{2}$            | Second particle type |
| …                 |                       |                      |
| `LTYPE`+`NTYPE`-1 | `IP`$_{\texttt{NMT}}$ | Last particle type   |

`PTYPE` Block.

$\texttt{IP}_{1},\ldots,\texttt{IP}_{\texttt{NMT}}$ are particle identifiers given as follows:

- $\texttt{IP} = 1$ for neutrons

- $\texttt{IP} = 9$ for protons

- $\texttt{IP} = 31$ for deuterons

- $\texttt{IP} = 32$ for tritons

- $\texttt{IP} = 33$ for helions

- $\texttt{IP} = 34$ for aphas

<a id="sec:NTROBlock"></a>

### <span class="sans-serif">NTRO</span> Block

The [`NTRO` Block](#sec:NTROBlock) gives the number of reactions for each of the particle types defined in the [`PTYPE` Block](#sec:PTYPEBlock). If the [`NTRO` Block](#sec:NTROBlock) is present, the [`NTRO` Block](#sec:NTROBlock) starts at the index `LTYPE` = `JXS(31)`.

The format of the [`NTRO` Block](#sec:NTROBlock) is given in Table [66](#tab:NTROBlock).

<a id="tab:NTROBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LTYPE` | `NP`$_{1}$ | Number of reactions producing the first particle type |
| `LTYPE`+1 | `NP`$_{2}$ | Number of reactions producing the second particle type |
| … |  |  |
| `LTYPE`+`NTYPE`-1 | `NP`$_{\texttt{NMT}}$ | Number of reactions producing the last particle type |

`NTRO` Block.

<a id="sec:IXSBlock"></a>

### <span class="sans-serif">IXS</span> Block

The [`IXS` Block](#sec:IXSBlock) gives 10 particle production locators for each of the particle types defined in the [`PTYPE` Block](#sec:PTYPEBlock). If the [`IXS` Block](#sec:IXSBlock) is present, the [`IXS` Block](#sec:IXSBlock) starts at the index `NEXT` = `JXS(32)`. The [`IXS` Block](#sec:IXSBlock) serves a similar function as the [JXS Array](#sec:JXSContinuousEnergyNeutron), in that it provides the locators to specific blocks of data, as laid out in Table [67](#tab:IXSBlock).

<a id="tab:IXSBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `LTYPE` | `HPD` | Location of the total particle production and heating data |
| `LTYPE`+1 | `MTRH` | Location of the particle production MT array |
| `LTYPE`+2 | `TYRH` | Location of the particle production TYR data |
| `LTYPE`+3 | `LSIGH` | Location of the particle production cross section locators |
| `LTYPE`+4 | `SIGH` | Location of the particle production cross sections |
| `LTYPE`+5 | `LANDH` | Location of the particle production angular distribution locators |
| `LTYPE`+6 | `ANDH` | Location of the particle production angular distributions |
| `LTYPE`+7 | `LDLWH` | Location of the particle production energy distribution locators |
| `LTYPE`+8 | `DLWH` | Location of the particle production energy distributions |
| `LTYPE`+9 | `YH` | Location of the particle production yield multipliers |

`IXS array for particle type `$j$`, with `$\texttt{LTYPE}=\texttt{NEXT}+10\texttt{NTYPE}(j-1)$ Block.

With the exception of the [`HPD` Block](#sec:HPDBlock), all other locators point to blocks similar to the ones already defined for neutrons and photons.

<a id="sec:HPDBlock"></a>

### <span class="sans-serif">HPD</span> Block

The [`HPD` Block](#sec:HPDBlock) gives the total particle production cross section and the associated heating number for a given particle. If the particle production data is given (i.e. the $\texttt{NTYPE}\ne0$, and the [`PTYPE` Block](#sec:PTYPEBlock), the [`NTRO` Block](#sec:NTROBlock) and [`IXS` Block](#sec:IXSBlock) are given), the [`HPD` Block](#sec:HPDBlock) is present. The [`HPD` Block](#sec:HPDBlock) starts at the location index $\texttt{HPD}=\texttt{XSS(()}\texttt{NEXT}+10*(j-1))$.

<a id="tab:HPDBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| `HPD` | `IE` | Energy grid index |
| `HPD`+1 | $N_{E}$ | Number of consecutive energies |
| `HPD`+2 | $\sigma[E(K)],$ | Total particle production cross section |
| `HPD`+2+`NE` | $E(l),l=1,\ldots,N_{E}$ | Average heating numbers |

`HPD` Block.

<a id="sec:Dosimetry"></a>

# Neutron Dosimetry

<a id="sec:NXSDosimetry"></a>

## `NXS` Array

<a id="tab:NXSDosimetry"></a>

| Element | Name | Description                                  |
|--------:|:-----|:---------------------------------------------|
|       1 | —    | Length of second block of data (`XSS` array) |
|       2 | ZA   | $1000*Z+A$                                   |
|       3 | —    |                                              |
|       4 | NTR  | Number of reactions                          |
|         | …    |                                              |
|      16 | —    |                                              |

`NXS` array element definitions for neutron dosimetry ACE Table.

<a id="sec:JXSDosimetry"></a>

## `JXS` Array

<a id="tab:JXSDosimetry"></a>

| Element | Name | Location Description            |
|--------:|:-----|:--------------------------------|
|       1 | LONE | First word of table             |
|       2 | —    |                                 |
|       3 | MTR  | `MT` array                      |
|         | …    |                                 |
|       6 | LSIG | Table of cross section locators |
|       7 | SIGD | Cross sections                  |
|         | …    |                                 |
|      22 | END  | Last word of this table         |
|         | …    |                                 |
|      32 | —    |                                 |

`JXS` array element definitions for neutron dosimetry ACE Table.

<a id="sec:ThermalScattering"></a>

# Thermal Scattering $S(\alpha, \beta)$

Data from thermal $S(\alpha, \beta)$ tables provide a complete representation of thermal neutron scattering by molecules and crystalline solids. Cross sections for (coherent and incoherent) elastic and (incoherent) inelastic scattering are found on the tables. A coupled energy/angle representation is used to describe the spectra of inelastically scattered neutrons. Angular distributions for elastic scattering are also provided.

Four unique types of data blocks are associated with $S(\alpha, \beta)$ tables. We now briefly describe each of these four data block types and reference the sections in which their formats are detailed.

1.  **[`ITIE` Block](#sec:ITIEBlock)** — contains the energy-dependent incoherent inelastic scattering cross sections. The [`ITIE` Block](#sec:ITIEBlock) always exists. See Section <a href="#sec:ITIEBlock" data-reference-type="ref" data-reference="sec:ITIEBlock">6.3.1</a>.

2.  **[`ITCE` Block](#sec:ITCEBlock)** and **[`ITCEI` Block](#sec:ITCEIBlock)** — contains the energy-dependent elastic scattering cross sections. The [`ITCE` Block](#sec:ITCEBlock) exists if the material has coherent and/or incoherent elastic scattering (`NXS(5)`$\neq0$ and `JXS(4)`$\neq0$). The [`ITCEI` Block](#sec:ITCEIBlock) only exists for mixed mode elastic scattering (`NXS(5)`$=5$ and `JXS(7)`$\neq0$). See Section <a href="#sec:ITCEBlock" data-reference-type="ref" data-reference="sec:ITCEBlock">6.3.3</a>.

3.  **[`ITXE` Block](#sec:ITXEBlock)** — contains coupled energy/angle distributions for incoherent inelastic scattering. The [`ITXE` Block](#sec:ITXEBlock) always exists. See Section <a href="#sec:ITXEBlock" data-reference-type="ref" data-reference="sec:ITXEBlock">6.3.2</a>.

4.  **[`ITCA` Block](#sec:ITCABlock)** and **[`ITCAI` Block](#sec:ITCAIBlock)** — contains angular distributions for elastic scattering. The [`ITCA` Block](#sec:ITCABlock) exists if the material has coherent and/or incoherent elastic scattering (`NXS(5)`$\neq0$, `JXS(6)`$\neq0$ and `NXS(6)`$\neq-1$). The [`ITCEI` Block](#sec:ITCEIBlock) only exists for mixed mode elastic scattering (`NXS(5)`$=5$, `JXS(9)`$\neq0$ and `NXS(6)`$\neq-1$). See Section <a href="#sec:ITCABlock" data-reference-type="ref" data-reference="sec:ITCABlock">6.3.4</a>.

<a id="sec:NXSThermalScattering"></a>

## `NXS` Array

<a id="tab:NXSThermalScattering"></a>

| Element | Name | Description |
|---:|:---|:---|
| 1 | — | Length of second block of data (`XSS` array) |
| 2 | `IDPNI` | Inelastic scattering mode |
| 3 | `NIL` | Inelastic dimensioning parameter |
| 4 | `NIEB` | Number of inelastic exiting energies |
| 5 | `IDPNC` | Elastic scattering mode (no elastic data=0, incoherent=3, coherent=4, mixed=5) |
| 6 | `NCL` | Elastic dimensioning parameter for the first elastic block |
| 7 | `IFENG` | Secondary energy mode (discrete=0, skewed=1, continuous=2) |
| 8 | `NCLI` | Elastic dimensioning parameter for the second elastic block |
|  | … |  |
| 16 | — |  |

`NXS` array element definitions for thermal scattering ACE Table.

<a id="sec:JXSThermalScattering"></a>

## `JXS` Array

<a id="tab:JXSThermalScattering"></a>

| Element | Name | Location Description |
|---:|:---|:---|
| 1 | `ITIE` | Inelastic energy table |
| 2 | `ITIX` | Inelastic cross sections |
| 3 | `ITXE` | Inelastic energy/angle distributions |
| 4 | `ITCE` | Elastic energy table (used for coherent elastic scattering if |
|  |  | `NXS(5)`=4 or 5, and used for incoherent elastic scattering if `NXS(5)`=3) |
| 5 | `ITCX` | Elastic cross sections (used for coherent elastic scattering if |
|  |  | `NXS(5)`=4 or 5, and used for incoherent elastic scattering if `NXS(5)`=3) |
| 6 | `ITCA` | Elastic angular distributions (used for coherent elastic scattering |
|  |  | if `NXS(5)`=4 or 5, and used for incoherent elastic scattering if `NXS(5)`=3) |
| 7 | `ITCEI` | Elastic energy table (used for incoherent elastic scattering if `NXS(5)`=5) |
| 8 | `ITCXI` | Elastic cross sections (used for incoherent elastic scattering if `NXS(5)`=5) |
| 9 | `ITCAI` | Elastic angular distributions (used for incoherent elastic scattering if `NXS(5)`=5) |
|  | … |  |
| 32 | — |  |

`JXS` array element definitions for thermal scattering ACE Table.

When a single mode of elastic scattering is used (either coherent when `NXS(5)`$=4$ or incoherent when `NXS(5)`$=3$), then only the first elastic block will be used. This is the way data was stored in the ACE format prior to the introduction of mixed mode elastic scattering in thermal scattering evaluations that combines both coherent and incoherent elastic scattering.

When using mixed mode elastic scattering (both coherent and incoherent elastic scattering are given, $\texttt{NXS(5)}=5$), the JXS array will contain an additional set of indices for a second elastic data block. In mixed mode, the first elastic blocks (pointed to by `JXS(4)` to `JXS(6)`) are used for the coherent part and the second elastic blocks (pointed to by `JXS(7)` to `JXS(9))` are used for the incoherent part.

## Format of Individual Data Blocks

<a id="sec:ITIEBlock"></a>

### <span class="sans-serif">ITIE</span> Block

The format of the [`ITIE` Block](#sec:ITIEBlock) is given in Table [73](#tab:ITIEBlock). The index at the start of the block is $S_{\mathrm{ITIE}}$=`JXS(1)`. Note that `JXS(2)`=`JXS(1)`+1+$N_{in}$. Linear-linear interpolation is assumed between adjacent energies.

<a id="tab:ITIEBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{ITIE}}$ | $N_{in}$ | Number of inelastic energies |
| $S_{\mathrm{ITIE}}$+1 | $E_{in}(l),l=1,\ldots,N_{in}$ | Energies |
| $S_{\mathrm{ITIE}}$+1+$N_{in}$ | $\sigma_{in}(l),l=1,\ldots,N_{in}$ | Inelastic cross sections |

`ITIE` Block.

<a id="sec:ITXEBlock"></a>

### <span class="sans-serif">ITXE</span> Block

The format of the coupled energy/angle distribution for incoherent inelastic scattering is governed by the value of `NXS(7)`. There are three possibilities:

$\texttt{NXS(7)}=0$  
equally-likely discrete cosines and energies (Table [74](#tab:ITXEBlock))

$\texttt{NXS(7)}=1$  
skewed distribution of discrete cosines and energies (Table [74](#tab:ITXEBlock))

$\texttt{NXS(7)}=2$  
continuous distribution of outgoing energies and equally-likely discrete cosines (Table [75](#tab:ITXEBlockContinuousHeader) and Table [76](#tab:ITXEBlockContinuousData))

The format of the [`ITXE` Block](#sec:ITXEBlock) for $\texttt{NXS(7)}<2$ is given in Table [74](#tab:ITXEBlock). The index at the start of the block is $S_{\mathrm{ITXE}}$=`JXS(3)`. For each incident energy from the [`ITIE` Block](#sec:ITIEBlock), $N'=$`NXS(4)` discrete outgoing energies are given. For each pair of incident and outgoing energies, $N_\mu=$`NXS(3)`+1 discrete cosines are given. The incident inelastic energy grid $E_{in}(l)$ is given in the [`ITIE` Block](#sec:ITIEBlock), and linear-linear interpolation is assumed between adjacent values of $E_{in}$.

$\dagger$  
<a id="tn:nieb"></a> The number of outgoing energies `NIEB` is determined as `NXS(4)`.

<a id="tab:ITXEBlock"></a>

<table>
<caption><a href="#sec:ITXEBlock"><code>ITXE</code> Block</a> for <span class="math inline"><code>NXS(7)</code> &lt; 2</span>.</caption>
<thead>
<tr>
<th style="text-align: left;">Location in <code>XSS</code></th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">First of <code>NIEB</code><sup><a href="#tn:nieb">note</a></sup> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span>+1</td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → 1), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span>+1+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Second of <code>NIEB</code> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span>+2+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → 2), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: center;">⋮</td>
<td style="text-align: center;">⋮</td>
<td style="text-align: center;">⋮</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span>+(<span class="math inline"><em>N</em><sup>′</sup></span>-1)(1+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup></sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Last of <code>NIEB</code> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline"><em>S</em><sub>ITXE</sub></span>+(<span class="math inline"><em>N</em><sup>′</sup></span>-1)(1+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)+1</td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → <em>N</em><sup>′</sup>), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup></sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">(Repeat for all remaining values of <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub></span>)</td>
</tr>
</tbody>
</table>

When $\texttt{NXS(7)}=0$, each of the `NXS(4)` discrete outgoing energies for a given incident energy are equally probable. When $\texttt{NXS(7)}=1$, the selection of the discrete outgoing energies is skewed such that the first two and last two outgoing energies have a lower probability of being selected than all other outgoing energies. The first and last energies have a relative probability of 1, the second and second-to-last energies have a relative probability of 4, and all other energies have a relative probability of 10.

Because the use of discrete outgoing energies and cosines can result in unphysical spikes in the neutron flux spectrum at thermal energies, some Monte Carlo codes attempt to “smear” the outgoing energies and cosines to produce a smoother distribution (that more closely approximates a continuous distribution with $\texttt{NXS(7)}=2$).

When $\texttt{NXS(7)}=2$, the distribution of outgoing energies for each incident energy is continuous in energy and specified by a probability density function and cumulative distribution function. The format of the [`ITXE` Block](#sec:ITXEBlock) in this case is given in Table [75](#tab:ITXEBlockContinuousHeader) and Table [76](#tab:ITXEBlockContinuousData). As before, the index at the start of the block is $S_{\mathrm{ITXE}}$=`JXS(3)`. Unlike in the $\texttt{NXS(7)} < 2$ cases, the number of outgoing energies for each incident energy is allowed to vary. The number of discrete cosines, $N_\mu=$`NXS(3)`-1, remains the same for each pair of incident and outgoing energies, however.

$\dagger$  
<a id="tn:nin"></a> The number of incoming energies $N_{in}$ for incoherent inelastic scattering is given in the [`ITIE` Block](#sec:ITIEBlock).

<a id="tab:ITXEBlockContinuousHeader"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{ITXE}}$ | `L`$(l),l=1,\ldots,N_{in}$<sup>[note](#tn:nin)</sup> | Location in `XSS` of distribution for incident energy $l$ |
| $S_{\mathrm{ITXE}}$+$N_{in}$ | $N'(l),l=1,\ldots,N_{in}$ | Number of outgoing energies for incident energy $l$ |

[`ITXE` Block](#sec:ITXEBlock) for $\texttt{NXS(7)}=2$.

<a id="tab:ITXEBlockContinuousData"></a>

<table>
<caption><a href="#sec:ITXEBlock"><code>ITXE</code> Block</a> for <span class="math inline"><code>NXS(7)</code> = 2</span> (continued).</caption>
<thead>
<tr>
<th style="text-align: left;">Location in <code>XSS</code></th>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><code>L</code>(1)+1</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">First of <code>NIEB</code><sup><a href="#tn:nieb">note</a></sup> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+2</td>
<td style="text-align: left;"><span class="math inline">PDF<sub>1</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Probability density function value for <span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+3</td>
<td style="text-align: left;"><span class="math inline">CDF<sub>1</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Cumulative distribution function value for <span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+4</td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → 1), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub>1</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+4+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Second of <code>NIEB</code> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+5+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline">PDF<sub>2</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Probability density function value for <span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+6+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline">CDF<sub>2</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Cumulative distribution function value for <span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+7+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → 2), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub>2</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: center;">⋮</td>
<td style="text-align: center;">⋮</td>
<td style="text-align: center;">⋮</td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+1+(<span class="math inline"><em>N</em><sup>′</sup>(1)</span>-1)(3+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup>(1)</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Last of <span class="math inline"><em>N</em><sup>′</sup>(1)</span> outgoing energies for inelastic scattering at <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+2+(<span class="math inline"><em>N</em><sup>′</sup>(1)</span>-1)(3+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">PDF<sub><em>N</em><sup>′</sup>(1)</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Probability density function value for <span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup>(1)</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+3+(<span class="math inline"><em>N</em><sup>′</sup>(1)</span>-1)(3+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline">CDF<sub><em>N</em><sup>′</sup>(1)</sub>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
<td style="text-align: left;">Cumulative distribution function value for <span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup>(1)</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td style="text-align: left;"><code>L</code>(1)+4+(<span class="math inline"><em>N</em><sup>′</sup>(1)</span>-1)(3+<span class="math inline"><em>N</em><sub><em>μ</em></sub></span>)</td>
<td style="text-align: left;"><span class="math inline"><em>μ</em><sub><em>l</em></sub>(1 → <em>N</em><sup>′</sup>(1)), <em>l</em> = 1, …, <em>N</em><sub><em>μ</em></sub></span></td>
<td style="text-align: left;">Discrete cosines for scattering from <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub>(1)</span> to <span class="math inline"><em>E</em><sub><em>N</em><sup>′</sup>(1)</sub><sup><em>o</em><em>u</em><em>t</em></sup>[<em>E</em><sub><em>i</em><em>n</em></sub>(1)]</span></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">(Repeat for all remaining values of <span class="math inline"><em>E</em><sub><em>i</em><em>n</em></sub></span>)</td>
</tr>
</tbody>
</table>

<a id="sec:ITCEBlock"></a>

### <span class="sans-serif">ITCE</span> Block

<a id="sec:ITCEIBlock"></a>

The format of the [`ITCE` Block](#sec:ITCEBlock) and [`ITCEI` Block](#sec:ITCEIBlock) is given in Table [77](#tab:ITCEBlock). The index at the start of the [`ITCE` Block](#sec:ITCEBlock) and [`ITCEI` Block](#sec:ITCEIBlock) is respectively $S_{\mathrm{ITCE}}$=`JXS(4)` and $S_{\mathrm{ITCE}}$=`JXS(7)`.

<a id="tab:ITCEBlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{ITCE}}$ | $N_{el}$ | Number of elastic energies |
| $S_{\mathrm{ITCE}}$+1 | $E_{el}(l),l=1,\ldots,N_{el}$ | Energies |
| $S_{\mathrm{ITCE}}$+1+$N_{el}$ | $P(l),l=1,\ldots,N_{el}$ | (See below) |

`ITCE` Block.

For incoherent elastic scattering (stored in [`ITCE` Block](#sec:ITCEBlock) if $\texttt{NXS(5)}=4$ and stored in [`ITCEI` Block](#sec:ITCEIBlock) if $\texttt{NXS(5)}=5$), $$P(l) = \sigma_{el}(E_{el}(l))\tag{20}$$ with linear-linear interpolation between points. For coherent elastic scattering (stored in [`ITCE` Block](#sec:ITCEBlock) if `NXS(5)`$=4 \text{or} 5$), <a id="eq:CoherentP"></a> $$P(l) = E\cdot\sigma_{el}(E), \qquad E_{el}(l) \le E < E_{el}(l+1).\tag{21}$$ In this case, the energies $E_{el}(l)$ correspond to Bragg edges, and between two energies the cross section is determined by inverting Equation [21](#eq:CoherentP): $$\sigma_{el}(l) = \frac{P(l)}{E}, \qquad E_{el}(l) \le E < E_{el}(l+1).\tag{22}$$ Also note that $\sigma_{el}(E)=0$ below $E_{el}(1)$. However, above $E_{el}(N_{el})$, $\sigma_{el}(E) = P(N_{el})/E$.

<a id="sec:ITCABlock"></a>

### <span class="sans-serif">ITCA</span> Block

<a id="sec:ITCAIBlock"></a>

The format of the [`ITCA` Block](#sec:ITCABlock) and [`ITCAI` Block](#sec:ITCAIBlock) is given in Table [78](#tab:ITCABlock). The index at the start of the [`ITCA` Block](#sec:ITCABlock) and [`ITCAI` Block](#sec:ITCAIBlock) is respectively $S_{\mathrm{ITCA}}$=`JXS(6)` and $S_{\mathrm{ITCA}}$=`JXS(9)`. For each incident energy from the [`ITCE` Block](#sec:ITCEBlock) and [`ITCEI` Block](#sec:ITCEIBlock) respectively, $N_\mu=$`NXS(6)`+1 and $N_\mu=$`NXS(8)`+1 discrete cosines are given.

<a id="tab:ITCABlock"></a>

| Location in `XSS` | Parameter | Description |
|:---|:---|:---|
| $S_{\mathrm{ITCA}}$ | $\mu_l[E_{el}(1)], l=1,\ldots,N_\mu$ | Discrete cosines for elastic scattering at $E_{el}(1)$ |
| $S_{\mathrm{ITCA}}$+$N_\mu$ | $\mu_l[E_{el}(2)], l=1,\ldots,N_\mu$ | Discrete cosines for elastic scattering at $E_{el}(2)$ |
| ⋮ | ⋮ | ⋮ |
| $S_{\mathrm{ITCA}}$+($N_{el}$-1)$N_\mu$ | $\mu_l[E_{el}(N_{el})], l=1,\ldots,N_\mu$ | Discrete cosines for elastic scattering at $E_{el}(N_{el})$ |

`ITCA` Block.

The incident elastic energy grid $E_{el}(l)$ is given in the [`ITCE` Block](#sec:ITCEBlock) or [`ITCEI` Block](#sec:ITCEIBlock). Linear-linear interpolation is assumed between adjacent values of $E_{el}$.

<a id="sec:ContinuousEnergyPhoton"></a>

# Continuous-Energy Photon

<a id="sec:NXSContinuousEnergyPhoton"></a>

## `NXS` Array

| Element | Name | Description                                  |
|--------:|:-----|:---------------------------------------------|
|       1 | —    | Length of second block of data (`XSS` array) |
|       2 | Z    | Atomic number                                |
|       3 | NES  | Number of energies                           |
|       4 | NFLC | Length of the flourescence data divided by 4 |
|       5 | NSH  | Number of electron shells                    |
|         | …    |                                              |
|      16 | —    |                                              |

`NXS` array element definitions for continuous-energyphoton ACE Table.

<a id="sec:JXSContinuousEnergyPhoton"></a>

## `JXS` Array

<a id="tab:JXSContinuousEnergyPhoton"></a>

| Element | Name  | Location Description                    |
|--------:|:------|:----------------------------------------|
|       1 | ESZG  | Energy table                            |
|       2 | JINC  | Incoherent form factors                 |
|       3 | JCOH  | Coherent form factors                   |
|       4 | JFLO  | Fluorescence data                       |
|       5 | LHNM  | Heating numbers                         |
|       6 | LNEPS | Number of electrons per shell           |
|       7 | LBEPS | Binding energy per shell                |
|       8 | LPIPS | Probability of interaction per shell    |
|       9 | LSWD  | Array of offsets to the shell-wise data |
|      10 | SWD   | Shell-wise data in PDF and CDF form     |
|         | …     |                                         |
|      32 | —     |                                         |

`JXS` array element definitions for continuous-energy photon ACE Table.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Conlin:2012Updat-0" class="csl-entry">

Conlin, Jeremy Lloyd, Forrest B. Brown, A. C. Kahler, M. Beth Lee, D. Kent Parsons, and Morgan C. White. 2012. “Updating the Format of ACE Data Tables.” In *Transactions of the American Nuclear Socity*, edited by Julie Rule, vol. 107. American Nuclear Society.

</div>

<div id="ref-Trkov:2011ENDF--0" class="csl-entry">

Trkov, A., M. Herman, and D. A. Brown. 2011. *ENDF-6 Formats Manual: Data Formats and Procedures for the Evaluated Nuclear Data Files*. BNL-90365-2009 Rev.2. National Nuclear Data Center, Brookhaven National Laboratory.

</div>

</div>

[^1]: data about the data

[^2]: See, for example, Table [3](#tab:NXSContinuousEnergyNeutron) and Table [4](#tab:JXSContinuousEnergyNeutron).

[^3]: pronounced “ess-ZAID”

[^4]: Note that this is an obsolete format. It only exists when $\texttt{JXS(12)} \neq 0$ and $\texttt{JXS(13)} = 0$.
