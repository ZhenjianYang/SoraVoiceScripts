from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3210   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Lynn',                                 # 9
        'Cyril',                                # 10
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
    )

    DeclNpc(
        X                   = 28010,
        Z                   = 0,
        Y                   = 4920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 3350,
        Z                   = 250,
        Y                   = 3380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_13C",          # 02, 2
        "Function_3_85B",          # 03, 3
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_104")
    Jump("loc_13A")

    label("loc_104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_10E")
    Jump("loc_13A")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_118")
    Jump("loc_13A")

    label("loc_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_133")
    SetChrPos(0x8, 27000, 0, 3050, 270)
    Jump("loc_13A")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_13A")

    label("loc_13A")

    Return()

    # Function_0_FA end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Return()

    # Function_1_13B end

    def Function_2_13C(): pass

    label("Function_2_13C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2")

    ChrTalk(    #0
        0xFE,
        (
            "I heard from the soldiers here on patrol,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Apparently orbments aren't working\x01",
            "throughout Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Th-That's pretty crazy.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_236")

    label("loc_1E2")


    ChrTalk(    #3
        0xFE,
        (
            "For orbments to be out across the\x01",
            "entire country...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "It's hard to believe.\x02",
    )

    CloseMessageWindow()

    label("loc_236")

    Jump("loc_857")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D1")

    ChrTalk(    #5
        0xFE,
        (
            "Awww, man. Seems like there's trouble\x01",
            "at the hot springs AGAIN.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "The orbment lights aren't working either.\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_857")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_374")

    ChrTalk(    #7
        0x8,
        (
            "The hot springs have finally gone back\x01",
            "to a normal temperature, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Apparently you can use the baths\x01",
            "at the Maple Leaf Inn again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486")

    label("loc_374")


    ChrTalk(    #9
        0x8,
        (
            "The hot springs have finally gone back\x01",
            "to a normal temperature, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Apparently you can use the baths\x01",
            "at the Maple Leaf Inn again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "That reminds me, there was an earthquake,\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I wonder if the trouble at the hot springs\x01",
            "is related to that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_486")

    Jump("loc_857")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_523")

    ChrTalk(    #13
        0x8,
        (
            "But, our village's hot springs are connected\x01",
            "straight from the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "I wonder if something happened\x01",
            "at the water source...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_602")

    label("loc_523")


    ChrTalk(    #15
        0x8,
        (
            "I thought it was loud outside, and wouldn't you\x01",
            "know it, the springs were just bubbling away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "As a housewife, it's nice to not have\x01",
            "to take the time to boil water, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "I suppose that's not the problem.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_602")

    Jump("loc_857")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_736")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_67B")

    ChrTalk(    #18
        0x8,
        (
            "Lately my daughter's been working\x01",
            "a side job at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "I hope she's taking it seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_733")

    label("loc_67B")


    ChrTalk(    #20
        0x8,
        "My daughter's FINALLY started working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "Yes, it may be true that it's a simple\x01",
            "a part-time job at the inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "...but it's better than having her lying\x01",
            "about the house.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_733")

    Jump("loc_857")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(    #23
        0x8,
        (
            "My husband's the chef behind the\x01",
            "Maple Leaf Inn's infamous Eastern\x01",
            "cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "He's well respected, you know. Magazines\x01",
            "and papers come to interview him all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_857")

    label("loc_7F5")


    ChrTalk(    #25
        0x8,
        "Oh, are you looking for the inn?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "The Maple Leaf Inn is straight down\x01",
            "the front road.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_857")

    TalkEnd(0x8)
    Return()

    # Function_2_13C end

    def Function_3_85B(): pass

    label("Function_3_85B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_9A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_939")

    ChrTalk(    #27
        0xFE,
        "Ah, it's good to have the pump fixed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "The inn can continue business...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "And it really saves us the time of boiling water.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "That's especially helpful now with orbments\x01",
            "not working.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_99F")

    label("loc_939")


    ChrTalk(    #31
        0xFE,
        "It's good to have the pump fixed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "More than anything it saves us\x01",
            "the time of boiling water.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F")

    Jump("loc_10B1")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")

    ChrTalk(    #33
        0xFE,
        (
            "With the orbments stopped, the pump's\x01",
            "not working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Our village survives on the tourism the\x01",
            "springs bring in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "If they're not fixed soon, I'm not sure\x01",
            "how we're going to make it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_AF8")

    label("loc_A77")


    ChrTalk(    #36
        0xFE,
        (
            "With the orbments stopped, the pump's\x01",
            "not working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "If they're not fixed soon, I'm not sure\x01",
            "how we're going to make it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF8")

    Jump("loc_10B1")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(    #38
        0x9,
        (
            "It seems the water's at a normal\x01",
            "temperature again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "Still, what a curious series of events.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "It seems it really might have been\x01",
            "an effect of the earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B1")

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(    #41
        0x9,
        "Perhaps there was a change in the earth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "There was an earthquake, so it's\x01",
            "not unthinkable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB6")

    label("loc_C27")


    ChrTalk(    #43
        0x9,
        "*sigh* What a mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "If the hot springs are no good,\x01",
            "the inn can't keep up business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        "Perhaps there was a change in the earth.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CB6")

    Jump("loc_10B1")

    label("loc_CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_F61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(    #46
        0x9,
        (
            "S-Something just ran behind my\x01",
            "house in a real hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "Wh-What was that, anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "I-It looked like a monster, but maybe\x01",
            "I imagined it...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5E")

    label("loc_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E2B")

    ChrTalk(    #49
        0x9,
        (
            "I heard rumors about a peeping\x01",
            "tom at the outdoor baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "I can't believe there'd be anyone\x01",
            "in this village who'd do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        "I'm sure it's just our customers' imaginations.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5E")

    label("loc_E2B")


    ChrTalk(    #52
        0x9,
        (
            "I heard from my wife Addy who works\x01",
            "at the inn, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Apparently there are rumors of a peeping\x01",
            "tom at the outdoor baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "I can't believe there'd be anyone\x01",
            "in this village who'd do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "Mrs. Mao contacted the guild just in case,\x01",
            "but I'm sure it's just our customers'\x01",
            "imaginations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F5E")

    Jump("loc_10B1")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_10B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(    #56
        0x9,
        "Hey, welcome. Welcome to Elmo Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "This place has been a hot springs haven for\x01",
            "some time now. We get a lot of visitors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B1")

    label("loc_FF8")


    ChrTalk(    #58
        0x9,
        "Hey, welcome. Welcome to Elmo Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        "Did you come here for the hot springs too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "This place has been a hot springs haven for\x01",
            "some time now. We get a lot of visitors.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_10B1")

    TalkEnd(0x9)
    Return()

    # Function_3_85B end

    SaveToFile()

Try(main)
