from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3401.x',
        MapIndex            = 1,
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
        'Private Chesley',                      # 9
        'Tammy',                                # 10
        'Private Jules',                        # 11
        'Private Hector',                       # 12
        'Anton',                                # 13
        'Ricky',                                # 14
        'Ritter Roadway',                       # 15
        'Royal Avenue',                         # 16
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
    )

    DeclNpc(
        X                   = 20790,
        Z                   = 11750,
        Y                   = 6470,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10500,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 10500,
        Z                   = 0,
        Y                   = 3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 13750,
        Y                   = 1650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 16520,
        Z                   = 11750,
        Y                   = -540,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -37360,
        Z                   = 0,
        Y                   = 960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 83520,
        Z                   = 0,
        Y                   = 630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -25540,
        Y                   = -1000,
        Z                   = -4310,
        Range               = -27840,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x1F90,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = 15150,
        TriggerZ            = 11750,
        TriggerY            = 1650,
        TriggerRange        = 400,
        ActorX              = 14160,
        ActorZ              = 15250,
        ActorY              = 1650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_342",          # 01, 1
        "Function_2_396",          # 02, 2
        "Function_3_43D",          # 03, 3
        "Function_4_461",          # 04, 4
        "Function_5_485",          # 05, 5
        "Function_6_4A9",          # 06, 6
        "Function_7_4CD",          # 07, 7
        "Function_8_4F1",          # 08, 8
        "Function_9_ABE",          # 09, 9
        "Function_10_E09",         # 0A, 10
        "Function_11_FD5",         # 0B, 11
        "Function_12_FDA",         # 0C, 12
        "Function_13_1105",        # 0D, 13
        "Function_14_1446",        # 0E, 14
        "Function_15_14F2",        # 0F, 15
        "Function_16_1E18",        # 10, 16
        "Function_17_1EB0",        # 11, 17
        "Function_18_2038",        # 12, 18
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_230")
    ClearChrFlags(0xB, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_24B")
    SetChrPos(0x8, 18040, 11750, -4680, 225)
    Jump("loc_2CD")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_260")
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2B7")
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    SetChrPos(0xC, 14830, 11750, 6510, 90)
    SetChrPos(0xD, 16120, 11750, 4840, 315)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_64(0x0, 0x1)
    Jump("loc_2CD")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2CD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetChrPos(0xC, 14830, 11750, 6510, 90)
    SetChrPos(0xD, 16120, 11750, 4840, 315)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x1413)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_341")

    Return()

    # Function_0_216 end

    def Function_1_342(): pass

    label("Function_1_342")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x230056)
    OP_1C(0x2, 0x0, 0x12)
    OP_1C(0x3, 0x0, 0x12)
    OP_1C(0x4, 0x0, 0x12)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_395")

    Return()

    # Function_1_342 end

    def Function_2_396(): pass

    label("Function_2_396")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3C7"),
        (1, "loc_3D3"),
        (2, "loc_3DF"),
        (3, "loc_3EB"),
        (4, "loc_3F7"),
        (5, "loc_403"),
        (6, "loc_40F"),
        (SWITCH_DEFAULT, "loc_41B"),
    )


    label("loc_3C7")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_427")

    label("loc_3D3")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_427")

    label("loc_3DF")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_427")

    label("loc_3EB")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_427")

    label("loc_3F7")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_427")

    label("loc_403")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_427")

    label("loc_40F")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_41B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_427")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_427")

    label("loc_43C")

    Return()

    # Function_2_396 end

    def Function_3_43D(): pass

    label("Function_3_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_460")
    OP_8D(0xFE, 20420, -7160, 16050, -13610, 2000)
    Jump("Function_3_43D")

    label("loc_460")

    Return()

    # Function_3_43D end

    def Function_4_461(): pass

    label("Function_4_461")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_484")
    OP_8D(0xFE, 15300, 14530, 19530, 9890, 2000)
    Jump("Function_4_461")

    label("loc_484")

    Return()

    # Function_4_461 end

    def Function_5_485(): pass

    label("Function_5_485")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8")
    OP_8D(0xFE, 15160, 2490, 19190, -2240, 2000)
    Jump("Function_5_485")

    label("loc_4A8")

    Return()

    # Function_5_485 end

    def Function_6_4A9(): pass

    label("Function_6_4A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CC")
    OP_8D(0xFE, 30170, 1730, 27910, -3560, 2000)
    Jump("Function_6_4A9")

    label("loc_4CC")

    Return()

    # Function_6_4A9 end

    def Function_7_4CD(): pass

    label("Function_7_4CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F0")
    OP_8D(0xFE, 23750, 7410, 18380, -2820, 2000)
    Jump("Function_7_4CD")

    label("loc_4F0")

    Return()

    # Function_7_4CD end

    def Function_8_4F1(): pass

    label("Function_8_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    Call(0, 15)
    Return()

    label("loc_502")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5CF")

    ChrTalk(    #0
        0xFE,
        (
            "Colonel Cid has more of a civil\x01",
            "servant look about him, but he's actually\x01",
            "a hell of a fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "He's one of the best in the Royal Army\x01",
            "when it comes to arts, from what I hear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676")

    label("loc_5CF")


    ChrTalk(    #2
        0xFE,
        (
            "Leiston Fortress units will be handling\x01",
            "security at the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Colonel Cid will be taking command,\x01",
            "too, so it sounds like we're in good shape.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_676")

    Jump("loc_ABA")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_776")

    ChrTalk(    #4
        0xFE,
        (
            "The tower started shining after the\x01",
            "birthday celebrations, as I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "At some point, there was this big,\x01",
            "pillar-like light rising into the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Ever since then, you can see a light\x01",
            "glowing on the very top of the tower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_854")

    label("loc_776")


    ChrTalk(    #7
        0xFE,
        (
            "From here, you can see the\x01",
            "Carnelia Tower on the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Speaking of, the top of the tower's\x01",
            "been shining like crazy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I reported it to my commanding officer,\x01",
            "but I wonder what that light is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_854")

    Jump("loc_ABA")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_8E6")

    ChrTalk(    #10
        0xFE,
        (
            "*pheeew* Took ages, but I've finally\x01",
            "finished cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Earthquakes are pretty rare, so I hope\x01",
            "we don't get another one...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_956")

    ChrTalk(    #12
        0xFE,
        "Tammy said she saw that weird guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "She works at the cafeteria, so why\x01",
            "don't you go ask her?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(    #14
        0xFE,
        "Just look at this mess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I hope we can clean up in time for dinner...\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(    #16
        0x8,
        "Climbing the wall is dangerous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "I gotta make sure to warn that guy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_A10")


    ChrTalk(    #18
        0x8,
        (
            "Trying to climb the wall is insane.\x01",
            "What does he plan on doing if he falls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "What the...?! No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "Hope he isn't thinking of doing anything\x01",
            "too crazy...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ABA")

    TalkEnd(0x8)
    Return()

    # Function_8_4F1 end

    def Function_9_ABE(): pass

    label("Function_9_ABE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_B23")

    ChrTalk(    #21
        0xFE,
        (
            "Welcome to the Sanktheim Gate. If you\x01",
            "have any business here, please, come\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E05")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #22
        0xFE,
        (
            "Hector went off to help and still hasn't\x01",
            "come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I wonder if he's eating early.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFA")

    label("loc_B95")


    ChrTalk(    #24
        0xFE,
        (
            "We finished cleaning up after the\x01",
            "earthquake, but I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Hector still isn't back.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BFA")

    Jump("loc_E05")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C6C")

    ChrTalk(    #26
        0xFE,
        (
            "Everyone at the gate's crazy busy\x01",
            "cleaning up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "My partner, Hector, ran off to help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDF")

    label("loc_C6C")


    ChrTalk(    #28
        0xFE,
        "Man, this place was shaking like mad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Don't know when's the last time\x01",
            "I feared for my life like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CDF")

    Jump("loc_E05")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D32")

    ChrTalk(    #30
        0xA,
        (
            "Welcome to the Sanktheim Gate!\x01",
            "Tourists are also welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E05")

    label("loc_D32")


    ChrTalk(    #31
        0xA,
        (
            "Welcome to the Sanktheim Gate!\x01",
            "Tourists are also welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "This is part of the ancient fortress\x01",
            "called Ahnenburg, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "It's a popular tourist spot, so a lot of\x01",
            "people come to take a gander.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E05")

    TalkEnd(0xA)
    Return()

    # Function_9_ABE end

    def Function_10_E09(): pass

    label("Function_10_E09")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EA8")

    ChrTalk(    #34
        0xFE,
        "Oh, yeah, the signing ceremony is soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Maaaan, the commander is gonna be\x01",
            "screaming in our ears about heightened\x01",
            "security AGAIN.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF8")

    label("loc_EA8")


    ChrTalk(    #36
        0xFE,
        "The earthquakes have finally settled down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Now I can breathe easy!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EF8")

    Jump("loc_FD1")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F76")

    ChrTalk(    #38
        0xB,
        (
            "Even if you don't have any specific business\x01",
            "here, it's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        "Go in and out as you please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FD1")

    label("loc_F76")


    ChrTalk(    #40
        0xB,
        "Hey, how's it goin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xB,
        (
            "If you have business, take it inside\x01",
            "with the commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_FD1")

    TalkEnd(0xB)
    Return()

    # Function_10_E09 end

    def Function_11_FD5(): pass

    label("Function_11_FD5")

    Call(0, 12)
    Return()

    # Function_11_FD5 end

    def Function_12_FDA(): pass

    label("Function_12_FDA")

    OP_EA(0x1, 0xA, 0x0, 0x0)
    SetChrName("Anton")
    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_107D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1037")

    ChrTalk(    #42
        0xFE,
        "Holy crap, I-I almost fell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Boy, that was scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_107A")

    label("loc_1037")


    ChrTalk(    #44
        0xFE,
        "*pant* *pant* Boy, that was scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "I-I almost fell!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_107A")

    Jump("loc_1101")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10BE")

    ChrTalk(    #46
        0xC,
        "Fareweeeeeell--!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        "My youuuuuuuuuth--!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1101")

    label("loc_10BE")


    ChrTalk(    #48
        0xC,
        "I hate--!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        "Birthday celebrations--!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xC,
        "Aaaaaaghh!!!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1101")

    TalkEnd(0xC)
    Return()

    # Function_12_FDA end

    def Function_13_1105(): pass

    label("Function_13_1105")

    SetChrName("Ricky")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1123")
    ClearChrFlags(0xD, 0x10)
    Jump("loc_1128")

    label("loc_1123")

    SetChrFlags(0xD, 0x10)

    label("loc_1128")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #51
        0xFE,
        (
            "This guy had climbed atop the wall\x01",
            "when the earthquake hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "He was so shocked by the shaking,\x01",
            "he almost fell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AA")

    label("loc_11B4")


    ChrTalk(    #53
        0xFE,
        (
            "This guy had climbed atop the wall\x01",
            "when the earthquake hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "He was so shocked by the shaking,\x01",
            "he almost fell.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xC, 400)

    ChrTalk(    #55
        0xFE,
        (
            "Had the earthquake been any stronger,\x01",
            "he might've really fallen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "At least you're lucky in one way, Anton.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12AA")

    Jump("loc_1442")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(    #57
        0xD,
        (
            "My buddy Anton confessed to his love\x01",
            "to a girl during the Queen's Birthday\x01",
            "Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "As you might have guessed by the\x01",
            "way he's acting, he was totally rejected\x01",
            "in the bluntest way possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        (
            "So he came here to erase all the bad\x01",
            "memories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_13BC")


    ChrTalk(    #60
        0xD,
        "Anton... You're facing towards Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "If you hate the Birthday Celebration\x01",
            "so much, at least scream towards the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1442")

    TalkEnd(0xD)
    Return()

    # Function_13_1105 end

    def Function_14_1446(): pass

    label("Function_14_1446")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1459")
    Call(0, 16)

    label("loc_1459")

    OP_6D(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x61A80, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC09._CH", 0x1, 0x7D0)
    OP_DE("Sanktheim Gate")
    FadeToBright(2000, 0)
    OP_6C(45000, 6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1446 end

    def Function_15_14F2(): pass

    label("Function_15_14F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_150C")
    Call(0, 16)
    FadeToBright(0, 0)

    label("loc_150C")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 18120, 11750, -11850, 270)
    SetChrPos(0xF7, 18420, 11750, -13130, 270)
    SetChrPos(0x105, 19340, 11750, -11430, 270)
    SetChrPos(0x104, 19610, 11750, -12770, 270)
    SetChrPos(0x8, 16800, 11750, -12550, 90)
    OP_6D(17660, 11750, -12360, 0)
    OP_67(0, 7800, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(310000, 0)
    OP_6E(423, 0)
    OP_0D()

    ChrTalk(    #62
        0x8,
        "#6PHuh? Who're you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F#7PYou're Private Chesley, right?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(    #64
        0x106,
        (
            "#051F#6PWe're with the Bracer Guild.\x02\x03",

            "Mind if we ask you about the earthquake\x01",
            "that happened a little bit ago?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FA")

    label("loc_1672")


    ChrTalk(    #65
        0x103,
        (
            "#020F#6PWe're from the Bracer Guild,\x01",
            "Private Chesley.\x02\x03",

            "May we ask you a few questions\x01",
            "about the earthquake that\x01",
            "happened recently?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05Estelle's group asked about the suspicious man Chesley saw.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #67
        0x8,
        "#6POh, right, that guy from yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#6PI dunno if he has anything to\x01",
            "do with the earthquake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#6PBut I did see a tall man with\x01",
            "black sunglasses around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1002F#7PI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x105,
        (
            "#047FIt must be the same man\x01",
            "seen at the Wolf Fort...\x02\x03",

            "#043FSir, did you see what this\x01",
            "man was doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#6PUh, well, he seemed like kind of a\x01",
            "tourist, really. Looked at the scenery\x01",
            "for a bit, then came down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#6PHe sorta caught my attention since\x01",
            "you don't see glasses like his often...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#6PHe didn't say anything to me and\x01",
            "walked off, though. I didn't have\x01",
            "a chance to talk to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1007F#7PHrm, okay...\x02\x03",

            "#1015FDid anyone else see\x01",
            "this guy, maybe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#6PYou know, that's where it gets\x01",
            "weird, thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#6PI brought the guy up at dinner\x01",
            "since he was kinda weird, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "#6PPractically nobody else even saw the guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#6PThe only one who remembered seeing him\x01",
            "was Tammy, who works in the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#032F#2PHm. Unlike the Wolf Fort, this\x01",
            "gate sees quite a bit of traffic.\x02\x03",

            "And yet, despite this, there\x01",
            "are only two witnesses?\x02\x03",

            "#035FHow wonderfully...spooky.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(    #81
        0x106,
        (
            "#053F#6PAll the more reason to see\x01",
            "what that girl has to say.\x02\x03",

            "#050FYou said Tammy's in the\x01",
            "mess hall, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC6")

    label("loc_1C32")


    ChrTalk(    #82
        0x103,
        (
            "#026F#6PSpooky or not, it would be a good\x01",
            "idea to talk to this 'Tammy' and\x01",
            "see what she knows.\x02\x03",

            "#020FYou said she's in the mess hall,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC6")


    ChrTalk(    #83
        0x101,
        "#1006F#7PThanks, Chesley! You were a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#6PNo problem! And yeah, she\x01",
            "should be in the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "#6PGood luck with your investigation.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18730, 11750, -12190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18730, 11750, -12190, 90)
    SetChrPos(0x1, 18730, 11750, -12190, 90)
    SetChrPos(0x2, 18730, 11750, -12190, 90)
    SetChrPos(0x3, 18730, 11750, -12190, 90)
    OP_4B(0x8, 255)
    OP_A2(0x1415)
    OP_28(0x86, 0x1, 0x8)
    OP_28(0x86, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_14F2 end

    def Function_16_1E18(): pass

    label("Function_16_1E18")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E91"),
        (1, "loc_1E97"),
        (SWITCH_DEFAULT, "loc_1E9D"),
    )


    label("loc_1E91")

    OP_A2(0x1200)
    Jump("loc_1E9D")

    label("loc_1E97")

    OP_A2(0x1201)
    Jump("loc_1E9D")

    label("loc_1E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1EAB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1EAF")

    label("loc_1EAB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1EAF")

    Return()

    # Function_16_1E18 end

    def Function_17_1EB0(): pass

    label("Function_17_1EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2037")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F34")

    ChrTalk(    #86
        0x101,
        (
            "#1002FOur investigations here aren't finished.\x02\x03",

            "Let's hurry up and get the questioning\x01",
            "done with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2017")

    label("loc_1F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1FA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F51")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1F58")

    label("loc_1F51")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1F58")


    ChrTalk(    #87
        0x106,
        (
            "#050FOur investigation here ain't over.\x02\x03",

            "Let's get back to questionin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2017")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FBE")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1FC5")

    label("loc_1FBE")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1FC5")


    ChrTalk(    #88
        0x103,
        (
            "#020FOur investigation here isn't over.\x02\x03",

            "We need to continue the interviews.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2017")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2037")

    Return()

    # Function_17_1EB0 end

    def Function_18_2038(): pass

    label("Function_18_2038")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_18_2038 end

    SaveToFile()

Try(main)
