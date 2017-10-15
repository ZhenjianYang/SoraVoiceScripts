from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3400.x',
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
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Private Jules',                        # 14
        'Private Hector',                       # 15
        'Anton',                                # 16
        'Ricky',                                # 17
        'Private Wolpe',                        # 18
        'Private Olnis',                        # 19
        'Gundolf',                              # 20
        'Ritter Roadway',                       # 21
        'Royal Avenue',                         # 22
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
        'ED6_DT07/CH01750 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01750P._CP',             # 05
    )

    DeclNpc(
        X                   = 20790,
        Z                   = 11750,
        Y                   = 6470,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 13400,
        Y                   = 1650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 5730,
        Z                   = 0,
        Y                   = 4940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 35310,
        Z                   = 0,
        Y                   = 3610,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 40970,
        Z                   = 0,
        Y                   = 10,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = 15150,
        TriggerZ            = 11750,
        TriggerY            = 1650,
        TriggerRange        = 400,
        ActorX              = 14160,
        ActorZ              = 14750,
        ActorY              = 1650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_45F",          # 01, 1
        "Function_2_517",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_606",          # 05, 5
        "Function_6_62A",          # 06, 6
        "Function_7_64E",          # 07, 7
        "Function_8_672",          # 08, 8
        "Function_9_696",          # 09, 9
        "Function_10_6BA",         # 0A, 10
        "Function_11_1341",        # 0B, 11
        "Function_12_135C",        # 0C, 12
        "Function_13_1377",        # 0D, 13
        "Function_14_1392",        # 0E, 14
        "Function_15_1A04",        # 0F, 15
        "Function_16_1F01",        # 10, 16
        "Function_17_1F06",        # 11, 17
        "Function_18_20C3",        # 12, 18
        "Function_19_234F",        # 13, 19
        "Function_20_29AB",        # 14, 20
        "Function_21_2FE7",        # 15, 21
        "Function_22_344C",        # 16, 22
        "Function_23_40D8",        # 17, 23
        "Function_24_4119",        # 18, 24
        "Function_25_41B1",        # 19, 25
        "Function_26_4334",        # 1A, 26
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 20790, 11750, 6470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_311")
    ClearChrFlags(0x13, 0x80)

    label("loc_311")

    Jump("loc_450")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_347")
    OP_43(0x8, 0x0, 0x0, 0x7)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 35300, 0, -3600, 90)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_450")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_35D")
    ClearChrFlags(0xE, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_36E")
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_37F")
    OP_43(0x8, 0x0, 0x0, 0x7)
    Jump("loc_450")

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_429")
    SetChrPos(0x8, 18300, 11750, -10110, 225)
    OP_43(0x8, 0x0, 0x0, 0x3)
    SetChrPos(0xA, 17700, 11750, 12950, 270)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x4)
    SetChrPos(0xB, 17070, 11750, -190, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x5)
    SetChrPos(0xC, 29080, 11750, -1550, 90)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x6)
    SetChrPos(0xF, 16120, 11750, 5980, 270)
    SetChrPos(0x10, 16120, 11750, 4840, 0)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_450")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_450")
    ClearChrFlags(0xE, 0x80)
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_45E")
    OP_A3(0x10F0)
    Event(0, 22)

    label("loc_45E")

    Return()

    # Function_0_2DE end

    def Function_1_45F(): pass

    label("Function_1_45F")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x230056)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A4")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 100)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 100)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 100)
    Jump("loc_4B3")

    label("loc_4A4")

    OP_1C(0x2, 0x0, 0x1A)
    OP_1C(0x3, 0x0, 0x1A)
    OP_1C(0x4, 0x0, 0x1A)

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4C1")
    OP_64(0x0, 0x1)
    Jump("loc_4E4")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_4E4")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4D9")
    OP_64(0x0, 0x1)
    Jump("loc_4E4")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_4E4")
    OP_64(0x0, 0x1)

    label("loc_4E4")

    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_516")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_516")

    Return()

    # Function_1_45F end

    def Function_2_517(): pass

    label("Function_2_517")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_548"),
        (1, "loc_554"),
        (2, "loc_560"),
        (3, "loc_56C"),
        (4, "loc_578"),
        (5, "loc_584"),
        (6, "loc_590"),
        (SWITCH_DEFAULT, "loc_59C"),
    )


    label("loc_548")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5A8")

    label("loc_554")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5A8")

    label("loc_560")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5A8")

    label("loc_56C")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5A8")

    label("loc_578")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A8")

    label("loc_584")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5A8")

    label("loc_590")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_59C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A8")

    label("loc_5BD")

    Return()

    # Function_2_517 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_8D(0xFE, 20420, -7160, 16050, -13610, 2000)
    Jump("Function_3_5BE")

    label("loc_5E1")

    Return()

    # Function_3_5BE end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_605")
    OP_8D(0xFE, 15300, 14530, 19530, 9890, 2000)
    Jump("Function_4_5E2")

    label("loc_605")

    Return()

    # Function_4_5E2 end

    def Function_5_606(): pass

    label("Function_5_606")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_629")
    OP_8D(0xFE, 15160, 2490, 19190, -2240, 2000)
    Jump("Function_5_606")

    label("loc_629")

    Return()

    # Function_5_606 end

    def Function_6_62A(): pass

    label("Function_6_62A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64D")
    OP_8D(0xFE, 30170, 1730, 27910, -3560, 2000)
    Jump("Function_6_62A")

    label("loc_64D")

    Return()

    # Function_6_62A end

    def Function_7_64E(): pass

    label("Function_7_64E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_8D(0xFE, 23750, 7410, 18380, -2820, 2000)
    Jump("Function_7_64E")

    label("loc_671")

    Return()

    # Function_7_64E end

    def Function_8_672(): pass

    label("Function_8_672")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_695")
    OP_8D(0xFE, 9410, 9240, 790, -7190, 2000)
    Jump("Function_8_672")

    label("loc_695")

    Return()

    # Function_8_672 end

    def Function_9_696(): pass

    label("Function_9_696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B9")
    OP_8D(0xFE, 38690, -4550, 43980, 4290, 2000)
    Jump("Function_9_696")

    label("loc_6B9")

    Return()

    # Function_9_696 end

    def Function_10_6BA(): pass

    label("Function_10_6BA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_82F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CF")

    ChrTalk(    #0
        0xFE,
        (
            "That floating island's still\x01",
            "floating around today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Ever since that island appeared\x01",
            "orbments haven't worked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "I kinda feel like that itself isn't at fault.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It's just my own impression, but...\x01",
            "there's something sublime about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_82C")

    label("loc_7CF")


    ChrTalk(    #4
        0xFE,
        (
            "I feel something divine about\x01",
            "that floating island.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I'm sure it itself isn't evil.\x02",
    )

    CloseMessageWindow()

    label("loc_82C")

    Jump("loc_133D")

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_951")

    ChrTalk(    #6
        0xFE,
        "You can kinda see that floating island from here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Since I'm dying of boredom, I've spent a lot\x01",
            "of time just watching it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Oooonce in a very rare while I see\x01",
            "something atop the island.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It kinda looks like buildings, but I wonder\x01",
            "exactly what it is...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9CC")

    label("loc_951")


    ChrTalk(    #10
        0xFE,
        (
            "If you squint, you can kinda see stuff that looks\x01",
            "like buildings on that floating island.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "I wonder what it is...\x02",
    )

    CloseMessageWindow()

    label("loc_9CC")

    Jump("loc_133D")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A7D")

    ChrTalk(    #12
        0xFE,
        (
            "Seems like the Intelligence Division's\x01",
            "shown up near the royal villa too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "All of them, including the members who\x01",
            "were in the capital, have been taken in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_B70")

    ChrTalk(    #14
        0xFE,
        (
            "I hope that peace really does come when\x01",
            "the non-aggression pact is signed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I wonder how well it'll actually go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "For example, I doubt the Imperial and Republican\x01",
            "border troubles can be solved through discussion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_BFD")

    ChrTalk(    #17
        0xFE,
        (
            "*pheeew* Guard and patrol missions\x01",
            "really are a lot more relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Even the Royal Army can't defend against\x01",
            "earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_CB8")

    ChrTalk(    #19
        0xFE,
        "Right now, the royal villa is open to civilians.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Soon it'll be used as patrol headquarters,\x01",
            "I hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "If you're going to visit the villa,\x01",
            "you might want to go now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D82")

    ChrTalk(    #22
        0xFE,
        (
            "Colonel Cid has more of a civil servant\x01",
            "look about him, but he's actually a heck\x01",
            "of a fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "He's one of the best in the Royal Army\x01",
            "when it comes to arts, from what I hear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFB")

    label("loc_D82")


    ChrTalk(    #24
        0xFE,
        (
            "Apparently it'll be the Leiston Fortress units\x01",
            "that handle security at the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Seems Colonel Cid will be taking command,\x01",
            "too, so it sounds like we're in good shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "He has more of a civil servant look about\x01",
            "him, but Colonel Cid's actually a heck\x01",
            "of a fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "He's one of the best in the Royal Army\x01",
            "when it comes to arts, from what I hear.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EFB")

    Jump("loc_133D")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_10D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF9")

    ChrTalk(    #28
        0xFE,
        (
            "The tower started shining after the\x01",
            "birthday celebrations, as I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "At some point there was this big\x01",
            "pillar-like light rising into the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Ever since then, you can see a light\x01",
            "glowing on the very top of the tower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_FF9")


    ChrTalk(    #31
        0xFE,
        (
            "From here you can see the Carnelia Tower\x01",
            "on the Tratt Plains, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Lately the top of the tower's\x01",
            "been shining like crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I reported it to my commanding officer,\x01",
            "but I wonder what that light is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10D0")

    Jump("loc_133D")

    label("loc_10D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_116C")

    ChrTalk(    #34
        0xFE,
        (
            "*pheeew* Took ages, but I've finally\x01",
            "finished cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Earthquakes are pretty rare, apparently,\x01",
            "so I hope we don't get another one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_11DE")

    ChrTalk(    #36
        0xFE,
        "Tammy apparently saw that weird guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "She works at the cafeteria,\x01",
            "so why don't you go ask her?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_11DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1237")

    ChrTalk(    #38
        0xFE,
        "Just look at this mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I hope we can clean up in time for dinner...\x02",
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1298")

    ChrTalk(    #40
        0x8,
        "Climbing the wall is dangerous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        "I gotta make sure to warn that guy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_1298")


    ChrTalk(    #42
        0x8,
        (
            "Trying to climb the wall is insane.\x01",
            "What does he plan on doing if he falls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "Ah?! N-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Hope he isn't thinking of doing anything\x01",
            "too crazy...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_133D")

    TalkEnd(0x8)
    Return()

    # Function_10_6BA end

    def Function_11_1341(): pass

    label("Function_11_1341")

    TalkBegin(0xA)

    ChrTalk(    #45
        0xA,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_11_1341 end

    def Function_12_135C(): pass

    label("Function_12_135C")

    TalkBegin(0xB)

    ChrTalk(    #46
        0xB,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_12_135C end

    def Function_13_1377(): pass

    label("Function_13_1377")

    TalkBegin(0xC)

    ChrTalk(    #47
        0xC,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_13_1377 end

    def Function_14_1392(): pass

    label("Function_14_1392")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B8")

    ChrTalk(    #48
        0xFE,
        (
            "If the airships can't fly, then our\x01",
            "responsibility's all the greater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "With air passage cut off, the only routes to\x01",
            "invade the capital are from the east and\x01",
            "west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "In other words, if our security is sufficient,\x01",
            "then we can protect the peace of the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1545")

    label("loc_14B8")


    ChrTalk(    #51
        0xFE,
        (
            "The gate is a problem, but there's not\x01",
            "much we can do about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "The problem is how to secure the\x01",
            "guard post in these conditions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1545")

    Jump("loc_1A00")

    label("loc_1548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161F")

    ChrTalk(    #53
        0xFE,
        "Hey, welcome to the Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "...is how I'd really like to welcome you,\x01",
            " but things are a bit dire for that cheerful\x01",
            " a greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Everyone inside the guard post is on edge.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_16B6")

    label("loc_161F")


    ChrTalk(    #56
        0xFE,
        (
            "Normally I'd love to welcome you with a smile,\x01",
            "but given the situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "If you're here for tourism purposes,\x01",
            "please come back another day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B6")

    Jump("loc_1A00")

    label("loc_16B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_171B")

    ChrTalk(    #58
        0xFE,
        (
            "Welcome to the Sanktheim Gate. If you have\x01",
            "any business here, please, come inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A00")

    label("loc_171B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_180B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1783")

    ChrTalk(    #59
        0xFE,
        "Hector went off to help and still isn't back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "I wonder if he's eating early.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1808")

    label("loc_1783")


    ChrTalk(    #61
        0xFE,
        (
            "Seems like cleaning up after\x01",
            "the earthquake's done, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Hector still isn't back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "I wonder if he's eating early.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1808")

    Jump("loc_1A00")

    label("loc_180B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_18E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1878")

    ChrTalk(    #64
        0xFE,
        "Everyone at the gate's crazy busy cleaning up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "My partner Hector ran off to help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18E1")

    label("loc_1878")


    ChrTalk(    #66
        0xFE,
        "It was really shaking a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "It's been a while since I've feared for\x01",
            "my life like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_18E1")

    Jump("loc_1A00")

    label("loc_18E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1934")

    ChrTalk(    #68
        0xD,
        (
            "Welcome to the Sanktheim Gate!\x01",
            "Tourists are also welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A00")

    label("loc_1934")


    ChrTalk(    #69
        0xD,
        (
            "Welcome to the Sanktheim Gate!\x01",
            "Tourists are also welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "This is part of the ancient fortress\x01",
            "called Ahnenburg, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "It's a popular tourist spot, so a lot of people\x01",
            "come to see it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1A00")

    TalkEnd(0xD)
    Return()

    # Function_14_1392 end

    def Function_15_1A04(): pass

    label("Function_15_1A04")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2D")

    ChrTalk(    #72
        0xFE,
        (
            "Those guys who are getting scared just\x01",
            "because they can't use their orbal guns\x01",
            "are useless as soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "One way or another, if things come to\x01",
            "a real melee, you can't use guns anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "If it's going to come to that, I'll fight\x01",
            "with my bayonet from the get-go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1BAE")

    label("loc_1B2D")


    ChrTalk(    #75
        0xFE,
        (
            "I've preferred swords to guns for\x01",
            "a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "A sword just feels more like you're using\x01",
            "your own power, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAE")

    Jump("loc_1EFD")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C95")

    ChrTalk(    #77
        0xFE,
        (
            "No matter what we do, this orbal\x01",
            "gate just won't come down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "This is the core of the capital's defense,\x01",
            "so we're in some serious trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Well, even if invaders show up,\x01",
            "I'll stop 'em, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1D2C")

    label("loc_1C95")


    ChrTalk(    #80
        0xFE,
        (
            "For the gate to not close is something\x01",
            "that's literally never happened before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Well, even so, we still have our duty to\x01",
            "protect the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2C")

    Jump("loc_1EFD")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DCC")

    ChrTalk(    #82
        0xFE,
        "Oh, yeah, the signing ceremony is soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Maaaan, the commander is gonna be screaming \x01",
            "in our ears about heightened security AGAIN.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E24")

    label("loc_1DCC")


    ChrTalk(    #84
        0xFE,
        "Seems like the earthquakes've settled down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Everyone can now breathe easy.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1E24")

    Jump("loc_1EFD")

    label("loc_1E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1EA2")

    ChrTalk(    #86
        0xE,
        (
            "Even if you don't have any specific business\x01",
            "here, it's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        "Go in and out as you please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EFD")

    label("loc_1EA2")


    ChrTalk(    #88
        0xE,
        "Hey, how's it goin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "If you have business, take it\x01",
            "inside with the commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1EFD")

    TalkEnd(0xE)
    Return()

    # Function_15_1A04 end

    def Function_16_1F01(): pass

    label("Function_16_1F01")

    Call(0, 17)
    Return()

    # Function_16_1F01 end

    def Function_17_1F06(): pass

    label("Function_17_1F06")

    OP_EA(0x1, 0xA, 0x0, 0x0)
    SetChrName("Anton")
    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F59")

    ChrTalk(    #90
        0xFE,
        "I-I almost fell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Ahhh, that was scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9D")

    label("loc_1F59")


    ChrTalk(    #92
        0xFE,
        "*pant* *pant* Ahhh, that was scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "I-I almost fell.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1F9D")

    Jump("loc_20BF")

    label("loc_1FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_20BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2020")
    SetChrSubChip(0xF, 0)

    def lambda_1FB9():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1FB9)

    ChrTalk(    #94
        0xF,
        "#3SFareweeeeeell--!\x02",
    )

    CloseMessageWindow()

    def lambda_1FEC():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1FEC)

    ChrTalk(    #95
        0xF,
        "#3SMy youuuuuuuuuth--!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_20BF")

    label("loc_2020")

    SetChrSubChip(0xF, 0)

    def lambda_202B():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_202B)

    ChrTalk(    #96
        0xF,
        "#3SI hate--!\x02",
    )

    CloseMessageWindow()

    def lambda_2057():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2057)

    ChrTalk(    #97
        0xF,
        "#3SBirthday celebrations--!!\x02",
    )

    CloseMessageWindow()

    def lambda_2093():
        OP_9E(0xF, 0xF, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2093)

    ChrTalk(    #98
        0xF,
        "#3SAaaaaaghh!!!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_20BF")

    TalkEnd(0xF)
    Return()

    # Function_17_1F06 end

    def Function_18_20C3(): pass

    label("Function_18_20C3")

    SetChrName("Ricky")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20D9")
    ClearChrFlags(0x10, 0x10)
    Jump("loc_20DE")

    label("loc_20D9")

    SetChrFlags(0x10, 0x10)

    label("loc_20DE")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_21E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2169")

    ChrTalk(    #99
        0xFE,
        (
            "This guy had climbed atop the wall when\x01",
            "the earthquake hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "He was so shocked by the shaking he\x01",
            "almost fell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E5")

    label("loc_2169")


    ChrTalk(    #101
        0xFE,
        (
            "If the earthquake had been a bit stronger,\x01",
            "he might've really fallen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "At least you're lucky in one way, Anton.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_21E5")

    Jump("loc_234B")

    label("loc_21E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_234B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_22CD")

    ChrTalk(    #103
        0x10,
        (
            "My buddy Anton confessed to his favorite girl\x01",
            "during the Queen's Birthday Celebration, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "He was totally rejected in the bluntest\x01",
            "way possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "Apparently he came here to erase\x01",
            "those memories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234B")

    label("loc_22CD")


    ChrTalk(    #106
        0x10,
        "Anton... You're facing towards Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "If you hate the Birthday Celebration, at\x01",
            "least scream towards the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_234B")

    TalkEnd(0x10)
    Return()

    # Function_18_20C3 end

    def Function_19_234F(): pass

    label("Function_19_234F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_248A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243A")

    ChrTalk(    #108
        0xFE,
        "The brass seems so unconcerned about it all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "I'm really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "We've got to protect this region with\x01",
            "our guns not working, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Couldn't we at least prepare some\x01",
            "barricades, maybe?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2487")

    label("loc_243A")


    ChrTalk(    #112
        0xFE,
        "The brass seems so unconcerned about it all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "I'm really worried.\x02",
    )

    CloseMessageWindow()

    label("loc_2487")

    Jump("loc_29A7")

    label("loc_248A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_267F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2600")

    ChrTalk(    #114
        0xFE,
        (
            "I'm part of the gate guard on the capital\x01",
            "side, but right now I'm helping over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Apparently the goal is to enhance security on\x01",
            "the external side, which'd be Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I'm honored to be able to stand shoulder\x01",
            "to shoulder with Jules and Hector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Both of them are good enough that there are\x01",
            "rumors about a promotion to the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_267C")

    label("loc_2600")


    ChrTalk(    #118
        0xFE,
        "Today I'm backing up the Zeiss side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I-I'm honored to be able to stand shoulder\x01",
            "to shoulder with the senior guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267C")

    Jump("loc_29A7")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2774")

    ChrTalk(    #120
        0xFE,
        (
            "Is it true a big orbal archaism\x01",
            "appeared in the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "If something like that really is around,\x01",
            "Haken Gate or Leiston Fortress'd be\x01",
            "in danger, wouldn't they...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Who are these 'society' guys we've gotten\x01",
            "reports about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2828")

    ChrTalk(    #123
        0xFE,
        "Are you bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Apparently security this time will be a\x01",
            "cooperative effort between Colonel\x01",
            "Cid's group and the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Well, we're counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_2828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_28E1")

    ChrTalk(    #126
        0xFE,
        "C.W.O. Dale here is famous for being strict.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I mean, it's the military, so sure things are\x01",
            "gonna be a bit strict, but being that exacting\x01",
            "is a little much, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_29A7")

    ChrTalk(    #128
        0xFE,
        (
            "It's already been several months since I got\x01",
            "posted here for the Birthday Celebration, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "There's still a lot that's rough, but I've\x01",
            "gotten used to life here for the most part.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A7")

    TalkEnd(0xFE)
    Return()

    # Function_19_234F end

    def Function_20_29AB(): pass

    label("Function_20_29AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2B96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AED")

    ChrTalk(    #130
        0xFE,
        (
            "If orbments aren't working, then night\x01",
            "guard is gonna be a real nail-biter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "With no lights, there's no way to\x01",
            "see any enemies coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Apparently they sell these goggles over in Zeiss\x01",
            "that let you see even in the dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I wish they'd consider buying a couple of those\x01",
            "for our squad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B93")

    label("loc_2AED")


    ChrTalk(    #134
        0xFE,
        (
            "There are no orbment lights, so night\x01",
            "guard is really nerve-racking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I wish they'd equip us with some of those\x01",
            "glasses that let you see things in the dark.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B93")

    Jump("loc_2FE3")

    label("loc_2B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8F")

    ChrTalk(    #136
        0xFE,
        (
            "Wolpe was standing guard with me before,\x01",
            "but now he's been sent over to the Zeiss side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Seems like they're beefing up\x01",
            "security on the outer side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "It's the right move given the sit,\x01",
            "but my side's kinda lonely now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2D2B")

    label("loc_2C8F")


    ChrTalk(    #139
        0xFE,
        (
            "It's been a long time since I ended\x01",
            "up gate guarding on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "If something happens, I'd better be ready\x01",
            "to call for reinforcements immediately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2B")

    Jump("loc_2FE3")

    label("loc_2D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2DC6")

    ChrTalk(    #141
        0xFE,
        (
            "There might still be leftovers of the special\x01",
            "forces that showed up at the capital and\x01",
            "near the villa around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Be very careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE3")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2EA8")

    ChrTalk(    #143
        0xFE,
        (
            "Starting today they'll be doing patrols\x01",
            "and guard work at the capital, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Apparently guard headquarters will be\x01",
            "in the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Really feels like the signing ceremony's\x01",
            "finally approaching.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE3")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2F2C")

    ChrTalk(    #146
        0xFE,
        "Nice weather today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I'd love to take my kids and a good lunch out\x01",
            "to the villa or something on a day like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE3")

    label("loc_2F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2FE3")

    ChrTalk(    #148
        0xFE,
        (
            "Seems like there's a lot of trouble\x01",
            "with the Zeiss earthquake stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Grancel's pretty peaceful right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Ever since the coup d'etat\x01",
            "no real cases have come up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE3")

    TalkEnd(0xFE)
    Return()

    # Function_20_29AB end

    def Function_21_2FE7(): pass

    label("Function_21_2FE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #151
        0xFE,
        "Yo, Estelle, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Must be hard having to come all the way out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1011FHey, Gundolf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        "#1040FIt's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B7")

    ChrTalk(    #155
        0x106,
        "#050FOn patrol?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_312E")

    label("loc_30B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EC")

    ChrTalk(    #156
        0x103,
        "#020FMaking the rounds?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_312E")

    label("loc_30EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_312E")

    ChrTalk(    #157
        0x107,
        "#064FAre you in the middle of a patrol?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    label("loc_312E")


    ChrTalk(    #158
        0xFE,
        "Yeah, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Thought I'd put my legs to work and keep\x01",
            "an eye on things around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Well, you guys can focus on your own mission.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "Leave the general upkeep to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1002FYeah, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        (
            "#1040FMuch appreciated.\x02\x03",

            "Well, then, pardon us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #164
        0xFE,
        "Yeah, best of luck to you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x20D1)
    Jump("loc_3448")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3317")

    ChrTalk(    #165
        0xFE,
        (
            "In the current situation, anything could\x01",
            "happen anywhere, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I'm putting my legs to work and trying to\x01",
            "keep things as safe as I can around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_3317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C0")

    ChrTalk(    #167
        0xFE,
        "Hey, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Seems like you're doin' bits\x01",
            "of work here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Well, nothing wrong with goin' all out,\x01",
            "but don't take on too much work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3448")

    label("loc_33C0")


    ChrTalk(    #170
        0xFE,
        (
            "Seems like you're doin' bits\x01",
            "of work here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Well, nothing wrong with goin' all out,\x01",
            "but don't take on too much work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3448")

    TalkEnd(0xFE)
    Return()

    # Function_21_2FE7 end

    def Function_22_344C(): pass

    label("Function_22_344C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_345D")
    Call(0, 24)

    label("loc_345D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0xC6, 0x0, 0x64)
    OP_6F(0x4, 100)
    OP_72(0x4, 0x10)
    SetChrPos(0x9, 22890, 7250, -24590, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 23390, 7250, -23090, 180)
    SetChrPos(0xF7, 22390, 7250, -23090, 180)
    SetChrPos(0x104, 23390, 7250, -22090, 180)
    SetChrPos(0x105, 22390, 7250, -22090, 180)
    OP_6D(22650, 7250, -20770, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(315000, 0)
    OP_6E(427, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    Sleep(2500)

    def lambda_3526():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3526)
    Sleep(80)

    def lambda_3546():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3546)
    Sleep(120)

    def lambda_3566():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB9B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3566)
    Sleep(80)

    def lambda_3586():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3586)
    Sleep(120)

    def lambda_35A6():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35A6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x104, 0x1)
    OP_6A(0xFF)
    Fade(1000)
    OP_6D(22860, 7250, -41960, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(220000, 0)
    OP_6E(427, 0)
    OP_0D()

    ChrTalk(    #172
        0x9,
        (
            "#6P...By the time I screwed up my courage\x01",
            "and came out, he was nowhere to be seen.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #173
        0x9,
        (
            "#6PIn other words, I lost him.\x01",
            "But...I lost him HERE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1020F#6PLost? But...wait a sec!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        (
            "#043F#2PHow is that possible?\x01",
            "This is a dead end, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#6PYeah! And there's no way he could've\x01",
            "jumped down from this height, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#6PI figured I made a mistake and\x01",
            "thought he went elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#6PI looked all over Sanktheim for him,\x01",
            "but I never saw him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#6PKinda makes ME want to jump off\x01",
            "the end, there. I missed my chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x104,
        (
            "#035F#2PAh, you poor kitten.\x02\x03",

            "#037FIf it would please you, I could help\x01",
            "you forget such lesser men...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #181
        0x101,
        (
            "#1019F#6PKnock it off. No one deserves\x01",
            "that kind of trauma.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_396D")

    ChrTalk(    #182
        0x106,
        (
            "#053F#4PAnyway... Think we have a pretty\x01",
            "good idea of what happened.\x02\x03",

            "#051FThanks. Sorry we had to\x01",
            "drag you out here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39DF")

    label("loc_396D")


    ChrTalk(    #183
        0x103,
        (
            "#026F#4PI think we have a fairly good\x01",
            "idea of what happened now.\x02\x03",

            "#526FYou were a big help.\x01",
            "Thank you again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39DF")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #184
        0x9,
        "#6PHaha! You're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        "#6PSo, um, is he some kind of wanted man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#6PA super-skilled, cold-blooded assassin\x01",
            "on the run from the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1016F#6PI, uh, dunno about that...but he's\x01",
            "definitely a dangerous guy.\x02\x03",

            "#1002FLook, if you see him again, don't\x01",
            "go near him, okay? Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        "#6PBut he's so cool! Aww... Oh, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#6PAnyway, I've got some things\x01",
            "to prepare, so excuse me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        "#6PKeep up the good work, everyone!\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x17)

    def lambda_3BB7():

        label("loc_3BB7")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BB7")

    QueueWorkItem2(0x101, 1, lambda_3BB7)

    def lambda_3BC8():

        label("loc_3BC8")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BC8")

    QueueWorkItem2(0xF7, 1, lambda_3BC8)

    def lambda_3BD9():

        label("loc_3BD9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BD9")

    QueueWorkItem2(0x105, 1, lambda_3BD9)

    def lambda_3BEA():

        label("loc_3BEA")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BEA")

    QueueWorkItem2(0x104, 1, lambda_3BEA)
    Sleep(1000)

    def lambda_3C00():
        OP_6D(23080, 7250, -38000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C00)
    WaitChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    def lambda_3C3C():
        OP_6D(23080, 7250, -40700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C3C)
    OP_8C(0x104, 225, 400)
    OP_8C(0xF7, 45, 400)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #191
        0x105,
        (
            "#047F'There's no way he could've jumped\x01",
            "down from this height,' huh...\x02\x03",

            "#042FEstelle...does that remind you of anyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1003F#6PYeah...\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C6, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    Sleep(1000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1002F#6PThat silver-haired...monster who jumped\x01",
            "off the top of Grancel Castle.\x01",
            "The man we know as 'Lorence.'\x02\x03",

            "If the other ones are like him, I think\x01",
            "they COULD jump from here and survive.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E41")

    ChrTalk(    #194
        0x106,
        (
            "#057F#6PYeah.\x02\x03",

            "Don't think there's any doubt about\x01",
            "who our 'sunglasses guy' is now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9C")

    label("loc_3E41")


    ChrTalk(    #195
        0x103,
        (
            "#022F#6PYes...\x02\x03",

            "I think it's safe to assume we know\x01",
            "who our 'wild sunglasses man' is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9C")


    ChrTalk(    #196
        0x104,
        (
            "#035F#6PAnother Enforcer of Ouroboros,\x01",
            "just like the Phantom Thief, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F62")

    ChrTalk(    #197
        0x106,
        (
            "#053F#6PNo doubt about it.\x02\x03",

            "#050FWe're definitely done investigating.\x01",
            "Let's get back to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4004")

    label("loc_3F62")


    ChrTalk(    #198
        0x103,
        (
            "#026F#6PI feel pretty confident saying\x01",
            "that at this point, yes.\x02\x03",

            "#020FI also feel confident saying we're done\x01",
            "investigating. Let's return to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4004")

    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(23030, 7250, -40170, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 23060, 7250, -40220, 16)
    SetChrPos(0x1, 23060, 7250, -40220, 16)
    SetChrPos(0x2, 23060, 7250, -40220, 16)
    SetChrPos(0x3, 23060, 7250, -40220, 16)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_6F(0x4, 0)
    OP_71(0x4, 0x10)
    OP_A2(0x1416)
    OP_28(0x86, 0x1, 0x20)
    OP_28(0x86, 0x1, 0x40)
    OP_28(0x86, 0x1, 0x80)
    OP_28(0x86, 0x1, 0x100)
    Sleep(1000)
    OP_21()
    OP_1D(0x10)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_22_344C end

    def Function_23_40D8(): pass

    label("Function_23_40D8")


    def lambda_40DE():
        OP_8E(0xFE, 0x5F50, 0x1C52, 0xFFFF5D1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40DE)
    WaitChrThread(0x9, 0x1)

    def lambda_40FE():
        OP_8E(0xFE, 0x5EEC, 0x1C52, 0xFFFF8EB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40FE)
    WaitChrThread(0x9, 0x1)
    Return()

    # Function_23_40D8 end

    def Function_24_4119(): pass

    label("Function_24_4119")

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
        (0, "loc_4192"),
        (1, "loc_4198"),
        (SWITCH_DEFAULT, "loc_419E"),
    )


    label("loc_4192")

    OP_A2(0x1200)
    Jump("loc_419E")

    label("loc_4198")

    OP_A2(0x1201)
    Jump("loc_419E")

    label("loc_419E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_41AC")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_41B0")

    label("loc_41AC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_41B0")

    Return()

    # Function_24_4119 end

    def Function_25_41B1(): pass

    label("Function_25_41B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4333")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4235")

    ChrTalk(    #199
        0x101,
        (
            "#1002FOur investigations here aren't finished.\x02\x03",

            "Let's hurry up and get the questioning done with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4318")

    label("loc_4235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_42A9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4252")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_4259")

    label("loc_4252")

    TurnDirection(0x106, 0x0, 400)

    label("loc_4259")


    ChrTalk(    #200
        0x106,
        (
            "#050FOur investigation here ain't over.\x02\x03",

            "Let's get back to questionin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4318")

    label("loc_42A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42BF")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_42C6")

    label("loc_42BF")

    TurnDirection(0x103, 0x0, 400)

    label("loc_42C6")


    ChrTalk(    #201
        0x103,
        (
            "#020FOur investigation here isn't over.\x02\x03",

            "We need to continue the interviews.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4318")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4333")

    Return()

    # Function_25_41B1 end

    def Function_26_4334(): pass

    label("Function_26_4334")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_26_4334 end

    SaveToFile()

Try(main)
