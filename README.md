Link to dataset: https://archive.ics.uci.edu/dataset/248/buzz+in+social+media

# Introduction
This notebook analyzes the Twitter dataset from the Buzz Prediction dataset. The target variable is the mean number of active discussions (NAD) of an instance's topic. Each row is a measurement of a feature of a topic *z*, with each feature representing a time *t* in (0,6).

There are 11 features in the Twitter dataset. Each are marked with a suffix [0, 6] denoting a timestamp. The dataset description included descriptive statistics on the features.
- **Number of Created Discussions (NCD):** Number of discussions created at time step t and involving the instance's topic. 
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

- **Author Increase (AI):** Number of new authors interacting on the instance's topic at time t.
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

- **Attention Level (AS(NA)):** Measure of the attention paid to an instance's topic on the social media.
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

- **Burstiness Level (BL):** Burstiness level for a topic z at time t, defined as the ratio of NCD/NAD. 
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

- **Number of Atomic Containers (NAC):** Measures the total number of atomic containers generated through the social media on the instance's topic until time t.
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

- **Attention Level (AS(NAC)):** Measure of the attention paid to the instance's topic on a social media.
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

- **Contribution Sparseness (CS):** Measure of spreading of contributions over discussion for the instance's topic at time t. 
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

- **Author Interaction (AT):** Measures the average number of authors interacting on the instance's topic within a discussion.
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

- **Number of Authors (NA):** Measures the number of authors interacting on the instance's topic at time t.
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

- **Average Discussions Length (ADL):** Measures the average length of a discussion belonging to an instance's topic.
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

- **Average Discussions Length (NAD):** Measures the number of discussions involving the instance's topic until time t. 
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

# Data Loading
The Twitter dataset contained 583,250 rows and 78 columns. The columns measured various statistics about the social media platform.

The features were split into 11 groups. Each group was measured at a time *t* in 7 periods. The features were renamed in the working dataset as listed in the table below.

The target feature measured the mean number of active discussions.

<table align="center">
<tr><th>Working_Name</th></tr>
<tr><td><code>NCD</code></td></tr>
<tr><td><code>NumNewDiscussions</code></td></tr>
<tr><td><code>AI</code></td></tr>
<tr><td><code>NumNewAuthors</code></td></tr>
<tr><td><code>AS_NA</code></td></tr>
<tr><td><code>AttentionPaid</code></td></tr>
<tr><td><code>BL</code></td></tr>
<tr><td><code>BurstinessLevel</code></td></tr>
<tr><td><code>NAC</code></td></tr>
<tr><td><code>NumAtomicContainers</code></td></tr>
<tr><td><code>AS_NAC</code></td></tr>
<tr><td><code>NumContributions</code></td></tr>
<tr><td><code>CS</code></td></tr>
<tr><td><code>ContributionSpread</code></td></tr>
<tr><td><code>AT</code></td></tr>
<tr><td><code>AuthorInteraction</code></td></tr>
<tr><td><code>NA</code></td></tr>
<tr><td><code>NumAuthorsInteracting</code></td></tr>
<tr><td><code>ADL</code></td></tr>
<tr><td><code>AverageDiscussionLength</code></td></tr>
<tr><td><code>NAD</code></td></tr>
<tr><td><code>NumDiscussions</code></td></tr>
<tr><td><code>buzz</code></td></tr>
<tr><td><code>buzz (target)</code></td></tr>
</table>

# Feature Engineering
This analysis created 2 features called **DiscussionsPerAuthor** and **AttentionPerAuthor**.

DiscussionsPerAuthor_t was defined as the ratio between ContributionSpread_t and AuthorInteraction_t at time *t*. 

AttentionPerAuthor_t was defined as the ratio between NumContributions_t and AttentionPaid_t at time *t*.

The BurstinessLevel feature was an existing ratio feature, and it used 0.0 in place of 0/0 divisions. This analysis made the same modification to the DiscussionsPerAuthor and AttentionPerAuthor features.

# EDA
The dataset included descriptive statistics on the feature groups. This analysis also performed summary statistic analysis, distribution analysis using skew and kurtosis, and correlation analysis.

<table>
  <thead>
    <tr>
      <th>Statistic</th>
      <th>NumNewDiscussions_0</th>
      <th>NumNewDiscussions_1</th>
      <th>NumNewDiscussions_2</th>
      <th>NumNewDiscussions_3</th>
      <th>NumNewDiscussions_4</th>
      <th>NumNewDiscussions_5</th>
      <th>NumNewDiscussions_6</th>
      <th>NumNewAuthors_0</th>
      <th>NumNewAuthors_1</th>
      <th>NumNewAuthors_2</th>
      <th>NumNewAuthors_3</th>
      <th>NumNewAuthors_4</th>
      <th>NumNewAuthors_5</th>
      <th>NumNewAuthors_6</th>
      <th>AttentionPaid_0</th>
      <th>AttentionPaid_1</th>
      <th>AttentionPaid_2</th>
      <th>AttentionPaid_3</th>
      <th>AttentionPaid_4</th>
      <th>AttentionPaid_5</th>
      <th>AttentionPaid_6</th>
      <th>BurstinessLevel_0</th>
      <th>BurstinessLevel_1</th>
      <th>BurstinessLevel_2</th>
      <th>BurstinessLevel_3</th>
      <th>BurstinessLevel_4</th>
      <th>BurstinessLevel_5</th>
      <th>BurstinessLevel_6</th>
      <th>NumAtomicContainers_0</th>
      <th>NumAtomicContainers_1</th>
      <th>NumAtomicContainers_2</th>
      <th>NumAtomicContainers_3</th>
      <th>NumAtomicContainers_4</th>
      <th>NumAtomicContainers_5</th>
      <th>NumAtomicContainers_6</th>
      <th>NumContributions_0</th>
      <th>NumContributions_1</th>
      <th>NumContributions_2</th>
      <th>NumContributions_3</th>
      <th>NumContributions_4</th>
      <th>NumContributions_5</th>
      <th>NumContributions_6</th>
      <th>ContributionSpread_0</th>
      <th>ContributionSpread_1</th>
      <th>ContributionSpread_2</th>
      <th>ContributionSpread_3</th>
      <th>ContributionSpread_4</th>
      <th>ContributionSpread_5</th>
      <th>ContributionSpread_6</th>
      <th>AuthorInteraction_0</th>
      <th>AuthorInteraction_1</th>
      <th>AuthorInteraction_2</th>
      <th>AuthorInteraction_3</th>
      <th>AuthorInteraction_4</th>
      <th>AuthorInteraction_5</th>
      <th>AuthorInteraction_6</th>
      <th>NumAuthorsInteracting_0</th>
      <th>NumAuthorsInteracting_1</th>
      <th>NumAuthorsInteracting_2</th>
      <th>NumAuthorsInteracting_3</th>
      <th>NumAuthorsInteracting_4</th>
      <th>NumAuthorsInteracting_5</th>
      <th>NumAuthorsInteracting_6</th>
      <th>AverageDiscussionLength_0</th>
      <th>AverageDiscussionLength_1</th>
      <th>AverageDiscussionLength_2</th>
      <th>AverageDiscussionLength_3</th>
      <th>AverageDiscussionLength_4</th>
      <th>AverageDiscussionLength_5</th>
      <th>AverageDiscussionLength_6</th>
      <th>NumDiscussions_0</th>
      <th>NumDiscussions_1</th>
      <th>NumDiscussions_2</th>
      <th>NumDiscussions_3</th>
      <th>NumDiscussions_4</th>
      <th>NumDiscussions_5</th>
      <th>NumDiscussions_6</th>
      <th>buzz</th>
      <th>DiscussionsPerAuthor_0</th>
      <th>DiscussionsPerAuthor_1</th>
      <th>DiscussionsPerAuthor_2</th>
      <th>DiscussionsPerAuthor_3</th>
      <th>DiscussionsPerAuthor_4</th>
      <th>DiscussionsPerAuthor_5</th>
      <th>DiscussionsPerAuthor_6</th>
      <th>AttentionPerAuthor_0</th>
      <th>AttentionPerAuthor_1</th>
      <th>AttentionPerAuthor_2</th>
      <th>AttentionPerAuthor_3</th>
      <th>AttentionPerAuthor_4</th>
      <th>AttentionPerAuthor_5</th>
      <th>AttentionPerAuthor_6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>count</b></td>
      <td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td><td>583250.0</td>
    </tr>
    <tr>
      <td><b>mean</b></td>
      <td>140.34</td><td>136.77</td><td>159.68</td><td>181.59</td><td>201.10</td><td>220.18</td><td>219.39</td><td>71.04</td><td>69.83</td><td>82.20</td><td>93.77</td><td>103.90</td><td>113.61</td><td>112.94</td><td>0.0002</td><td>0.0002</td><td>0.0002</td><td>0.0002</td><td>0.0003</td><td>0.0003</td><td>0.0003</td><td>0.9254</td><td>0.9181</td><td>0.9071</td><td>0.9200</td><td>0.9307</td><td>0.9561</td><td>0.9553</td><td>150.66</td><td>146.64</td><td>170.72</td><td>193.79</td><td>214.20</td><td>234.22</td><td>233.24</td><td>0.0001</td><td>0.0001</td><td>0.0001</td><td>0.0001</td><td>0.0001</td><td>0.0002</td><td>0.0002</td><td>0.9308</td><td>0.9231</td><td>0.9116</td><td>0.9246</td><td>0.9354</td><td>0.9609</td><td>0.9606</td><td>1.0455</td><td>1.0352</td><td>1.0170</td><td>1.0326</td><td>1.0459</td><td>1.0781</td><td>1.0818</td><td>123.06</td><td>119.58</td><td>138.96</td><td>157.42</td><td>173.70</td><td>189.52</td><td>188.41</td><td>1.0953</td><td>1.0837</td><td>1.0667</td><td>1.0852</td><td>1.1002</td><td>1.1367</td><td>1.1404</td><td>140.79</td><td>137.18</td><td>160.11</td><td>182.06</td><td>201.60</td><td>220.71</td><td>219.94</td><td>191.28</td><td>0.8798</td><td>0.8733</td><td>0.8613</td><td>0.8730</td><td>0.8827</td><td>0.9056</td><td>0.9049</td><td>0.4985</td><td>0.4944</td><td>0.4978</td><td>0.5093</td><td>0.5193</td><td>0.5398</td><td>0.5392</td>
    </tr>
    <tr>
      <td><b>std</b></td>
      <td>431.77</td><td>432.31</td><td>502.06</td><td>574.88</td><td>630.45</td><td>669.21</td><td>672.18</td><td>196.88</td><td>202.20</td><td>239.52</td><td>278.89</td><td>309.20</td><td>326.08</td><td>326.02</td><td>0.0006</td><td>0.0006</td><td>0.0006</td><td>0.0007</td><td>0.0007</td><td>0.0007</td><td>0.0007</td><td>0.2555</td><td>0.2677</td><td>0.2846</td><td>0.2650</td><td>0.2471</td><td>0.1960</td><td>0.1970</td><td>453.69</td><td>452.04</td><td>523.80</td><td>598.29</td><td>654.47</td><td>694.17</td><td>696.42</td><td>0.0003</td><td>0.0003</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.0004</td><td>0.2538</td><td>0.2665</td><td>0.2839</td><td>0.2641</td><td>0.2459</td><td>0.1939</td><td>0.1945</td><td>1.3594</td><td>1.4697</td><td>1.2081</td><td>1.2502</td><td>1.2863</td><td>1.3000</td><td>1.4229</td><td>350.22</td><td>347.24</td><td>403.60</td><td>460.88</td><td>503.66</td><td>532.32</td><td>531.15</td><td>1.4880</td><td>1.5869</td><td>1.3158</td><td>1.3707</td><td>1.4057</td><td>1.4323</td><td>1.5523</td><td>432.62</td><td>433.03</td><td>502.77</td><td>575.66</td><td>631.26</td><td>670.05</td><td>673.03</td><td>612.35</td><td>0.2657</td><td>0.2760</td><td>0.2901</td><td>0.2733</td><td>0.2582</td><td>0.2167</td><td>0.2177</td><td>0.3160</td><td>0.2936</td><td>0.3171</td><td>0.3410</td><td>0.3719</td><td>0.3834</td><td>0.3831</td>
    </tr>
    <tr>
      <td><b>min</b></td>
      <td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td>
    </tr>
    <tr>
      <td><b>25%</b></td>
      <td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>5.0</td><td>6.0</td><td>6.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>4e-06</td><td>4e-06</td><td>5e-06</td><td>6e-06</td><td>7e-06</td><td>8e-06</td><td>8e-06</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>5.0</td><td>5.0</td><td>7.0</td><td>7.0</td><td>2e-06</td><td>2e-06</td><td>3e-06</td><td>3e-06</td><td>3e-06</td><td>4e-06</td><td>4e-06</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>5.0</td><td>6.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>3.0</td><td>3.0</td><td>4.0</td><td>4.0</td><td>5.0</td><td>6.0</td><td>6.0</td><td>4.5</td><td>0.9091</td><td>0.9070</td><td>0.8961</td><td>0.9033</td><td>0.9091</td><td>0.9203</td><td>0.9200</td><td>0.4615</td><td>0.4583</td><td>0.4593</td><td>0.4615</td><td>0.4652</td><td>0.4701</td><td>0.4689</td>
    </tr>
    <tr>
      <td><b>50%</b></td>
      <td>18.0</td><td>17.0</td><td>21.0</td><td>24.0</td><td>27.0</td><td>31.0</td><td>30.0</td><td>11.0</td><td>11.0</td><td>13.0</td><td>14.0</td><td>16.0</td><td>19.0</td><td>18.0</td><td>2.6e-05</td><td>2.5e-05</td><td>2.9e-05</td><td>3.3e-05</td><td>3.7e-05</td><td>4.2e-05</td><td>4.1e-05</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>20.0</td><td>19.0</td><td>23.0</td><td>26.0</td><td>30.0</td><td>34.0</td><td>34.0</td><td>1.4e-05</td><td>1.3e-05</td><td>1.6e-05</td><td>1.8e-05</td><td>2e-05</td><td>2.3e-05</td><td>2.3e-05</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>17.0</td><td>17.0</td><td>20.0</td><td>22.0</td><td>25.0</td><td>29.0</td><td>28.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>18.0</td><td>17.0</td><td>21.0</td><td>24.0</td><td>27.0</td><td>31.0</td><td>31.0</td><td>25.5</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td>
    </tr>
    <tr>
      <td><b>75%</b></td>
      <td>104.0</td><td>100.0</td><td>115.0</td><td>131.0</td><td>147.0</td><td>166.0</td><td>164.0</td><td>59.0</td><td>57.0</td><td>65.0</td><td>74.0</td><td>82.0</td><td>92.0</td><td>91.0</td><td>0.0002</td><td>0.0001</td><td>0.0002</td><td>0.0002</td><td>0.0002</td><td>0.0002</td><td>0.0002</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>113.0</td><td>108.0</td><td>125.0</td><td>143.0</td><td>161.0</td><td>181.0</td><td>179.0</td><td>8.5e-05</td><td>8.2e-05</td><td>9.4e-05</td><td>0.0001</td><td>0.0001</td><td>0.0001</td><td>0.0001</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0526</td><td>1.0500</td><td>1.0541</td><td>1.0568</td><td>1.0588</td><td>1.0631</td><td>1.0633</td><td>96.0</td><td>92.0</td><td>105.0</td><td>118.0</td><td>132.0</td><td>148.0</td><td>146.0</td><td>1.0744</td><td>1.0714</td><td>1.0769</td><td>1.0811</td><td>1.0836</td><td>1.0909</td><td>1.0913</td><td>104.0</td><td>101.0</td><td>115.0</td><td>131.0</td><td>148.0</td><td>167.0</td><td>165.0</td><td>139.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.5565</td><td>0.5556</td><td>0.5581</td><td>0.5610</td><td>0.5632</td><td>0.5709</td><td>0.5706</td>
    </tr>
    <tr>
      <td><b>max</b></td>
      <td>24210.0</td><td>29574.0</td><td>37505.0</td><td>72366.0</td><td>79079.0</td><td>79079.0</td><td>79079.0</td><td>18654.0</td><td>22035.0</td><td>29402.0</td><td>57617.0</td><td>63147.0</td><td>63147.0</td><td>63147.0</td><td>0.0250</td><td>0.0294</td><td>0.0403</td><td>0.0811</td><td>0.0946</td><td>0.0946</td><td>0.0946</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>26644.0</td><td>29574.0</td><td>37505.0</td><td>72397.0</td><td>79136.0</td><td>79136.0</td><td>79136.0</td><td>0.0225</td><td>0.0225</td><td>0.0225</td><td>0.0402</td><td>0.0460</td><td>0.0460</td><td>0.0460</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>282.0</td><td>283.0</td><td>283.0</td><td>263.0</td><td>282.0</td><td>249.0</td><td>283.0</td><td>21723.0</td><td>26134.0</td><td>34085.0</td><td>64984.0</td><td>72159.0</td><td>72159.0</td><td>72159.0</td><td>294.0</td><td>295.0</td><td>295.0</td><td>273.0</td><td>294.0</td><td>262.0</td><td>295.0</td><td>24301.0</td><td>29574.0</td><td>37505.0</td><td>72366.0</td><td>79083.0</td><td>79083.0</td><td>79083.0</td><td>75724.5</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>63.1111</td><td>41.7143</td><td>51.0</td><td>51.0</td><td>63.1111</td><td>63.1111</td><td>63.1111</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Column</th>
      <th>Skew</th>
      <th>Kurtosis</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>0</td><td>NumNewDiscussions_0</td><td>12.7087</td><td>310.3021</td></tr>
    <tr><td>1</td><td>NumNewDiscussions_1</td><td>14.1261</td><td>407.9773</td></tr>
    <tr><td>2</td><td>NumNewDiscussions_2</td><td>14.5678</td><td>443.4133</td></tr>
    <tr><td>3</td><td>NumNewDiscussions_3</td><td>17.2519</td><td>819.5164</td></tr>
    <tr><td>4</td><td>NumNewDiscussions_4</td><td>18.7265</td><td>1048.3705</td></tr>
    <tr><td>5</td><td>NumNewDiscussions_5</td><td>17.3934</td><td>869.9598</td></tr>
    <tr><td>6</td><td>NumNewDiscussions_6</td><td>17.5216</td><td>867.2118</td></tr>
    <tr><td>7</td><td>NumNewAuthors_0</td><td>14.3682</td><td>643.8704</td></tr>
    <tr><td>8</td><td>NumNewAuthors_1</td><td>17.8591</td><td>1016.4396</td></tr>
    <tr><td>9</td><td>NumNewAuthors_2</td><td>18.4894</td><td>1085.2191</td></tr>
    <tr><td>10</td><td>NumNewAuthors_3</td><td>29.8824</td><td>3803.7105</td></tr>
    <tr><td>11</td><td>NumNewAuthors_4</td><td>37.8265</td><td>5519.9874</td></tr>
    <tr><td>12</td><td>NumNewAuthors_5</td><td>33.9559</td><td>4530.2147</td></tr>
    <tr><td>13</td><td>NumNewAuthors_6</td><td>33.9159</td><td>4523.5084</td></tr>
    <tr><td>14</td><td>AttentionPaid_0</td><td>10.2041</td><td>214.8216</td></tr>
    <tr><td>15</td><td>AttentionPaid_1</td><td>10.7005</td><td>243.8883</td></tr>
    <tr><td>16</td><td>AttentionPaid_2</td><td>10.6292</td><td>265.7545</td></tr>
    <tr><td>17</td><td>AttentionPaid_3</td><td>13.1464</td><td>630.8066</td></tr>
    <tr><td>18</td><td>AttentionPaid_4</td><td>15.8651</td><td>1065.7910</td></tr>
    <tr><td>19</td><td>AttentionPaid_5</td><td>14.7326</td><td>908.2112</td></tr>
    <tr><td>20</td><td>AttentionPaid_6</td><td>15.0350</td><td>946.8968</td></tr>
    <tr><td>21</td><td>BurstinessLevel_0</td><td>-3.3186</td><td>9.0874</td></tr>
    <tr><td>22</td><td>BurstinessLevel_1</td><td>-3.1167</td><td>7.7687</td></tr>
    <tr><td>23</td><td>BurstinessLevel_2</td><td>-2.8576</td><td>6.2067</td></tr>
    <tr><td>24</td><td>BurstinessLevel_3</td><td>-3.1629</td><td>8.0589</td></tr>
    <tr><td>25</td><td>BurstinessLevel_4</td><td>-3.4747</td><td>10.1494</td></tr>
    <tr><td>26</td><td>BurstinessLevel_5</td><td>-4.6183</td><td>19.5269</td></tr>
    <tr><td>27</td><td>BurstinessLevel_6</td><td>-4.5836</td><td>19.2217</td></tr>
    <tr><td>28</td><td>NumAtomicContainers_0</td><td>12.2857</td><td>296.2320</td></tr>
    <tr><td>29</td><td>NumAtomicContainers_1</td><td>13.4611</td><td>372.8738</td></tr>
    <tr><td>30</td><td>NumAtomicContainers_2</td><td>13.9793</td><td>410.9312</td></tr>
    <tr><td>31</td><td>NumAtomicContainers_3</td><td>16.4133</td><td>734.5925</td></tr>
    <tr><td>32</td><td>NumAtomicContainers_4</td><td>17.7396</td><td>934.0292</td></tr>
    <tr><td>33</td><td>NumAtomicContainers_5</td><td>16.5302</td><td>778.7297</td></tr>
    <tr><td>34</td><td>NumAtomicContainers_6</td><td>16.6778</td><td>779.2287</td></tr>
    <tr><td>35</td><td>NumContributions_0</td><td>13.1170</td><td>349.8339</td></tr>
    <tr><td>36</td><td>NumContributions_1</td><td>13.5970</td><td>375.3183</td></tr>
    <tr><td>37</td><td>NumContributions_2</td><td>12.7660</td><td>340.3730</td></tr>
    <tr><td>38</td><td>NumContributions_3</td><td>13.7106</td><td>488.7623</td></tr>
    <tr><td>39</td><td>NumContributions_4</td><td>14.7603</td><td>658.7599</td></tr>
    <tr><td>40</td><td>NumContributions_5</td><td>13.8609</td><td>572.6602</td></tr>
    <tr><td>41</td><td>NumContributions_6</td><td>13.8709</td><td>578.0207</td></tr>
    <tr><td>42</td><td>ContributionSpread_0</td><td>-3.3949</td><td>9.5255</td></tr>
    <tr><td>43</td><td>ContributionSpread_1</td><td>-3.1750</td><td>8.0809</td></tr>
    <tr><td>44</td><td>ContributionSpread_2</td><td>-2.9000</td><td>6.4101</td></tr>
    <tr><td>45</td><td>ContributionSpread_3</td><td>-3.2157</td><td>8.3409</td></tr>
    <tr><td>46</td><td>ContributionSpread_4</td><td>-3.5415</td><td>10.5420</td></tr>
    <tr><td>47</td><td>ContributionSpread_5</td><td>-4.7544</td><td>20.6039</td></tr>
    <tr><td>48</td><td>ContributionSpread_6</td><td>-4.7369</td><td>20.4383</td></tr>
    <tr><td>49</td><td>AuthorInteraction_0</td><td>70.6416</td><td>8079.0839</td></tr>
    <tr><td>50</td><td>AuthorInteraction_1</td><td>77.8096</td><td>9211.5903</td></tr>
    <tr><td>51</td><td>AuthorInteraction_2</td><td>77.4423</td><td>10598.9011</td></tr>
    <tr><td>52</td><td>AuthorInteraction_3</td><td>77.2830</td><td>9528.8512</td></tr>
    <tr><td>53</td><td>AuthorInteraction_4</td><td>87.7194</td><td>12453.3750</td></tr>
    <tr><td>54</td><td>AuthorInteraction_5</td><td>78.9710</td><td>9575.1954</td></tr>
    <tr><td>55</td><td>AuthorInteraction_6</td><td>86.1412</td><td>11346.7699</td></tr>
    <tr><td>56</td><td>NumAuthorsInteracting_0</td><td>11.6804</td><td>315.0737</td></tr>
    <tr><td>57</td><td>NumAuthorsInteracting_1</td><td>13.1570</td><td>437.4251</td></tr>
    <tr><td>58</td><td>NumAuthorsInteracting_2</td><td>13.7674</td><td>482.3085</td></tr>
    <tr><td>59</td><td>NumAuthorsInteracting_3</td><td>17.4888</td><td>1071.9285</td></tr>
    <tr><td>60</td><td>NumAuthorsInteracting_4</td><td>20.0880</td><td>1513.5567</td></tr>
    <tr><td>61</td><td>NumAuthorsInteracting_5</td><td>18.4934</td><td>1255.9139</td></tr>
    <tr><td>62</td><td>NumAuthorsInteracting_6</td><td>18.6645</td><td>1270.6856</td></tr>
    <tr><td>63</td><td>AverageDiscussionLength_0</td><td>63.2509</td><td>6774.5679</td></tr>
    <tr><td>64</td><td>AverageDiscussionLength_1</td><td>70.6479</td><td>7946.7211</td></tr>
    <tr><td>65</td><td>AverageDiscussionLength_2</td><td>67.6737</td><td>8715.1522</td></tr>
    <tr><td>66</td><td>AverageDiscussionLength_3</td><td>67.4370</td><td>7756.3079</td></tr>
    <tr><td>67</td><td>AverageDiscussionLength_4</td><td>76.2929</td><td>10164.9571</td></tr>
    <tr><td>68</td><td>AverageDiscussionLength_5</td><td>67.6255</td><td>7573.3868</td></tr>
    <tr><td>69</td><td>AverageDiscussionLength_6</td><td>75.8024</td><td>9396.7855</td></tr>
    <tr><td>70</td><td>NumDiscussions_0</td><td>12.6869</td><td>309.4407</td></tr>
    <tr><td>71</td><td>NumDiscussions_1</td><td>14.0969</td><td>406.4057</td></tr>
    <tr><td>72</td><td>NumDiscussions_2</td><td>14.5392</td><td>441.7513</td></tr>
    <tr><td>73</td><td>NumDiscussions_3</td><td>17.2149</td><td>815.9520</td></tr>
    <tr><td>74</td><td>NumDiscussions_4</td><td>18.6851</td><td>1043.8249</td></tr>
    <tr><td>75</td><td>NumDiscussions_5</td><td>17.3571</td><td>866.3266</td></tr>
    <tr><td>76</td><td>NumDiscussions_6</td><td>17.4848</td><td>863.5900</td></tr>
  </tbody>
</table>

We note that many of the features are heavily right skewed.

# Data Cleaning
There are no missing values in the dataset.



# Research Questions

Q1: Which features are highly predictive of the target?
The RandomForestRegressor was used to build 

Q2: How does time affect the target?
Q3: Which model is effective in predicting the target with the features?

# Conclusions