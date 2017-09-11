from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_90",           # 01, 1
        "Function_2_B8",           # 02, 2
        "Function_3_D9",           # 03, 3
        "Function_4_13F",          # 04, 4
        "Function_5_16D",          # 05, 5
        "Function_6_19A",          # 06, 6
        "Function_7_1C6",          # 07, 7
        "Function_8_220",          # 08, 8
        "Function_9_26D",          # 09, 9
        "Function_10_2BD",         # 0A, 10
        "Function_11_2FB",         # 0B, 11
        "Function_12_345",         # 0C, 12
        "Function_13_3AC",         # 0D, 13
        "Function_14_3D9",         # 0E, 14
        "Function_15_40A",         # 0F, 15
        "Function_16_433",         # 10, 16
        "Function_17_475",         # 11, 17
        "Function_18_4E4",         # 12, 18
        "Function_19_54A",         # 13, 19
        "Function_20_5C5",         # 14, 20
        "Function_21_631",         # 15, 21
        "Function_22_67A",         # 16, 22
        "Function_23_6AF",         # 17, 23
        "Function_24_6F2",         # 18, 24
        "Function_25_73E",         # 19, 25
        "Function_26_7D5",         # 1A, 26
        "Function_27_800",         # 1B, 27
        "Function_28_869",         # 1C, 28
        "Function_29_8ED",         # 1D, 29
        "Function_30_950",         # 1E, 30
        "Function_31_9BE",         # 1F, 31
        "Function_32_A2C",         # 20, 32
        "Function_33_A82",         # 21, 33
        "Function_34_B11",         # 22, 34
        "Function_35_B35",         # 23, 35
        "Function_36_BBB",         # 24, 36
        "Function_37_D2F",         # 25, 37
        "Function_38_DFB",         # 26, 38
        "Function_39_E25",         # 27, 39
        "Function_40_EB8",         # 28, 40
        "Function_41_EDE",         # 29, 41
        "Function_42_1038",        # 2A, 42
        "Function_43_1212",        # 2B, 43
        "Function_44_1301",        # 2C, 44
        "Function_45_15EB",        # 2D, 45
        "Function_46_19AC",        # 2E, 46
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "I hope the match starts soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_0_66 end

    def Function_1_90(): pass

    label("Function_1_90")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "Can't wait to see who wins!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_1_90 end

    def Function_2_B8(): pass

    label("Function_2_B8")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "This is so exciting!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_B8 end

    def Function_3_D9(): pass

    label("Function_3_D9")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        (
            "My excitement got the better of\x01",
            "me, and I showed up waaaaaaaaay\x01",
            "earlier than I needed to.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_D9 end

    def Function_4_13F(): pass

    label("Function_4_13F")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "Who should I cheer for this year?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_13F end

    def Function_5_16D(): pass

    label("Function_5_16D")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "Time for the final round! WOOOO!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_16D end

    def Function_6_19A(): pass

    label("Function_6_19A")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "Crap, I forgot my orbal camera!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_19A end

    def Function_7_1C6(): pass

    label("Function_7_1C6")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        (
            "Wait, so the Royal Guardsmen\x01",
            "aren't in the tournament this\x01",
            "year?! That sucks!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1C6 end

    def Function_8_220(): pass

    label("Function_8_220")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        (
            "This team battle thing is more\x01",
            "interesting than I'd anticipated.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_220 end

    def Function_9_26D(): pass

    label("Function_9_26D")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        (
            "It's all about the border patrol\x01",
            "team. They're gonna win, for sure!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_26D end

    def Function_10_2BD(): pass

    label("Function_10_2BD")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        (
            "What do you think today's match-ups\x01",
            "will be like?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_2BD end

    def Function_11_2FB(): pass

    label("Function_11_2FB")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "Two bracer teams remain...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Go for the gold, both of you!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_2FB end

    def Function_12_345(): pass

    label("Function_12_345")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        (
            "Those Special Ops guys are creepy...\x01",
            "but they've got it goin' on strength-\x01",
            "wise, for sure!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_345 end

    def Function_13_3AC(): pass

    label("Function_13_3AC")

    TalkBegin(0xFE)

    ChrTalk(    #14
        0xFE,
        "Just hurry up and start already!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3AC end

    def Function_14_3D9(): pass

    label("Function_14_3D9")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "I've been waiting for this all\x01",
            "year!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_3D9 end

    def Function_15_40A(): pass

    label("Function_15_40A")

    TalkBegin(0xFE)

    ChrTalk(    #16
        0xFE,
        "Championship today! WOOOOOO!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_40A end

    def Function_16_433(): pass

    label("Function_16_433")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        "I wonder who'll win...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "It's going to be amazing!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_433 end

    def Function_17_475(): pass

    label("Function_17_475")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        (
            "I like that blond boy on the\x01",
            "bracer team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "He looks laid back, but he's\x01",
            "got such a quick draw!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_475 end

    def Function_18_4E4(): pass

    label("Function_18_4E4")

    TalkBegin(0xFE)

    ChrTalk(    #21
        0xFE,
        (
            "I want to see the masked guy\x01",
            "and the big guy go at it head-\x01",
            "to-head. That'd be something!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4E4 end

    def Function_19_54A(): pass

    label("Function_19_54A")

    TalkBegin(0xFE)

    ChrTalk(    #22
        0xFE,
        (
            "Everybody came super-early because it's\x01",
            "the finals. Guess they figured seats\x01",
            "would fill up fast. And they did!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_54A end

    def Function_20_5C5(): pass

    label("Function_20_5C5")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0xFE,
        (
            "Two first-year teams making it\x01",
            "to the finals...and both poised\x01",
            "to win it all! Which will it be?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_5C5 end

    def Function_21_631(): pass

    label("Function_21_631")

    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        (
            "There's a girl on the bracer team,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Good for her!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_631 end

    def Function_22_67A(): pass

    label("Function_22_67A")

    TalkBegin(0xFE)

    ChrTalk(    #26
        0xFE,
        (
            "On with the show, ya' whipper-\x01",
            "snappers!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_67A end

    def Function_23_6AF(): pass

    label("Function_23_6AF")

    TalkBegin(0xFE)

    ChrTalk(    #27
        0xFE,
        (
            "Grandpa and I love watching\x01",
            "the tournament every year.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_6AF end

    def Function_24_6F2(): pass

    label("Function_24_6F2")

    TalkBegin(0xFE)

    ChrTalk(    #28
        0xFE,
        (
            "I was so excited for today's events,\x01",
            "I couldn't sleep one wink!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_6F2 end

    def Function_25_73E(): pass

    label("Function_25_73E")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "I really think the Special Ops\x01",
            "team is a shoe-in this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I mean, just the name 'Special\x01",
            "Ops' alone has such an awesome\x01",
            "ring to it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_73E end

    def Function_26_7D5(): pass

    label("Function_26_7D5")

    TalkBegin(0xFE)

    ChrTalk(    #31
        0xFE,
        "I'm gonna shout myself hoarse!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_7D5 end

    def Function_27_800(): pass

    label("Function_27_800")

    TalkBegin(0xFE)

    ChrTalk(    #32
        0xFE,
        "I'll be cheering for the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "They're always there to help when\x01",
            "people are in need.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_800 end

    def Function_28_869(): pass

    label("Function_28_869")

    TalkBegin(0xFE)

    ChrTalk(    #34
        0xFE,
        (
            "Maybe I should have packed a\x01",
            "lunch today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I was in line from such an ungoddessly\x01",
            "hour, I'm already hungry again...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_869 end

    def Function_29_8ED(): pass

    label("Function_29_8ED")

    TalkBegin(0xFE)

    ChrTalk(    #36
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "is always so much fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Every year, I get so INTO it!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_8ED end

    def Function_30_950(): pass

    label("Function_30_950")

    TalkBegin(0xFE)

    ChrTalk(    #38
        0xFE,
        (
            "That boy on the bracer team\x01",
            "looks about as old as my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I think I'll cheer for them today.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_950 end

    def Function_31_9BE(): pass

    label("Function_31_9BE")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        (
            "If teamwork is the deciding factor,\x01",
            "then Special Ops have the champion-\x01",
            "ship in the bag for sure.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_9BE end

    def Function_32_A2C(): pass

    label("Function_32_A2C")

    TalkBegin(0xFE)

    ChrTalk(    #41
        0xFE,
        (
            "I would've never predicted the\x01",
            "match-ups to go in the direction\x01",
            "they did.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_A2C end

    def Function_33_A82(): pass

    label("Function_33_A82")

    TalkBegin(0xFE)

    ChrTalk(    #42
        0xFE,
        "Royal Army vs. Bracer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Both of them fight to protect people as\x01",
            "part of their jobs. Now...I guess we see\x01",
            "who's better at it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_A82 end

    def Function_34_B11(): pass

    label("Function_34_B11")

    TalkBegin(0xFE)

    ChrTalk(    #44
        0xFE,
        "Time to start cheering!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_B11 end

    def Function_35_B35(): pass

    label("Function_35_B35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(    #45
        0x2F,
        (
            "#600FI haven't watched the Martial\x01",
            "Arts Competition since I was\x01",
            "a young man.\x02\x03",

            "Good luck out there, you two!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB7")

    TalkEnd(0xFE)
    Return()

    # Function_35_B35 end

    def Function_36_BBB(): pass

    label("Function_36_BBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C72")

    ChrTalk(    #46
        0xFE,
        (
            "I heard your opponents are really\x01",
            "tough...but you guys should be able\x01",
            "to take 'em, no sweat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "We'll be screaming ourselves hoarse\x01",
            "for you, so go knock 'em dead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2B")

    label("loc_C72")

    OP_A2(0x4)

    ChrTalk(    #48
        0xFE,
        "Hey, newbies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Your opponents are tough, but\x01",
            "you guys should be able to take\x01",
            "'em, no sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Break a leg out there. We'll be\x01",
            "cheering for you like you wouldn't\x01",
            "believe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2B")

    TalkEnd(0xFE)
    Return()

    # Function_36_BBB end

    def Function_37_D2F(): pass

    label("Function_37_D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(    #51
        0xFE,
        (
            "Listen, just relax and do what\x01",
            "you've always done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "There's no pressure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_D8E")

    OP_A2(0x3)

    ChrTalk(    #53
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Listen, just relax and do what\x01",
            "you've always done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "There's no pressure.\x02",
    )

    CloseMessageWindow()

    label("loc_DF7")

    TalkEnd(0xFE)
    Return()

    # Function_37_D2F end

    def Function_38_DFB(): pass

    label("Function_38_DFB")

    TalkBegin(0xFE)

    ChrTalk(    #56
        0xFE,
        "I hope the match starts soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_DFB end

    def Function_39_E25(): pass

    label("Function_39_E25")

    TalkBegin(0xFE)

    ChrTalk(    #57
        0xFE,
        (
            "I got up extra-early today so\x01",
            "I could rouse these two and get\x01",
            "some good seats at the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "I'd never miss a spectacle like this!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_E25 end

    def Function_40_EB8(): pass

    label("Function_40_EB8")

    TalkBegin(0xFE)

    ChrTalk(    #59
        0xFE,
        "Who'll win, do you think?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_EB8 end

    def Function_41_EDE(): pass

    label("Function_41_EDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_EEB")
    Jump("loc_1034")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_EF5")
    Jump("loc_1034")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_EFF")
    Jump("loc_1034")

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_F09")
    Jump("loc_1034")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(    #60
        0xFE,
        (
            "I was gonna camp out to get\x01",
            "some good seats, but the night\x01",
            "patrol made me go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "So, I did the only sensible thing. I snuck out\x01",
            "of the house, hid in my bushes, and waited for\x01",
            "the soldiers to leave. Then bam...line city!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1034")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1005")
    Jump("loc_1034")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_100F")
    Jump("loc_1034")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1019")
    Jump("loc_1034")

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1023")
    Jump("loc_1034")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_102D")
    Jump("loc_1034")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1034")

    label("loc_1034")

    TalkEnd(0xFE)
    Return()

    # Function_41_EDE end

    def Function_42_1038(): pass

    label("Function_42_1038")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1045")
    Jump("loc_120E")

    label("loc_1045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_104F")
    Jump("loc_120E")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1059")
    Jump("loc_120E")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1063")
    Jump("loc_120E")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(    #62
        0xFE,
        (
            "My husband went through a lot to\x01",
            "get us some good seats yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I can't believe he went through\x01",
            "all of that just for me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_10FD")
    Jump("loc_120E")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(    #64
        0xFE,
        (
            "Today, he lined up just as early\x01",
            "as he did yesterday...but all the\x01",
            "best seats were already taken!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "He'll just have to try harder\x01",
            "tomorrow. The early bird gets\x01",
            "the worm, as they say!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11D0")
    Jump("loc_120E")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_11FD")

    ChrTalk(    #66
        0xFE,
        "It's that time of year again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1207")
    Jump("loc_120E")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_120E")

    label("loc_120E")

    TalkEnd(0xFE)
    Return()

    # Function_42_1038 end

    def Function_43_1212(): pass

    label("Function_43_1212")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_121F")
    Jump("loc_12FD")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1229")
    Jump("loc_12FD")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1233")
    Jump("loc_12FD")

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_123D")
    Jump("loc_12FD")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_12C4")

    ChrTalk(    #67
        0xFE,
        (
            "We're all here to root for you\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "You're representing the Bracer\x01",
            "Guild out there. So be sure to\x01",
            "make us proud!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FD")

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_12CE")
    Jump("loc_12FD")

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_12D8")
    Jump("loc_12FD")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12E2")
    Jump("loc_12FD")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_12EC")
    Jump("loc_12FD")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_12F6")
    Jump("loc_12FD")

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_12FD")

    label("loc_12FD")

    TalkEnd(0xFE)
    Return()

    # Function_43_1212 end

    def Function_44_1301(): pass

    label("Function_44_1301")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1506")
    OP_A2(0x633)

    ChrTalk(    #69
        0x23,
        (
            "#151FHeeey! Esteeeelle!\x02\x03",

            "You did it! The fiinaaal fiiiight!\x02\x03",

            "It's soooo exciiiiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#506FDeep breaths, Dorothy. Come\x01",
            "on now, do it with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#010FIf you don't relax and keep yourself\x01",
            "still and focused, you won't be able\x01",
            "to get any good shots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x23,
        (
            "#150FOh, don't you worry about THAT.\x02\x03",

            "I take my best pictures when\x01",
            "I'm all hyped up like this!\x02\x03",

            "They're more natural, you see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        "#019FOh. I...guess they would be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#007FDorothy...I think you're some\x01",
            "kind of savant or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_1506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(    #75
        0x110,
        (
            "#151FOoh, stop flattering me. Now\x01",
            "come on, show me whatcha' got!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_15E7")

    ChrTalk(    #76
        0x110,
        (
            "#150FIt shouldn't be hard to get good\x01",
            "shots of you, what with these super-\x01",
            "awesome press seats!\x02\x03",

            "Better keep my camera at the ready!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E7")

    TalkEnd(0x23)
    Return()

    # Function_44_1301 end

    def Function_45_15EB(): pass

    label("Function_45_15EB")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1939")
    OP_A2(0x632)

    ChrTalk(    #77
        0x22,
        "#130FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#004FProfessor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#014FYou came to watch us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x22,
        (
            "#130FBut of course! You've always\x01",
            "been such a big help to me.\x02\x03",

            "I owe you two at least THAT much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#001FThanks, Professor!\x02\x03",

            "#006FBut...how'd you scrape together\x01",
            "the mira for a ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x22,
        (
            "#130FWell, that was a bit of a lucky\x01",
            "break on my part, actually.\x02\x03",

            "The museum director had some\x01",
            "sudden business to attend to,\x01",
            "so he couldn't make it today.\x02\x03",

            "And I am here in his stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#506FHa! Should have guessed you'd\x01",
            "never be able to get in here\x01",
            "out of your OWN pocket!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x22,
        (
            "#130FHa! Not that I wouldn't try, of\x01",
            "course. I'm sure I could find a\x01",
            "way, if I put my mind to it...\x02\x03",

            "At any rate, I am here, and here\x01",
            "I am. And I'll be shouting your\x01",
            "names for sure.\x02\x03",

            "Knock 'em dead, you two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#006FYou bet we will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#010FThank you, Professor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A8")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(    #87
        0x22,
        (
            "#130FI am here, and here I am. And\x01",
            "I'll be shouting your names for\x01",
            "sure.\x02\x03",

            "Knock 'em dead, you two!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A8")

    TalkEnd(0x22)
    Return()

    # Function_45_15EB end

    def Function_46_19AC(): pass

    label("Function_46_19AC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202D")
    OP_A2(0x634)
    OP_8C(0xC, 90, 0)

    ChrTalk(    #88
        0xC,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#004FIs something wrong, Kurt?\x02",
    )

    CloseMessageWindow()
    OP_9E(0xC, 0xF, 0x0, 0x12C, 0xFA0)
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #90
        0xC,
        "Hmm? Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "Guess it's time for the final match.\x01",
            "Give it all you've got, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#006FYou bet!\x02\x03",

            "#505F...You don't look so good there,\x01",
            "Kurt. Are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        "#012FYou do seem pale.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xC,
        (
            "Nah, just a little light-headed,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xC,
        (
            "Though it's kind of odd...I don't\x01",
            "feel sick, so why am I light-headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        "I think I'm having...a flashback...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#580FFlashback? From what, yesterday?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "No, no, no. From an accident I had\x01",
            "about three months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xC,
        (
            "Seems I screwed up on a job and\x01",
            "messed myself up pretty bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#505FWhat do you mean, 'seems'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#012FYou don't mean...amnesia, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xC,
        (
            "I do. It's kind of embarrassing, and perhaps\x01",
            "even a bit cliched...but, I actually don't\x01",
            "remember a thing about it. Or didn't, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        (
            "I still can't even remember what\x01",
            "job I was doing that got me hurt\x01",
            "in the first place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xC,
        (
            "The doctor said it wasn't shock or\x01",
            "anything, but offered no other explanations\x01",
            "as to what it could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#003FWow, what a story...\x02\x03",

            "#002FBut you were still okay to\x01",
            "participate in the match,\x01",
            "even in that condition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        (
            "I told you, physically there\x01",
            "isn't a thing wrong with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "In fact...I'm feeling a lot better\x01",
            "just talking it over with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "And in time, these flashbacks will start to\x01",
            "take shape, and I'll remember what happened.\x01",
            "So don't worry about me, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#505FUh, okay, I guess...if you say so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        (
            "#010FYou are starting to look a little\x01",
            "better than you did a minute ago.\x02\x03",

            "Just be careful, though, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        "You guys too. Good luck out there.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    Jump("loc_2072")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2072")

    ChrTalk(    #114
        0xFE,
        (
            "You've got to fight hard enough\x01",
            "for me, too, you got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2072")

    TalkEnd(0xC)
    Return()

    # Function_46_19AC end

    SaveToFile()

Try(main)
