from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0601   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0601.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
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
        'Private Selbourne',                    # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = -940,
        Z                   = 7250,
        Y                   = -94770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_D3",           # 01, 1
        "Function_2_E6",           # 02, 2
        "Function_3_FC",           # 03, 3
        "Function_4_120",          # 04, 4
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Return()

    # Function_0_D2 end

    def Function_1_D3(): pass

    label("Function_1_D3")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFD7790, 0x30012)
    Return()

    # Function_1_D3 end

    def Function_2_E6(): pass

    label("Function_2_E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_E6")

    label("loc_FB")

    Return()

    # Function_2_E6 end

    def Function_3_FC(): pass

    label("Function_3_FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11F")
    OP_8D(0xFE, -3140, -97580, 1480, -73120, 3000)
    Jump("Function_3_FC")

    label("loc_11F")

    Return()

    # Function_3_FC end

    def Function_4_120(): pass

    label("Function_4_120")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D6")

    ChrTalk(    #0
        0xFE,
        (
            "When I was standing guard here\x01",
            "before, I could have sworn I saw\x01",
            "a little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "But when I rubbed my eyes and\x01",
            "looked again, she was nowhere\x01",
            "to be found.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF")

    label("loc_1D6")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "When I was standing guard here\x01",
            "before, I could have sworn I saw\x01",
            "a little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "But when I rubbed my eyes and\x01",
            "looked again, she was nowhere\x01",
            "to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I wonder if I'm running on too\x01",
            "little sleep...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF")

    Jump("loc_14D5")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_38D")

    ChrTalk(    #5
        0xFE,
        (
            "Today is the finals for the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I should have guessed that the\x01",
            "Special Ops Unit would make it\x01",
            "to the final round...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Though I don't want to admit it,\x01",
            "they're a tough bunch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46A")

    ChrTalk(    #8
        0xFE,
        (
            "Starting today, the number of times\x01",
            "I'll need to patrol has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Though we haven't received any information,\x01",
            "I can only imagine that those responsible\x01",
            "for the terrorist acts haven't been caught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_54C")

    ChrTalk(    #10
        0xFE,
        (
            "The Erbe Scenic Route is surrounded\x01",
            "by beautiful greenery and is normally\x01",
            "the perfect spot for a stroll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "However, all I can see now are leafy\x01",
            "thickets that could be hiding the\x01",
            "terrorist criminals...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_664")

    label("loc_54C")

    OP_A2(0x0)

    ChrTalk(    #12
        0xFE,
        (
            "The Erbe Scenic Route is surrounded\x01",
            "by beautiful greenery and is normally\x01",
            "the perfect spot for a stroll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "And the area is considered a park\x01",
            "for the citizens of Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "However, all I can see now are leafy\x01",
            "thickets that could be hiding the\x01",
            "terrorist criminals...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_664")

    Jump("loc_14D5")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_74A")

    ChrTalk(    #15
        0xFE,
        (
            "I haven't seen any of the Royal Guard in\x01",
            "the area, so I could say that things here\x01",
            "are pretty peaceful at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "But I'm sure those standing guard\x01",
            "in the Royal City are under a lot\x01",
            "of stress right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 1)), scpexpr(EXPR_END)), "loc_89B")

    ChrTalk(    #17
        0xFE,
        (
            "Because of the size of this place,\x01",
            "patrolling it is one of the biggest\x01",
            "challenges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Since all of the tourists are concentrated\x01",
            "in the Royal City at the moment, this\x01",
            "place is a bit more relaxed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If one of the terrorists were among\x01",
            "the tourists, we'd have no real way\x01",
            "of knowing. It's a little scary!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB9")

    label("loc_89B")

    OP_A2(0x6E9)

    ChrTalk(    #20
        0xFE,
        (
            "Good work making it all the\x01",
            "way up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I'll give you this as a souvenir.\x01",
            "Ha ha, don't mind that it's a\x01",
            "hand-me-down from me.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21A, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x07\x00Received \x07\x02Carnelia - Chapter 9\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #23
        0xFE,
        (
            "Because of the size of this place,\x01",
            "patrolling it is one of the biggest\x01",
            "challenges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Since all of the tourists are concentrated\x01",
            "in the Royal City at the moment, this\x01",
            "place is a bit more relaxed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "If one of the terrorists were among\x01",
            "the tourists, we'd have no real way\x01",
            "of knowing. It's a little scary!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB9")

    Jump("loc_14D5")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_B48")

    ChrTalk(    #26
        0xFE,
        (
            "The airliners usually pass directly\x01",
            "overhead, but not today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I guess the rumor that all flights\x01",
            "were canceled was true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(    #28
        0xFE,
        (
            "I guess it's about time for\x01",
            "my shift replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "The cool air inside feels so\x01",
            "good after spending a day out\x01",
            "here standing guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "All right, maybe I'll have a drink\x01",
            "down in the mess hall for the\x01",
            "first time in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAC")
    OP_A2(0x0)

    ChrTalk(    #31
        0xFE,
        (
            "Scholars and others sometimes\x01",
            "come to investigate this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It seems they're interested because\x01",
            "this place is actually an ancient\x01",
            "ruin from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I guess people into old places just\x01",
            "can't resist coming here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Can't really see the appeal myself. It's not\x01",
            "a treasure trove of knowledge so much as it\x01",
            "is a workplace for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E93")

    label("loc_DAC")


    ChrTalk(    #35
        0xFE,
        (
            "Scholars sometimes come to\x01",
            "investigate this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "It seems they're interested because\x01",
            "this place is actually an ancient\x01",
            "ruin from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I wonder if people interested in old\x01",
            "places just can't resist coming here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E93")

    Jump("loc_14D5")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CB")
    OP_A2(0x0)

    ChrTalk(    #38
        0xFE,
        (
            "Not too long ago, my only\x01",
            "daughter came to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "When I told her this is where\x01",
            "I worked, she was so jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "It's nice that children are so meek...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Now it's nice and warm during the day,\x01",
            "but standing guard out here on those\x01",
            "cold winter nights is the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "It's dark, cold, the wind is unrelenting,\x01",
            "my skin gets chapped, and my nose\x01",
            "never stops running...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "And on summer days, it's hotter than\x01",
            "an oven, and I feel myself fading in\x01",
            "and out of consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "But the view is splendid,\x01",
            "so I am glad I work here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116F")

    label("loc_10CB")


    ChrTalk(    #45
        0xFE,
        (
            "Not too long ago, my only\x01",
            "daughter came to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "When I told her this is where\x01",
            "I worked, she was so jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "It's nice that children are so meek...\x02",
    )

    CloseMessageWindow()

    label("loc_116F")

    Jump("loc_14D5")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1265")

    ChrTalk(    #48
        0xFE,
        (
            "There's been nothing out of\x01",
            "the ordinary today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Both the Grancel and Rolent sides\x01",
            "are pretty quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Ten years ago the outside of this wall\x01",
            "was flooded with the Imperial Army, but\x01",
            "now it's almost impossible to imagine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1429")
    OP_A2(0x0)

    ChrTalk(    #51
        0xFE,
        "Welcome to the Ahnenburg Wall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Have you come here to sightsee\x01",
            "or investigate the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "This wall surrounds the Grancel\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "In ancient verse, the Royal City is referred\x01",
            "to as a pearl and the Ahnenburg Wall is the\x01",
            "oyster shell which surrounds it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I've heard that the wall is so\x01",
            "old that nobody really knows\x01",
            "why it was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "The prevailing theory seems to\x01",
            "be that it was built to prevent\x01",
            "enemy invasions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1429")


    ChrTalk(    #57
        0xFE,
        (
            "This wall surrounds the Grancel\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "In ancient verse, the Royal City is referred\x01",
            "to as a pearl and the Ahnenburg Wall is the\x01",
            "oyster shell which surrounds it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")

    TalkEnd(0xFE)
    Return()

    # Function_4_120 end

    SaveToFile()

Try(main)
