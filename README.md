Link to dataset: https://archive.ics.uci.edu/dataset/248/buzz+in+social+media

# Introduction
The Buzz Prediction dataset contains data on two social media sites: Tom's Hardware and Twitter. 

**Mention what each row in the dataset means, ie measurement of feature at time t related to target (mean number of active discussions of an instance's topic).**

This notebook analyzes the Twitter dataset. The dataset contains information on the mean number of active discussions (NAD) of an instance's topic. 

There are 11 features in the Twitter dataset. Each are marked with a suffix [0, 6] denoting a timestamp.
- **Number of Created Discussions (NCD):** Number of discussions created at time step t and involving the instance's topic. 
- **Author Increase (AI):** Number of new authors interacting on the instance's topic at time t.
- **Attention Level (AS(NA)):** Measure of the attention paid to an instance's topic on the social media.
- **Burstiness Level (BL):** Burstiness level for a topic z at time t, defined as the ratio of NCD/NAD. 
- **Number of Atomic Containers (NAC):** Measures the total number of atomic containers generated through the social media on the instance's topic until time t.
- **Attention Level (AS(NAC)):** Measure of the attention paid to the instance's topic on a social media.
- **Contribution Sparseness (CS):** Measure of spreading of contributions over discussion for the instance's topic at time t. 
- **Author Interaction (AT):** Measures the average number of authors interacting on the instance's topic within a discussion.
- **Number of Authors (NA):** Measures the number of authors interacting on the instance's topic at time t.
- **Average Discussions Length (ADL):** Measures the average length of a discussion belonging to an instance's topic.
- **Average Discussions Length (NAD):** Measures the number of discussions involving the instance's topic until time t. 

# Data Loading

# EDA
The dataset included descriptive statistics on the features.
NCD:
<table>
  <thead>
    <tr><th colspan="5"><strong>NCD</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>NCD_0</td><td>0</td><td>24210</td><td>140.340</td><td>431.772</td></tr>
    <tr><td>NCD_1</td><td>0</td><td>29574</td><td>136.770</td><td>432.305</td></tr>
    <tr><td>NCD_2</td><td>0</td><td>37505</td><td>159.679</td><td>502.057</td></tr>
    <tr><td>NCD_3</td><td>0</td><td>72366</td><td>181.592</td><td>574.883</td></tr>
    <tr><td>NCD_4</td><td>0</td><td>79079</td><td>201.097</td><td>630.448</td></tr>
    <tr><td>NCD_5</td><td>0</td><td>79079</td><td>220.175</td><td>669.205</td></tr>
    <tr><td>NCD_6</td><td>0</td><td>79079</td><td>219.388</td><td>672.182</td></tr>
  </tbody>
</table>
AI:
<table>
  <thead>
    <tr><th colspan="5"><strong>AI</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>AI_0</td><td>0</td><td>18654</td><td>71.038</td><td>196.877</td></tr>
    <tr><td>AI_1</td><td>0</td><td>22035</td><td>69.830</td><td>202.200</td></tr>
    <tr><td>AI_2</td><td>0</td><td>29402</td><td>82.198</td><td>239.523</td></tr>
    <tr><td>AI_3</td><td>0</td><td>57617</td><td>93.775</td><td>278.892</td></tr>
    <tr><td>AI_4</td><td>0</td><td>63147</td><td>103.896</td><td>309.197</td></tr>
    <tr><td>AI_5</td><td>0</td><td>63147</td><td>113.611</td><td>326.077</td></tr>
    <tr><td>AI_6</td><td>0</td><td>63147</td><td>112.941</td><td>326.015</td></tr>
  </tbody>
</table>
AS(NA):
<table>
  <thead>
    <tr><th colspan="5"><strong>AS(NA)</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>AS(NA)_0</td><td>0</td><td>0.025</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_1</td><td>0</td><td>0.029</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_2</td><td>0</td><td>0.040</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_3</td><td>0</td><td>0.081</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_4</td><td>0</td><td>0.095</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_5</td><td>0</td><td>0.095</td><td>0.000</td><td>0.001</td></tr>
    <tr><td>AS(NA)_6</td><td>0</td><td>0.095</td><td>0.000</td><td>0.001</td></tr>
  </tbody>
</table>
BL:
<table>
  <thead>
    <tr><th colspan="5"><strong>BL</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>BL_0</td><td>0</td><td>1</td><td>0.925</td><td>0.256</td></tr>
    <tr><td>BL_1</td><td>0</td><td>1</td><td>0.918</td><td>0.268</td></tr>
    <tr><td>BL_2</td><td>0</td><td>1</td><td>0.907</td><td>0.285</td></tr>
    <tr><td>BL_3</td><td>0</td><td>1</td><td>0.920</td><td>0.265</td></tr>
    <tr><td>BL_4</td><td>0</td><td>1</td><td>0.931</td><td>0.247</td></tr>
    <tr><td>BL_5</td><td>0</td><td>1</td><td>0.956</td><td>0.196</td></tr>
    <tr><td>BL_6</td><td>0</td><td>1</td><td>0.955</td><td>0.197</td></tr>
  </tbody>
</table>
NAC:
<table>
  <thead>
    <tr><th colspan="5"><strong>NAC</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>NAC_0</td><td>0</td><td>26644</td><td>150.662</td><td>453.689</td></tr>
    <tr><td>NAC_1</td><td>0</td><td>29574</td><td>146.642</td><td>452.039</td></tr>
    <tr><td>NAC_2</td><td>0</td><td>37505</td><td>170.721</td><td>523.801</td></tr>
    <tr><td>NAC_3</td><td>0</td><td>72397</td><td>193.786</td><td>598.287</td></tr>
    <tr><td>NAC_4</td><td>0</td><td>79136</td><td>214.196</td><td>654.468</td></tr>
    <tr><td>NAC_5</td><td>0</td><td>79136</td><td>234.218</td><td>694.165</td></tr>
    <tr><td>NAC_6</td><td>0</td><td>79136</td><td>233.236</td><td>696.419</td></tr>
  </tbody>
</table>
AS(NAC):
<table>
  <thead>
    <tr><th colspan="5"><strong>AS(NAC)</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>AS(NAC)_0</td><td>0</td><td>0.022</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_1</td><td>0</td><td>0.022</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_2</td><td>0</td><td>0.022</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_3</td><td>0</td><td>0.040</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_4</td><td>0</td><td>0.046</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_5</td><td>0</td><td>0.046</td><td>0.000</td><td>0.000</td></tr>
    <tr><td>AS(NAC)_6</td><td>0</td><td>0.046</td><td>0.000</td><td>0.000</td></tr>
  </tbody>
</table>
CS:
<table>
  <thead>
    <tr><th colspan="5"><strong>CS</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>CS_0</td><td>0</td><td>1</td><td>0.931</td><td>0.254</td></tr>
    <tr><td>CS_1</td><td>0</td><td>1</td><td>0.923</td><td>0.266</td></tr>
    <tr><td>CS_2</td><td>0</td><td>1</td><td>0.912</td><td>0.284</td></tr>
    <tr><td>CS_3</td><td>0</td><td>1</td><td>0.925</td><td>0.264</td></tr>
    <tr><td>CS_4</td><td>0</td><td>1</td><td>0.935</td><td>0.246</td></tr>
    <tr><td>CS_5</td><td>0</td><td>1</td><td>0.961</td><td>0.194</td></tr>
    <tr><td>CS_6</td><td>0</td><td>1</td><td>0.961</td><td>0.194</td></tr>
  </tbody>
</table>

AT:
<table>
  <thead>
    <tr><th colspan="5"><strong>AT</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>AT_0</td><td>0</td><td>282</td><td>1.045</td><td>1.359</td></tr>
    <tr><td>AT_1</td><td>0</td><td>283</td><td>1.035</td><td>1.470</td></tr>
    <tr><td>AT_2</td><td>0</td><td>283</td><td>1.017</td><td>1.208</td></tr>
    <tr><td>AT_3</td><td>0</td><td>263</td><td>1.033</td><td>1.250</td></tr>
    <tr><td>AT_4</td><td>0</td><td>282</td><td>1.046</td><td>1.286</td></tr>
    <tr><td>AT_5</td><td>0</td><td>249</td><td>1.078</td><td>1.300</td></tr>
    <tr><td>AT_6</td><td>0</td><td>283</td><td>1.082</td><td>1.423</td></tr>
  </tbody>
</table>

NA:
<table>
  <thead>
    <tr><th colspan="5"><strong>NA</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>NA_0</td><td>0</td><td>21723</td><td>123.064</td><td>350.215</td></tr>
    <tr><td>NA_1</td><td>0</td><td>26134</td><td>119.580</td><td>347.236</td></tr>
    <tr><td>NA_2</td><td>0</td><td>34085</td><td>138.959</td><td>403.603</td></tr>
    <tr><td>NA_3</td><td>0</td><td>64984</td><td>157.424</td><td>460.884</td></tr>
    <tr><td>NA_4</td><td>0</td><td>72159</td><td>173.702</td><td>503.660</td></tr>
    <tr><td>NA_5</td><td>0</td><td>72159</td><td>189.521</td><td>532.315</td></tr>
    <tr><td>NA_6</td><td>0</td><td>72159</td><td>188.410</td><td>531.152</td></tr>
  </tbody>
</table>

ADL:
<table>
  <thead>
    <tr><th colspan="5"><strong>ADL</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>ADL_0</td><td>0</td><td>294</td><td>1.095</td><td>1.488</td></tr>
    <tr><td>ADL_1</td><td>0</td><td>295</td><td>1.084</td><td>1.587</td></tr>
    <tr><td>ADL_2</td><td>0</td><td>295</td><td>1.067</td><td>1.316</td></tr>
    <tr><td>ADL_3</td><td>0</td><td>273</td><td>1.085</td><td>1.371</td></tr>
    <tr><td>ADL_4</td><td>0</td><td>294</td><td>1.100</td><td>1.406</td></tr>
    <tr><td>ADL_5</td><td>0</td><td>262</td><td>1.137</td><td>1.432</td></tr>
    <tr><td>ADL_6</td><td>0</td><td>295</td><td>1.140</td><td>1.552</td></tr>
  </tbody>
</table>

NAD:
<table>
  <thead>
    <tr><th colspan="5"><strong>NAD</strong></th></tr>
    <tr><th>feature</th><th>min</th><th>max</th><th>mean</th><th>std</th></tr>
  </thead>
  <tbody>
    <tr><td>NAD_0</td><td>0</td><td>24301</td><td>140.790</td><td>432.625</td></tr>
    <tr><td>NAD_1</td><td>0</td><td>29574</td><td>137.181</td><td>433.026</td></tr>
    <tr><td>NAD_2</td><td>0</td><td>37505</td><td>160.106</td><td>502.774</td></tr>
    <tr><td>NAD_3</td><td>0</td><td>72366</td><td>182.057</td><td>575.658</td></tr>
    <tr><td>NAD_4</td><td>0</td><td>79083</td><td>201.596</td><td>631.258</td></tr>
    <tr><td>NAD_5</td><td>0</td><td>79083</td><td>220.706</td><td>670.050</td></tr>
    <tr><td>NAD_6</td><td>0</td><td>79083</td><td>219.937</td><td>673.032</td></tr>
  </tbody>
</table>

# Data Cleaning
There are no missing values in the dataset.

# Model Building

# Conclusions