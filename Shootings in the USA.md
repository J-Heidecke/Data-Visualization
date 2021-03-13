---
id: litvis

elm:
  dependencies:
    gicentre/elm-vegalite: latest
    gicentre/tidy: latest
---

```elm {l=hidden}
import Tidy exposing (..)
import VegaLite exposing (..)
```

# IN3030 - Data Visualization Coursework

## Introduction

Police shootings have come into the limelight in recent years, especially in the USA. Even here in the UK, during the London Bridge Attack, the police had used firearms to ensure the safety of the public and themselves. The police itself has come into scrutiny after the death of George Floyd. Though no firearm was used in his public murder, police violence and especially police shootings have been in the public light of America for a while. Thus, I decided to look at this issue. I have decided to specifically use police shootings because shootings have to be reported and are currently a much-debated topic.

### Research Questions

1. What are the underlying conditions for police shootings in the US?

1.1 If there are any, how have they changed in recent years?

1.2 How are they linked to the latest rise of the BLM movement?

1.3 i.e. Is there any relation between victims of shooting and their race?

2. Are shootings more common in certain states/cities in the US?

3. Has the amount of police shootings changed over the last years?

4. Can it be determined that victims are shot in self-defense?

## Analysis Part 1 - Overview
This analysis moves from the general to specific. This allows me to zoom into specific features and evaluate them individually.
I will split the analysis into different 'chapters' the first being the overview where I will investigate age distribution, gender, and racial disparity of shootings. Secondly, I will zoom into the circumstances of the shootings. Thirdly, I will look at the geography of the shootings.

### 1.1 Age Distribution - Bar Chart

The first overview I wanted to gain was the age distribution of the shootings.

```elm {l v}
age : Spec
age =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])
                << configuration
                    (coAxis
                        [ axcoTicks False
                        , axcoDomain False
                        , axcoLabelAngle 0
                        , axcoLabelPadding 0
                        ]
                    )

        enc =
            encoding
                << position X
                    [ pName "age"
                    , pBin []
                    , pAxis [ axTitle "" ]
                    ]
                << position Y
                    [ pAggregate opCount
                    , pAxis [ axTitle "", axValues (nums [ 1000 ]), axFormat "" ]
                    ]
    in
    toVegaLite
        [ width 600
        , height (600 / 1.618)
        , cfg []
        , data []
        , enc []
        , bar [ maFillOpacity 0.5 ]
        ]
```

#### Insights

It seems that most shooting victims are between the ages of 20 to 40, most of them being in their 30s. I am surprised that a significant number of victims are above 60. Tragically, there is one victim in the age range 0 to 10 and some in the age group 10 to 20. It looks quite like a normal distribution. I was quite shocked and decided to look him up in the data set. The boy's name was Jeremy Mardis, he was shot by two police officers in Louisiana. They have been sentenced to 40 years and 5 years in prison. More details: https://en.wikipedia.org/wiki/Shooting_of_Jeremy_Mardis.

### 1.2 Racial Disparity - Pie Chart

One of my questions is the relationship between race and victims of shootings. Initially, I thought a good way of showing this is using a pie chart. A pie chart is perfect at showing proportions.

```elm {l v interactive}
race : Spec
race =
    let
        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])

        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position Theta [ pName "id", pQuant ]
                << color
                    [ mName "race"
                    , mScale [ scScheme "greys" [] ]
                    ]
    in
    toVegaLite
        [ cfg [], data [], enc [], arc [ maInnerRadius 50 ] ]
```

#### Insights

The main talking point of BLM is the oppressive nature of the police against black people, saying that they are targeted in greater numbers compared to other ethnicities. However, I can find no evidence in the chart above, where it seems like white people are almost twice as likely to be killed by the police than black people. However, this is a quite general chart not considering the time frame, for it could be that police shootings have increased in recent years leading to the protests.

### 1.3 Racial Disparity over Time - Stacked Area

```elm {l v}
raceAndTime : Spec
raceAndTime =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X [ pName "date", pTimeUnit yearMonth, pAxis [ axTitle "", axFormat "" ] ]
                << position Y [ pName "date", pAggregate opSum, pTitle "Ratio", pAxis [ axTitle "", axValues (nums [ 109000000000000 ]), axFormat "" ] ]
                << color
                    [ mName "race"
                    , mTitle "Race"
                    , mScale [ scScheme "greys" [] ]
                    ]
    in
    toVegaLite [ width 600, data [], enc [], area [] ]
```

#### Insights

This visualization essentially shows the same as the pie chart above but stretched out over 5 years. One notices that the numbers stay roughly the same over the years. The line indicates the first entry date, and in recent years (mid-2018 onwards) it seems that the throughs are much lower, and the peaks are not much higher, however, there has not been much change. The spikes are usually highest around Jan except in 2019 when overall the numbers are rather low. There is a large dive in the numbers in Nov/Dec 2017, however, I believe this might be to a lack of data rather than good fortune because the numbers seem to be consistent which means it is unlikely that shootings will have dropped suddenly.

### 1.4 Gender Disparity - Circle Plot

```elm {l v interactive}
genderDisparity : Spec
genderDisparity =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])
                << configuration
                    (coAxis
                        [ axcoTicks False
                        , axcoDomain False
                        , axcoLabelAngle 0
                        , axcoLabelPadding 0
                        ]
                    )

        enc =
            encoding
                << position X
                    [ pName "age"
                    , pBin []
                    , pAxis [ axTitle "" ]
                    ]
                << position Y
                    [ pName "race"
                    , pAxis [ axTitle "" ]
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 3500 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mName "gender", mScale [ scScheme "set1" [], scReverse False ] ]
    in
    toVegaLite
        [ width 600
        , height (600 / 1.618)
        , cfg []
        , data []
        , enc []
        , circle [ maFillOpacity 0.5, maTooltip ttEncoding ]
        ]
```

## Analysis Part 2 - The Circumstances of Shootings

As mentioned above, I will now zoom into the details surrounding the shootings. I will look at the threat level of shootings as indicated by reports.

### 2.1 Threat Level - Pie Chart

```elm {l v}
threatLevel : Spec
threatLevel =
    let
        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])

        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position Theta [ pName "id", pQuant ]
                << color [ mName "threat_level", mScale [ scScheme "redgrey" [], scReverse False ] ]
    in
    toVegaLite
        [ cfg [], data [], enc [], arc [ maInnerRadius 50 ] ]
```

#### Insights

During my research for this project, it had come to my attention, that in many interviews, representatives of the movements that intend to 'defund' the police have stated that the police kills people according to their own will or to put it simply in cold blood. However, the chart above shows that roughly two-thirds of killings were responses to attacks. Skeptics would question if an officer who'd perform such an act would mark such an event as an attack to save himself from lawful prosecution, however, regarding the higher number of attacks it seems unlikely that this is the case.

### 2.2 Threat Level - Stacked Area

```elm {l v}
threatAndTime2 : Spec
threatAndTime2 =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X [ pName "date", pTimeUnit yearMonth, pAxis [ axTitle "", axFormat "" ] ]
                << position Y [ pName "date", pAggregate opSum, pTitle "Number of Victims", pAxis [ axTitle "", axValues (nums [ 0 ]), axFormat "" ] ]
                << color [ mName "threat_level", mTitle "Threat Level", mScale [ scScheme "redgrey" [], scReverse False ] ]
    in
    toVegaLite [ width 600, data [], enc [], area [] ]
```

#### Insights

I kept the color scheme consistent with the previous graph. The visualization shows that all threat levels have increased, however, attacks have severely increased. Especially, the last two years. What is the reason for this? Is it linked to the recent anti-police sentiment? Looking at sheer numbers one can understand the emotional response; the feeling of loss of a recently deceased family member, the fear of losing a family member, or being shot oneself. This is certainly different compared to Europe, especially the UK where the ordinary police force cannot carry firearms. In my home country of Germany, the number of police shootings is ca. 529 since 1952, the exact number of victims is unclear. In comparison, this is less than the number of victims in the USA in recent years.

A friend of my father's coincidentally is a policeman, and though he has undergone countless hours of training he stated once in a conversation that even with training and experience in a high threat level situation the brain short wires returns to a fight or flight response and takes any measure to protect itself. From personal experience as a martial artist, I can only but agree with his statement. In a situation when one is out of one's depth one reverts to the basic techniques to get out of that situation. Thus, I can understand that in a given situation when weapons, possibly firearms are involved a policeman would revert to fight or flight and protect himself and the public.

### 2.3 Ratio of Weapons Utilized - Normalized Stacked Area

```elm {l v}
typesOfAttack : Spec
typesOfAttack =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X [ pName "date", pTimeUnit yearMonth, pAxis [ axTitle "", axFormat "" ] ]
                << position Y [ pName "id", pAggregate opSum, pStack stNormalize, pTitle "Ratio" ]
                << color
                    [ mName "arms_category"
                    , mTitle "category of weapon"
                    , mScale [ scScheme "tableau20" [] ]
                    ]
    in
    toVegaLite [ width 600, data [], enc [], area [] ]
```

#### Insights

The graph above shows that assailants consistently use guns in their attacks. The second most used weapon group is sharp objects. The percentage of unarmed assailants is also consistent. From this data, it is unclear how the attackers used the weapons against the officers or other persons, or even if they used them at all. However, more and more weapons are being identified. The percentage of unknown weapons has decreased, this could indicate that the police has increased its effort to identify the threat before taking forceful action.

A trend surprising trend is the use of vehicles. They first appeared in late 2016 and have picked up from the beginning of 2018. Both the Nice truck terror attack and the Berlin truck Christmas market attack were in 2016. Could there be a link between these and the use of vehicles? Could these attacks have inspired the use of vehicles as a weapon? In 2017 a terror attack was committed using a car in Charlottesville, Virginia. Logistically, a vehicle is easier to organize and conceal than an explosive or a firearm. Thus, making it a 'safer' option out of the view of a person who would like to cause chaos and death.

### 2.4 Threat Level and Weapons Used - Interactive

As I finished the previous visualization, I thought that combining the threat level and the weapons used would help me gain further insight into the use of self-defense by officers. Combining the two would allow me to view what arms category were most likely to be used by attackers and which would cause the officer/s to act in a self-preserving manner.

```elm {l}
interactiveLegend : String -> String -> Spec
interactiveLegend field selName =
    let
        enc =
            encoding
                << position Y
                    [ pName field
                    , pAxis [ axTitle "", axDomain False, axTicks False ]
                    ]
                << color
                    [ mSelectionCondition (selectionName selName)
                        [ mName field, mScale [ scScheme "redgrey" [] ], mLegend [] ]
                        [ mStr "lightgrey" ]
                    ]

        sel =
            selection
                << select selName seMulti [ seEncodings [ chColor ] ]
    in
    asSpec [ sel [], enc [], square [ maSize 120, maOpacity 1 ] ]
```

```elm {l v interactive}
weaponsWithInteractiveLegend : Spec
weaponsWithInteractiveLegend =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        trans =
            transform
                << filter (fiSelection "legendSel")

        enc =
            encoding
                << position X
                    [ pName "age"
                    , pQuant
                    , pBin []
                    ]
                << position Y [ pName "threat_level", pNominal, pTitle "" ]
                << color
                    [ mName "arms_category"
                    , mTitle "arms category"
                    , mScale [ scScheme "tableau20" [] ]
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 1500 ]), scType scPow, scExponent 1 ]
                    ]

        chartSpec =
            asSpec [ height 150, width 600, trans [], enc [], circle [ maOpacity 0.8, maTooltip ttEncoding ] ]

        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])
    in
    toVegaLite
        [ cfg []
        , data []
        , hConcat [ chartSpec, interactiveLegend "arms_category" "legendSel" ]
        ]
```

#### Insights

In electrical devices, guns, multiple, others, and vehicles the ratio most people who used these had attacking intention. The attack column dominates the others in terms of numbers. Especially in guns (the largest category) though the number of others (I assume this includes non-attack behavior) is very high. In the other categories, the trends are not as clear, especially in the unknown, I think it has something to do with the fact that the weapon used is unknown and in a fight or flight situation, it is more difficult (than usual) to assess the situation correctly. Thus, depending on the personality of the office, he/she might be more trigger happy or more inclined to run away. Further, the number of attacks, other and undetermined is almost equal, I think this is due to the same reason. In the category’s blunt instruments, explosives, hand tools, piercing objects, sharp objects, and unarmed either the ratio between attack and other is almost equal or other dominates. It is difficult to judge the exact reasoning behind this pattern, but I suspect it is linked to the very nature of the type of weapon used. The police in the US are trained to be alert when a gun, knife, and other 'conventional' weapons such as hammers, axes, and so on are in play. However, when other weapons are used the officers might not be as accustomed to it as if they were with conventional weaponry.

### 2.5 Fleeing - Circle Plot

```elm {l v interactive}
flee : Spec
flee =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X
                    [ pName "threat_level"
                    , pNominal
                    , pAxis [ axTitle "" ]
                    ]
                << position Y
                    [ pName "flee"
                    , pNominal
                    , pAxis [ axTitle "" ]
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 5000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color
                    [ mName "flee"
                    , mScale [ scScheme "viridis" [], scReverse True ]
                    , mLegend []
                    ]
    in
    toVegaLite
        [ width 600
        , height (600 / 1.618)
        , enc []
        , data []
        , circle [ maOpacity 0.8, maTooltip ttEncoding ]
        ]
```

#### Insight

The visualization shows that most shooting victims do not flee, the majority of victims choose to attack, the motivation behind these attacks is unknown, it could be out of self-preservation because they feel threatened themselves, out of malice, or suicide by cop. There are an infinite amount of reasons why a person might attack. The question that I am trying to answer is if the policeman/woman acted in self-defense. Certainly, in these cases that could well be the case. However, a large group of people who do not flee are labeled as 'other', I think this includes peaceful behavior. If that is the case, then the police officers did not act in self-defense but out of other reasons. The motivation behind this will only be known to the officer in question, however, if I assume that someone who is aware of the consequences of using a deadly weapon will, and is trained in the use of said weapon will use is reasonably then there must have been a good intention for the officer to discharge his gun whether out of self-defense or not.

However, if I assume that the officer actsed with malevolent intent, and abused the authority that had been given to him by the state, then it is fair to say that the officer acted with intent to kill or seriously injure the person he had pointed his weapon at. Again, the psychological state of the officer will only be known to himself/herself and possibly the investigators. I think both have existed. For instance, in the case of Jeremy Mardis who I have mentioned at the very beginning of this report, the officer guilty of his murder acted in with malevolence, according the police report there was no reason for the officer to discharge his weapon but he did so anyways. As mentioned before, the exact reasoning behind the officers action is only known to him whether he commited them out of fear, anger, or malice is unknown.

Hence, the visualization is an indicator of how the circumstances of shootings. Highlighting both the victims's threat level and intention of escape. But, I believe every case has to be investigated individually.

A note regarding the 'undetermined' instances. It is the smallest of the three groups, and shows a trend towards younger poplution. I can only speculate what this means. It could be that younger people do not make their intentions known as the older population does.

### 2.6 Impact of Mental Illness

```elm {l v interactive}
mentalIllness : Spec
mentalIllness =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        cfg =
            configure
                << configuration (coView [ vicoStroke Nothing ])
                << configuration
                    (coAxis
                        [ axcoTicks False
                        , axcoDomain False
                        , axcoLabelAngle 0
                        , axcoLabelPadding 0
                        ]
                    )

        enc =
            encoding
                << position X
                    [ pName "threat_level"
                    , pNominal
                    , pAxis [ axTitle "" ]
                    ]
                << position Y
                    [ pName "signs_of_mental_illness"
                    , pAxis [ axTitle "Sign of Mental Illness" ]
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 3500 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color
                    [ mName "signs_of_mental_illness"
                    , mScale [ scScheme "darkred" [], scReverse False ]
                    , mLegend []
                    ]
    in
    toVegaLite
        [ width 600
        , height (600 / 1.618)
        , cfg []
        , data []
        , enc []
        , circle [ maTooltip ttEncoding ]
        ]
```

#### Insights

This visualization shows that roughly 1 in 5 shooting victims show a sign of mental illness, what kind of mental illness was not specified in the data set, however, this represents the prevalence of mental illness, 1 in 5 adults suffer from a mental disorder. Thus, this implies that shootings are representative of the US populations statistics.

## Analysis Part 3 - Geography of Shootings

The following visualization are all derivatives of each other. I have produced them to gain further insight and answer my research questions, however, they hold little value for justifications. Thus, I will justify the first visualization, and only point out the differences in the following ones.

### 3.1 Map of Shootings

```elm {v l interactive}
epicenters : Spec
epicenters =
    let
        boundaryData =
            dataFromUrl "https://cdn.jsdelivr.net/npm/vega-datasets@2.1/data/us-10m.json" [ topojsonFeature "states" ]

        shootingsData =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings_final.csv" []

        backdropSpec =
            asSpec [ boundaryData, geoshape [ maColor "black" ] ]

        proj =
            projection [ prType albersUsa ]

        enc =
            encoding
                << position Longitude [ pName "longitude_cities" ]
                << position Latitude [ pName "latitude_cities" ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 5000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mAggregate opCount, mScale [ scScheme "turbo" [], scReverse True ] ]

        overlaySpec =
            asSpec [ shootingsData, circle [ maOpacity 0.5, maTooltip ttEncoding ], enc [] ]
    in
    toVegaLite
        [ width 800, height 600, shootingsData, proj, layer [ backdropSpec, overlaySpec ] ]
```

#### Insights

Most shootings happen in 'epicenters' in the major cities of the US such as Los Angeles, Houston and Chicago. Overall, the shootings reflect the population distribution of the US, in the more densly populated states in the east and south most shootings seem to take place not just in cities but rurual areas, however, in fairly small proportion. I think that more smaller dots would be seen on the map if I had a list of the smallest of towns in the US which represent the large red bubble in the top left, these are all the places where I couldn't find a longitutude and latitude value.

### 3.2 Cities and Density of Shootings - Interactive Circle Plot

```elm {l v interactive}
citiesAndStates : Spec
citiesAndStates =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X [ pName "city", pNominal, pAxis [ axTitle "", axValues (nums [ 1000 ]), axFormat "" ] ]
                << position Y
                    [ pName "state"
                    , pNominal
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 6000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mAggregate opCount, mScale [ scScheme "reds" [] ] ]
    in
    toVegaLite [ width 600, data [], enc [], circle [ maFillOpacity 0.5, maTooltip ttEncoding ] ]
```

#### Insight

The discoveries of this are not particularly suprising. There is a clear trend that in the more populated areas of the USA the number of shooting victims is higher. Especially in metropolian areas such as Los Angeles, Phoenix, Las Vegas and Houston. The Los Angeles metroplitan area seems to be especially affected, places such as Long Beach contribute to that score. In general, the largest cities in each state are the most affected by police shootings, I suspect largely due to their large population.

Furthermore, the states with a higher population are suffering from more police shootings. California (CA), Texas (TX and Florida (FL) are the 1st, 2nd and 3rd largest states by population and they seem to have the most number of shootings. Whereas Wyoming (WY) and Vermont (VT) which are the 50th and 49th largest state by population barely have any shootings.

### 3.3 States and Time - Interactive Circle Plot

```elm {l v interactive}
statesAndTime : Spec
statesAndTime =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X
                    [ pName "date"
                    , pTimeUnit yearMonth
                    ]
                << position Y
                    [ pName "state"
                    , pNominal
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 1000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mAggregate opCount, mScale [ scScheme "reds" [] ] ]
    in
    toVegaLite [ width 600, data [], enc [], circle [ maFillOpacity 0.5, maTooltip ttEncoding ] ]
```

#### Insight

It seems that the number of shootings as diminished in some places, and increased in some. For instance, there seems to have been an epidemic of shootings in California (CA) from December 2014 to April 2016, the number of shootings has slowly decreased since then. However, there has been a slight increase in the other big states such as Florida and Texas and smaller states. As seen in previous visualizations in part two, such as 'Racial Disparity over Time' and 'Threat Level over Time' the number of shootings as hardly changed over the last five years.

### 3.4 Map of Vicitms sorted by Race

```elm {v l interactive}
epicentersRace : Spec
epicentersRace =
    let
        boundaryData =
            dataFromUrl "https://cdn.jsdelivr.net/npm/vega-datasets@2.1/data/us-10m.json" [ topojsonFeature "states" ]

        shootingsData =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings_final.csv" []

        backdropSpec =
            asSpec [ boundaryData, geoshape [ maColor "black" ] ]

        proj =
            projection [ prType albersUsa ]

        enc =
            encoding
                << position Longitude [ pName "longitude_cities" ]
                << position Latitude [ pName "latitude_cities" ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 5000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mName "race", mScale [ scScheme "turbo" [], scReverse False ] ]

        overlaySpec =
            asSpec [ shootingsData, circle [ maOpacity 0.5, maTooltip ttEncoding ], enc [] ]
    in
    toVegaLite
        [ width 800, height 600, shootingsData, proj, layer [ backdropSpec, overlaySpec ] ]
```

### 3.5 States And Race - Interactive Circle Plot

```elm {l v interactive}
statesAndRace : Spec
statesAndRace =
    let
        data =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings.csv"

        enc =
            encoding
                << position X
                    [ pName "race"
                    , pNominal
                    ]
                << position Y
                    [ pName "state"
                    , pNominal
                    ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 5000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mAggregate opCount, mScale [ scScheme "reds" [] ] ]
    in
    toVegaLite [ width 600, data [], enc [], circle [ maFillOpacity 0.5, maTooltip ttEncoding ] ]
```

#### Insight

As shown in the 'race disparity' visualizations this plot indicates that the majority of people who are shot in the US are of white ethnicity. Thus, I find that the claim of BLM movement that the police force is intrinsically racist to be false. I think if anything these plots show that the ethnicity of the victim depends on the suburb, city, and state the victims was shot in. Most shooting victims are white because the US is 60% White, 18.5% Hispanic, and 13.4% Black, these visualizations reflect that demographic. To make a more specific example, most victims that are Hispanic are shot in states that are close to the border to Mexico. California, Texas, New Mexico, and Arizona have the highest number of Hispanic victims, being the bordering states, these states have a high Hispanic population.

### 3.6 Map of Vicitms sorted by Gender

```elm {v l interactive}
epicentersGender : Spec
epicentersGender =
    let
        boundaryData =
            dataFromUrl "https://cdn.jsdelivr.net/npm/vega-datasets@2.1/data/us-10m.json" [ topojsonFeature "states" ]

        shootingsData =
            dataFromUrl "https://j-heidecke.github.io/hostingdata/shootings_final.csv" []

        backdropSpec =
            asSpec [ boundaryData, geoshape [ maColor "black" ] ]

        proj =
            projection [ prType albersUsa ]

        enc =
            encoding
                << position Longitude [ pName "longitude_cities" ]
                << position Latitude [ pName "latitude_cities" ]
                << size
                    [ mAggregate opCount
                    , mScale
                        [ scRange (raNums [ 0, 5000 ]), scType scPow, scExponent 1 ]
                    , mLegend []
                    ]
                << color [ mName "gender", mScale [ scScheme "set1" [], scReverse False ] ]

        overlaySpec =
            asSpec [ shootingsData, circle [ maOpacity 0.5, maTooltip ttEncoding ], enc [] ]
    in
    toVegaLite
        [ width 800, height 600, shootingsData, proj, layer [ backdropSpec, overlaySpec ] ]
```

## Analysis Part 4 - Conclusion

### Answers to Research Questions

-**What are the underlying conditions for police shootings in the US?**

Most of the shootings take place when the victim is armed, most of the time with a firearm, and attacks the police officer with said weapon. It is likely that a firefight ensues. It would be of interest to compare these numbers and the numbers of police officer killed/injured while on duty. I would not be suprised if these numbers were causally linked.

Most individuals that are shot are aged between 20 and 40 and most vicitms are men. This could possibly linked to another statistic which showed that most prisoners are men and most people who commit crimes are male (in the US). The reasons behind this are diverse and cannot be summarized in this short paragraph.

-**If there are any, how have they changed in recent years?**

Overall, there has been little to now change, however, the use of vehicles as a weapon has increased significantly, in recent years. The motivations behind this sharp increase is unclear but I imagine it could be linked to the use of vehicles in terror attacks serving as inspiration for imitators.

-**How are they linked to the latest rise of the BLM movement? Is there any relation between victims of shooting and their race?**

The victim's race as far as I was able to analyze in this investigation is influenced by the demographic of a state, and by the demographic of the US itself. The ratio between the victim's race is almost identical to the ratio between the population of each race in the US. Thus, the rise of the BLM cannot be due to the number of shootings but rather other reasons, as mentioned in the introduction, the brutal murder of George Floyd. It is based on an understandable emotional response rather than data. However, the 'peaceful' emotions of loss and sadness were quickly overtaken by rage and anger towards the police force and the government itself, an offensive that led to a counter-attack on the BLM movement, questioning the validitiy of its purpose and mission. Personally, I think that these numbers are scary, over 1000 men and women are killed each year.

-**Are shootings more common in certain states/cities in the US?**

Yes, shootings are more common in states/cities that are more populated. Most shootings take place in urban/metropolitan areas.

-**Has the number of police shootings changed over the last years?**

The number of plice shootings has stayed fairly constant over the last five years. The ratio between the races has as well. There was no change in weapons employed either. However, in some states such as California the number of shootings has diminished in recent years in comparison to 2014 and 2015, on the other hand, the number of shootings in other states such as Florida has increased during the same time frame.

-**Can it be determined that victims are shot in self-defense?**

I could not accuratly determine the if the victims were shot in self-defense because I was lacking enough information regarding the shootings. However, a large proportion of vicitms attack the officer, hence, I would assume that a large proportion of these incidencts are self-defense.
