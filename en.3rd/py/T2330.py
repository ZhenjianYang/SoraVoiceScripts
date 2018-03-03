from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2330   ._SN',
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
        'Rex',                                  # 9
        'Carla',                                # 10
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_144",          # 02, 2
        "Function_3_149",          # 03, 3
        "Function_4_67E",          # 04, 4
        "Function_5_683",          # 05, 5
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    Return()

    # Function_1_143 end

    def Function_2_144(): pass

    label("Function_2_144")

    Call(0, 3)
    Return()

    # Function_2_144 end

    def Function_3_149(): pass

    label("Function_3_149")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_26B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BF")

    ChrTalk(    #0
        0x10,
        (
            "There's no harm in playing around and\x01",
            "having a good time. Just make sure you\x01",
            "don't get hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268")

    label("loc_1BF")


    ChrTalk(    #1
        0x10,
        "Hmm? What happened to Polly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "Is she playing with Clem and Daniel now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "Well, that's all right. Though, I hope they\x01",
            "all take it easy and don't get hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_268")

    Jump("loc_67A")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_3F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_303")

    ChrTalk(    #4
        0x10,
        (
            "I'll have to go and check the bazaar out\x01",
            "myself a bit later on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "All of the interesting items might have sold\x01",
            "by now, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5")

    label("loc_303")


    ChrTalk(    #6
        0x10,
        "Well! You two look cheery all of a sudden.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "Did you find something interesting over at\x01",
            "the bazaar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14E,
        "#1711FThat's a secret!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14F,
        "#1732FA BIIIG secret!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "Ahaha. Maybe I should pop over there myself\x01",
            "and see what I find, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3F5")

    Jump("loc_67A")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 1)), scpexpr(EXPR_END)), "loc_5AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46D")

    ChrTalk(    #11
        0x10,
        (
            "Lucia's supposed to be helping out over at the\x01",
            "bazaar, too. Why not pop by for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A9")

    label("loc_46D")


    ChrTalk(    #12
        0x10,
        (
            "I take it you've heard about the bazaar in town\x01",
            "already? It started today, if you haven't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "The town's all in a bustle because of it.\x01",
            "A bazaar like this feels right for a rural\x01",
            "town like this, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "I think Lucia's out helping with it, too.\x01",
            "If you're interested, you should stop by\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5A9")

    Jump("loc_670")

    label("loc_5AC")


    ChrTalk(    #15
        0x10,
        "Hello there, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14E,
        "#1718FHello, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "Thanks so much for always playing with our Lucia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14F,
        "#1732FYou're welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "Haha. Always nice to see such cheery faces\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F41)

    label("loc_670")

    Jump("loc_67A")

    label("loc_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_67A")

    label("loc_67A")

    TalkEnd(0x10)
    Return()

    # Function_3_149 end

    def Function_4_67E(): pass

    label("Function_4_67E")

    Call(0, 5)
    Return()

    # Function_4_67E end

    def Function_5_683(): pass

    label("Function_5_683")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_8D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 2)), scpexpr(EXPR_END)), "loc_7BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_712")

    ChrTalk(    #20
        0x11,
        (
            "Try and go home before it gets dark, all right?\x02\x03",

            "Otherwise Matron Theresa will be very worried \x01",
            "about you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BA")

    label("loc_712")


    ChrTalk(    #21
        0x11,
        (
            "Just remember that Matron Theresa will worry\x01",
            "about you all if you stay out too late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "Try and go home before it gets dark, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        "#1713F...I will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7BA")

    Jump("loc_8D4")

    label("loc_7BD")


    ChrTalk(    #24
        0x11,
        (
            "Hmm? I thought you were with Polly earlier?\x02\x03",

            "What happened to her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x14E,
        (
            "#1713FShe's... Umm... She's playing with Clem and\x01",
            "Daniel at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "Oh, really? That's all right, then.\x02\x03",

            "You all be careful. And remember to stay\x01",
            "away from tall cliffs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x14E,
        "#1712FI-I will!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F42)

    label("loc_8D4")

    Jump("loc_B3A")

    label("loc_8D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_9E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_942")

    ChrTalk(    #28
        0x11,
        "Come play with Lucia again soon, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        "I'm sure nothing would make her happier.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_942")


    ChrTalk(    #30
        0x11,
        "Oh? What's going on here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "You look like you're having fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x14E,
        "#1711FNothing! Nothing at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14F,
        "#1732FNothing at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "Heehee. Really, now? \x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9E4")

    Jump("loc_B3A")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A54")

    ChrTalk(    #35
        0x11,
        "Lucia's always loved big events like these.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "And people wonder who she took after.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B30")

    label("loc_A54")


    ChrTalk(    #37
        0x11,
        "Oh, if it isn't Mary and Polly! Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "If you're looking for Lucia, she's out helping\x01",
            "with the bazaar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "She loves these kinds of things, you see,\x01",
            "so she couldn't resist trying to get involved\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B30")

    Jump("loc_B3A")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_B3A")

    label("loc_B3A")

    TalkEnd(0x11)
    Return()

    # Function_5_683 end

    SaveToFile()

Try(main)
