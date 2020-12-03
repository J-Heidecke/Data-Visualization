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

Police shootings have come into the limelight in recent years, especially in the USA. Even here in the UK, during the London Bridge Attack, the police had used guns to ensure the safety of the public and themselves. However, the police itself has come into scrutiny after the death of George Floyd. Though no firearm was used in his public murder, police violence and especially police shootings have been in the public light of America for a while. Thus, I decided to look at this issue. I have decided to specifically use police shootings because shootings have to be reported and are currently a much-debated topic.

I dedicated a part of this introduction to the topic of the problem of racism with is so intrinsically linked with the recent criticisms of the police.

### Racism and Guilt

Racism has become the most discussed political and social topic of recent years, especially in the USA. It sits amongst other social issues such as sexism, the political left classifies these as tools of oppression against marginalized people and minorities (though it would be more fitting to say against non-white, non-male, and non-heterosexual individuals according to them). Multiple groups perpetuate this mindset such as BLM and Antifa. These axioms are accepted by representatives of the Democratic party, most notably by the presidential candidate Joe Biden. The origin of this ideology can be traced back to a post-WW2 America, at universities who took in the Jewish refugees of the Frankfurt School.

The members were critics of Western Civilization directly experiencing the direct impact of Nazism and Fascism. One of their most famous/infamous contributions to history is the denazification of Germany. As a German myself, the impact of their experiment can be clearly felt to this day. The denazification can be best summed up as the collective guilt for WW2 bestowed upon the German people to eradicate the German cultural heritage (behavior, beliefs, ideas) because they were perceived (for good reason) as dangerous. This is probably best illustrated with an example. In Germany, the only glimpse remaining of the 2nd World War is guilt, we have no war heroes, we have national Remembrance Day for our fallen, they have been forgotten. Whereas, in the UK soldiers are celebrated and remembered. Thus, aggression (in a positive sense) and other masculine traits have been discouraged. The belief and practice of Norse rituals which had been popular after World War 1 had been abandoned ever since, and any sympathy for Thor, Odin, or Loki has been sympathy for the Nazi party. Furthermore, religion of any kind has been censored 28% is non-religious has been abandoned (though this is a European phenomenon). For a long time, certain books from authors such as Nietzsche were out of print or forbidden. This was done to discourage the development of German values.

Though this divergence into Germany's recent history seems to be acausal to the recent history of America and answering my research question, I would like the reader to have this in mind while going through my findings because I believe this same method is happening in America against the white population. All guilt of the slave trade, misogyny has been collectively associated with 'whiteness'. However, instead of using WW2 as the reasoning behind the attributed guilt, racism is used instead.

### Police Killings and BLM

In recent history, police killings in the USA have become a much-discussed topic in the public, reports reaching as far as Europe, and I am sure even further. Amidst the COVID-19 pandemic, this reached its boiling point spearheaded by the social movement of Black Lives Matter (BLM), though the group was originally founded in America in 2013 it has since expanded internationally. In recent months, it has become a symbol of the anti-racism sentiment that has engulfed the western nations in the past 10 years.

It has become almost intangible to discuss the overall sentiment of the left-leaning individual/political group without considering BLM. Most of these civil movements such as BLM, Antifa, and others seem to have the same objectives:

1. The reduction/abolition of racially motivated crimes against 'minorities'. (Even though it would be more accurate to say, non-white people)
2. The advocation of non-violent civil disobedience. (This is largely aimed towards global organizations and the government, more specifically it is representative of the law; the police.)
3. The elimination of oppression.

Through considerations axioms, these groups have concluded the concept of the abolition of the police force across the United States because they feel that police violence is specifically aimed at minorities, especially black people. Thus, being an oppressor of black people in America.

The presidential candidate Joe Biden (at the time of writing the result of the election is still uncertain) has expressed sympathy for the BLM movement, with the prospect of the implementation of the idea of police abolition seems relatively high I would like to investigate the validity of these statements. Is America's police intrinsically racist?

This movement has been exponentially accelerated by the tragic death of George Floyd who has inadvertently become the face of the fight against racism. This has led to mass protests and riots leading to looting and the burning of property much reminiscent of the London riots in 2011 and the Los Angeles riots following the death of Rodney King in 1992.

### Research Questions

What are the underlying conditions for police shootings in the US?

If there are any, how have they changed in recent years?

How are they linked to the latest rise of the BLM movement?

i.e. Is there any relation between victims of shooting and their race?

Are shootings more common in certain states/cities in the US?

Has the amount of police shootings changed over the last years?

Can it be determined that victims are shot in self-defense?

## Analysis Part 1 - Overview

Generally, an analysis moves from the general to specific. It allows us to zoom into specific features and evaluate them by referencing back to our understanding of the problem gained by the overview. I think this concept will apply well to this analysis.

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

#### Justification

##### Bar Chart

I thought that a bar chart was the best type of visualization to show this distribution. Other options would have been a pie chart, however, I thought that a pie chart might be too densely populated. Furthermore, it would only show the ratio of the distribution instead of showing the number of people shoot in each age group.

##### Tufte Approach

Since this is an overview, I thought the Tufte approach would be fitting, so that the raw distribution would be undisturbed by labels, colors, and other cosmetics. However, there are a few drawbacks this approach has. If I did not name, the title 'Age distribution' would a reader be able to figure out what this visualization is about? I do not believe so. Yet, given this information, anyone can figure out that the scale of the x-axis is age, and that the y-axis is the number of people killed.

Taking this approach, I have also decided against any interactivity. Even though interactivity encourages engagement with a visualization thus leading to a better understanding it would defeat the purpose of this visualization is Tufte.

Also, as per usual for a minimalist, I decided against any color (besides the standard blue) to let the data speak for itself.

##### Line

However, once I had the visualization in front of me, I thought it lacked a tangible scale of the sheer number of victims. Hence, I decided to draw a line on the y-axis to introduce relativity to this graph because for all the reader could know the maximum value on the y-axis was 10 instead of 1550. Why 1000? I thought the number 1000 in this context is quite intimidating since one would like this number to be as small as possible to minimize the loss of life, however, upon seeing this large number and noticing that two age groups are significantly above it the reader will hopefully grasp the true scale of the number of victims.

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

#### Justification

##### Color

The color of this pie chart is probably the most sensitive part of the visualization. To avoid any 'ranking' or scaling of the races and/or that some lives mean more than others. Furthermore, as mentioned extensively in the introduction, a point of discussion regarding this topic is racism, so to avoid any intrinsically racist statements, I avoided color schemes that would suggest any bias towards a race. I used a dark color scheme to emphasize the gravity of the situation. These charts represent the deaths of men and women. I looked at the standard color schemes, but I could not find one that satisfied my requirements, they were either too bright or had an intrinsic color scale. Hence, I used the greyscale which was the best compromise between seriousness, thoughtfulness, and distinguishability. However, I do have to admit that it is somewhat difficult to distinguish between races. However, it is a compromise I am willing to take.

Additionally, no matter what sort of color blindness a person may have, everyone can distinguish greys. I considered the 'inferno' color scheme (the same that the BBC used for its Covid-19 visualization), however, I think it does not have a mournful tone. It implies aggression and 'apocalypse' which is not the sentiment I would like to convey.

##### Pie Chart

As previously stated, I thought that a pie chart would be an ideal way of the proportion of the victim's race. However, I realized that this is the proportion of the entire data set. In one of my questions, I stated that I would like to discern the difference over time. For this that undertaking the pie chart is insufficient. I think the 'best' way of showing both the ratio and the change over time would be a normalized stacked area graph would be 'ideal' for this. I kept the color scheme consistent to show the link between the pie chart and the stack area chart. Furthermore, it does not show the number of police shootings only the ratio. However, since showing the actual numbers of victims in the previous visualization I thought it would not be necessary to show it again, rather focusing on the ratio.

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

#### Justification

##### Stacked Area

I wanted to create a visualization that both incorporates the ratio of the pie chart and the numbers of the bar chart. I thought that good methods of showing this would be either stacked area or its normalized form. However, I quickly chose stack area because the normalized version puts more emphasis on ratio and it would be a pie chart stretch out over the years, theoretically (without the circular shape).

Furthermore, another good type of graph would have been a bar chart, and it is what I initially intended to do, coming from the age bar chart. However, the white spaces between each bar made the visualization uneasy on the eyes. The stark white is a heavy contrast to the greys of the color scheme causing an uncomfortable dissonance. This harshness is eliminated because there are no gaps in an area graph.

However, this gives the illusion that the data (specifically the dates the shootings occur) is continuous which it is not, the dates are discrete. Thus, a reader could assume that shootings occur throughout the year every day of the month. Furthermore, I noticed that the color scheme in conjunction with this stacked area approach marginalizes the races other than white, black, or Hispanic. Therefore, I decided to separate each race into different rows to clarify the trends of each. This approach can be found below the justification.

##### Axes

I used date as the x-axis since I wanted to measure the change over the years. The y-axis is the aggregate count of these dates, since I thought it worked with the bar chart it would work here. I also tried using the column 'id' instead of date. However, it resulted in a different (false) graph because the id starts at 1 and ends at ca. 6000. The aggregate count would lead to a false graph because the ids were allocated according to date. Thus, even if there were the same number of shootings in Jan 2015 and Jan 2017 the aggregate count would be vastly different. Hence, I decided to use date because the difference between 2015 and 2017 is only 2, and more importantly, only 5 between 2015 and 2020. Whereas the difference in ID number between the first person shot in 2015 and the first person shot in 2020 is over 5000. Thus, the aggregate count should produce accurate results, and preserve the shape of the visualization.

##### Line

To make the analysis easier I decided to put a line on at the first data point. This serves the purpose of showing the change in the number of shootings over time. Without the line, it would be more difficult to perceive the changes. It holds no significant number value since the aggregate count is extremely high due to using 'date' for counting.

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

#### Insights

#### Justification

##### Circle plot

I used a circle plot because it would allow me to use the size encoding to show both male and female in the same bubble. A bar chart or area chart would separate them, and I think that would have been less effective. Using a circle plot the relative sizes (see more in Size) can be more effectively conveyed.

##### Axes

As this is meant to be a combination of the first two visualizations, combining both age, race, number of shooting victims, and as a new 'axis' gender I thought that having the positional differentiators (x and y) allowed the clear distinction between these two. I have age binned (pain []) because it classifies age groups instead of having each specific age take up a position on the x-axis which makes the graph look cleaner.

##### Size

I decided to code the aggregate count as size to visualize the number of shooting victims. The only disadvantage is the estimation of size. As Munzner discovered, the area is relatively good at conveying the properties. Humans vision is not optimized to estimate are which makes the task of judging the relative size of the circles in the plot difficult but not impossible. The relative differences are distinguishable if one focuses. This does not allow the reader to gain insight into the visualization at first glance as the very first visualization did.

I choose one as the exponent to represent the data as 'naturally' as possible. As discussed in lecture four, changing the exponent to a value such as 0.7 or 0.87 will make it look more visually pleasing, however, it distorts the data itself which leads to dishonesty. Especially, in an age where fake news and discussion of inclusiveness is prevalent not adjusting to these issues would be negligent of them. However, at closer examination an exponent such as 1.2 or 1.3 would make the ratio between the genders look more extreme which it is. The ratio is in the region of 1:10. Using an exponent of 1 makes this ratio look smaller.

##### Color

I decided to use blue and red to represent the genders. This is a conventional color scheme, however, I thought it would be fitting to not overload the visualization and keep it as minimalistic (Tufte's approach) to convey the information as cleanly and straightforward as possible.

##### Interaction

I added tooltip as an interaction so that the exact numbers can be examined by the user, giving more detailed insight into the exact ratios between the genders.

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

#### Justification

##### Pie Chart

I have chosen to make a pie chart to clarify the ratio rather than the sheer number of each level. I will explore the change over time in the visualization below.

##### Color

I have chosen the color scheme 'redgrey' to reflect the urgency and threat of death that looms over shootings. The police officers engaging in these shootings put their lives at risk as well. Naturally, red is connected to blood, and I wanted to reflect that in this visualization that indeed blood is spilled, tragically. However, I wanted to be able to distinguish between 'attack', 'other', and 'undetermined'. Hence, I found 'redgrey' to be more fitting than 'reds'. When I used 'reds', the different levels are somewhat difficult to distinguish. Thus, I thought someone who looked at the visualization was somewhat offput and confused by it. Moreover, I wanted a color scheme that could be perceived by people with color blindness, this scheme offers this.

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

#### Justification

Much of the justification has already been done for the 'Threat Level - Pie Chart' above regarding the color and 'Racial Disparity - Stacked Area' regarding the use of stacked area graph. Thus, for the sake of not repeating myself, I omitted these here. However, I will mention the reason for the omittance of a line. I thought that easier to make out in this stacked area graph than in the one above.

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

#### Justification

##### Normalized Stacked Area

I used the normalized stacked area graph instead of its stacked area cousin to clearly convey the ratio over time. The reader is already aware of the changes in the numbers from the previous stacked area graph, and that they stay roughly the same. Thus, I thought a pure emphasis on ratio would be more useful.

##### Color

The data behind this graph is easier to approach since it does not (directly) deal with the loss of life. Hence, I used a color scheme that could clearly show the different categories but remained 'serious' with slightly darker colors.

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

#### Justification

##### Axes

It was clear to me that I wanted to map 'threat_level' against 'arms_category'. However, I wanted to represent all the victims in the data set, hence, I used 'age' because I already examined the change in time in the previous graph. Another plausible option for the x-axis would have been 'id', however since there is 5000+ IDs the visualization would have been extremely large. However, there is an issue with the us of age, the plot does not truly show every data point because if a group of victims used the same weapon, had the same threat level, and were of the same age their respective bars overlap. Therefore, this visualization is not perfect, even though one can infer where the bars overlap as the margins between bars disappear creating a continuous bar. This could be fixed by increasing color saturation as the number of victims in a category increase.

#### Circle Plot

Initially, this plot was encoded as 'bar', however, it did not show the number of records correctly, hence I changed the it to 'circle' so that the size would represent the aggregate count.

##### Interaction

After mapping 'threat_level' and 'age', I didn't include 'arms_category' anywhere. Hence, I color-coded it, however, the result was not particularly satisfying because in ages where a certain category of weaponry dominated the bar took the color of it. Hence, to represent each data point it needed the ability to filter each category (see more in 'Interactive Legend').

Moreover, interaction allows the user to 'bond' with the visualization, the user has control over it, thus, creating a sense of ownership over the visualization, the user can transform the plot to their own needs (within limitations), and will therefore be more engaged with the visualization encouraging a deeper conversation with the data.

Shneiderman's criteria:

-**Overview**: The plot allows for an overview of the data, however, as previously mentioned not all the data is shown in the overview.

-**Zoom**: One cannot zoom into the visualization; however, it is not necessary to do so as all data can be shown without it using the filter.

-**Filter**: Categories can be filter in on-demand via the interactive legend.

-**Details-on-demand**: Other than 'age', 'arms_category', and 'threat_level' no details are given.

-**Relate**: One can infer the relationship between different categories by the number of bars present, however as previously mentioned due to the plot being imperfect this can not be done to the full extent.

-**History**: This is not supported; however, I think it is superfluous for this visualization.

-**Extract**: This is not supported but as with 'History' it is beyond the application of this plot.

##### Interactive Legend

I choose the interactive legend because it allows to filter the data in a controlled manner and display each arms category in a 'separate' window allowing for separation without taking up space.

Furthermore, it looks clean and is intuitive enough to be used easily, though it is not as intuitive as direct interaction. Yet, I believe it is a compromise between it and ease of use. The user can simply select the filter in the legend which hardly fails, whereas, with direct interaction when a user fails to click on the right field or misclicks frustration will occur when the interaction does not perform the desired command.

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

#### Justification

##### Circle Plot

As seen in previous visualization, I find the circle plot an effective method to discern between the number of records of different categories. And I thought that it would apply well here as well.

##### Colour and Size

With this visualization I wanted to investigate the ratio between fleeing and threat level, and I thought that a stacked bar chart would fit best to my plan. But then I thought I could add a little more to it and 'double-encoded' aggregate count as size to make the differnce in numbers more apparant to the viewer.

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

#### Justification

This a relativly simple visualization based on principles that I have explained in the previous visualization. To not repreat myself, I have omitted it here.

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

#### Justification

##### Choropleth vs Dot Map

I have decided to use a dot map rather than choropleth because as discussed in the lecture a choropleth map can lead to 'false' information and a 'false' view of the data, also a dot map allows for epicenter location. If I had used a choropleth map specific locations would not be highlighted and no conclusion could be drawn.

##### Colour

I have used a colour scheme so that the places with significantly more shootings are highlighted.

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

#### Justification

The visualization is meant to uncover the relationship between states and between cities within and outside their respective states

##### Circle plot

I have decided to use the circle plot once again because I think it is a good fit for double encoding. I had intended to double encode the aggregate count of shootings to emphazise them. I did so because if size or color where different attributes the plot becomes messy and could distract from the relationship I would like to discover with this visualization, with this method 'noise' is filtered out. This noise filtering could have been done with a different type of interactive visualization, perhaps, it could have led to a greater engagement with the plot at hand by the user. However, my intention is that the user discovers the different cities using 'maTooltip'. See more in the interaction section.

##### Double Encoding - Size and Color

I have double encoded size and color with the aggregate count because it make spotting the differences between the data points easier. It puts an emphisis on the number of shootings, which is at the heart of analysis. I have chosen the color red to represent the blood shed, this might seem an extreme measure, and suggests that the death of many is weighs more than the deaths of a few, but this is not my intention, I do not aim to pass judgement on the people involved in these shootings.

##### Interaction - maTooltip

The maTooltip allows the user to find out more information about the data point they hover over. In this visualization they will find the name of the city, the state the city is in, and the number of people shot in this city in the past five years. One can clearly find the bubbles that are biggest and find the name of the city and other information regarding it.

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

#### Justification

This visualization has the purpose of showing the relationship between the number of shootings per state against time. Other than the axis there is not much difference.

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

#### Justification

This graph is inteded to show the difference in race of shootings victims per state.

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
