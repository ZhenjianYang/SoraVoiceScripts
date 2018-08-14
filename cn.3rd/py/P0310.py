from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P0310   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '封印石②',                             # 9
        '凯文',                                 # 10
        '莉丝',                                 # 11
        '提妲',                                 # 12
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 13
        '穆拉',                                 # 14
        '乔丝特',                               # 15
        '约修亚',                               # 16
        '科洛丝',                               # 17
        '基库',                                 # 18
        '奥利维尔',                             # 19
        '金',                                   # 20
        '亚妮拉丝',                             # 21
        '雪拉扎德',                             # 22
        '阿加特',                               # 23
        '艾丝蒂尔',                             # 24
        '理查德',                               # 25
        '玲',                                   # 26
        '赛雷斯托',                             # 27
        '基尔巴特',                             # 28
        '临时用尤莉亚',                         # 29
        '',                                     # 30
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02891 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03470 ._CH',             # 02
        'ED6_DT26/CH20743 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT26/CH20742 ._CH',             # 06
        'ED6_DT26/CH20741 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT27/CH03000 ._CH',             # 0F
        'ED6_DT26/CH20740 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT27/CH03750 ._CH',             # 12
        'ED6_DT26/CH20500 ._CH',             # 13
        'ED6_DT26/CH20454 ._CH',             # 14
        'ED6_DT26/CH20621 ._CH',             # 15
        'ED6_DT07/CH02895 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH02891P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03470P._CP',             # 02
        'ED6_DT26/CH20743P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT26/CH20742P._CP',             # 06
        'ED6_DT26/CH20741P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT27/CH03000P._CP',             # 0F
        'ED6_DT26/CH20740P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT27/CH03750P._CP',             # 12
        'ED6_DT26/CH20500P._CP',             # 13
        'ED6_DT26/CH20454P._CP',             # 14
        'ED6_DT26/CH20621P._CP',             # 15
        'ED6_DT07/CH02895P._CP',             # 16
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1910,
        Z                   = 2000,
        Y                   = 90260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 2000,
        Y                   = 90150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3630,
        Z                   = 200,
        Y                   = 97420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1090,
        Z                   = 2200,
        Y                   = 93560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1630,
        Z                   = 250,
        Y                   = 97420,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196627,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1300,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2200,
        Z                   = 2000,
        Y                   = 91600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1930,
        Z                   = 2000,
        Y                   = 86990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 230,
        Z                   = 2000,
        Y                   = 87070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -920,
        Z                   = 2000,
        Y                   = 88300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 120,
        Z                   = 2000,
        Y                   = 88300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3150,
        Z                   = 2000,
        Y                   = 87000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 2000,
        Y                   = 88740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 100,
        Y                   = 99020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3010,
        Z                   = 2000,
        Y                   = 88790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -210,
        Z                   = 2500,
        Y                   = 91540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1230,
        Z                   = 2000,
        Y                   = 85800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1090,
        Z                   = 2200,
        Y                   = 93300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -1120,
        TriggerZ            = 2000,
        TriggerY            = 93910,
        TriggerRange        = 1000,
        ActorX              = -1120,
        ActorZ              = 3300,
        ActorY              = 93910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_56E",          # 01, 1
        "Function_2_68D",          # 02, 2
        "Function_3_6A3",          # 03, 3
        "Function_4_927",          # 04, 4
        "Function_5_950",          # 05, 5
        "Function_6_979",          # 06, 6
        "Function_7_A30",          # 07, 7
        "Function_8_DF6",          # 08, 8
        "Function_9_F81",          # 09, 9
        "Function_10_FCC",         # 0A, 10
        "Function_11_100E",        # 0B, 11
        "Function_12_1050",        # 0C, 12
        "Function_13_1097",        # 0D, 13
        "Function_14_1DF8",        # 0E, 14
        "Function_15_26CD",        # 0F, 15
        "Function_16_2DD5",        # 10, 16
        "Function_17_38BB",        # 11, 17
        "Function_18_4193",        # 12, 18
        "Function_19_41F0",        # 13, 19
        "Function_20_44D7",        # 14, 20
        "Function_21_4E86",        # 15, 21
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44C")
    OP_A3(0x2504)
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 21)
    Jump("loc_56D")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_472")
    OP_A3(0x2504)
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)
    Jump("loc_56D")

    label("loc_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_491")
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 19)
    Jump("loc_56D")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_4B0")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 17)
    Jump("loc_56D")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_4CF")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_56D")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_4EE")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_56D")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_50D")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_56D")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_52C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_56D")

    label("loc_52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_542")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_56D")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_558")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_56D")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_56D")

    Return()

    # Function_0_426 end

    def Function_1_56E(): pass

    label("Function_1_56E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 0)), scpexpr(EXPR_END)), "loc_581")
    OP_B1("P0310_1")
    Jump("loc_5B8")

    label("loc_581")

    OP_B1("P0310_2")
    OP_76(0xFF, 0x12, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x15, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC")
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x1017, 0x0)
    ExitThread()

    label("loc_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_688")
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -1120, 3200, 93910, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_68C")

    label("loc_688")

    OP_64(0x0, 0x1)

    label("loc_68C")

    Return()

    # Function_1_56E end

    def Function_2_68D(): pass

    label("Function_2_68D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A2")
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Jump("Function_2_68D")

    label("loc_6A2")

    Return()

    # Function_2_68D end

    def Function_3_6A3(): pass

    label("Function_3_6A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 160, 150, 9100, 180)
    SetChrPos(0x10F, 160, 150, 9100, 180)
    SetChrPos(0x107, 160, 150, 9100, 180)
    OP_6D(1370, 0, -5520, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    FadeToBright(2000, 0)

    def lambda_72E():
        OP_6D(620, 0, 6230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72E)

    def lambda_746():
        OP_67(0, 5990, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_746)

    def lambda_75E():
        OP_6B(2990, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_75E)

    def lambda_76E():
        OP_6E(267, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_76E)
    Sleep(3000)
    OP_72(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 0)
    OP_70(0x16, 0xF)
    OP_73(0x16)
    Sleep(300)

    def lambda_79F():
        OP_8E(0xFE, 0xFFFFFF88, 0x0, 0x11A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_79F)
    Sleep(500)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_43(0x107, 0x0, 0x0, 0x5)
    Sleep(1000)
    OP_71(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 15)
    OP_70(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        (
            "#1446F#5P没有人的气息……\x02\x03",

            "#1440F至少最近几天\x01",
            "应该没人来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#063F主要系统的导力\x01",
            "似乎也完全停止了。\x02\x03",

            "是不是导力引擎\x01",
            "发生了什么异常呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1065F#6P唔……\x01",
            "总之先进去调查看看吧。\x02\x03",

            "#1063F说不定有什么线索。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2613)
    OP_28(0x29, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_6A3 end

    def Function_4_927(): pass

    label("Function_4_927")

    OP_8F(0xFE, 0xFFFFFFC4, 0x0, 0x1D60, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFB82, 0x0, 0x1540, 0x7D0, 0x0)
    Return()

    # Function_4_927 end

    def Function_5_950(): pass

    label("Function_5_950")

    OP_8F(0xFE, 0xFFFFFFC4, 0x0, 0x1D60, 0x7D0, 0x0)
    OP_8F(0xFE, 0x15E, 0x0, 0x17E8, 0x7D0, 0x0)
    Return()

    # Function_5_950 end

    def Function_6_979(): pass

    label("Function_6_979")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    SetChrFlags(0x107, 0x80)
    OP_6D(150, 2150, 50240, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_22(0x9C, 0x0, 0x64)
    OP_0D()
    OP_72(0x1017, 0x0)
    ExitThread()
    OP_6F(0x17, 0)
    OP_70(0x17, 0xF)
    OP_73(0x17)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1017, 0x0)
    ExitThread()
    OP_A2(0x2616)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_979 end

    def Function_7_A30(): pass

    label("Function_7_A30")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x109, -1000, 2000, 94980, 180)
    SetChrPos(0x10F, -70, 2000, 94000, 270)
    SetChrPos(0x107, -1930, 2000, 93500, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(-410, 2000, 94840, 0)
    OP_67(0, 6770, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFFFC18, 0xC80, 0x17188, 0x1F4, 0x0)
    Sleep(1000)

    ChrTalk(    #3
        0x109,
        "#1067F#5P……又是这个吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x107,
        (
            "#560F#6P哇，好漂亮……\x02\x03",

            "这是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1446F#2P『封印石』……\x02\x03",

            "#1448F和那块把提妲\x01",
            "关起来的石头\x01",
            "应该是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        (
            "#064F#6P是、是这样吗！？\x02\x03",

            "#066F我……\x01",
            "曾经待在这么漂亮的石头里面啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x10, 0x80)
    Sleep(1000)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x53\x03\x07\x00。\x02",
    )

    Jump("loc_C67")

    label("loc_C67")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x353, 1)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1065F#5P好了……\x01",
            "如果这也是『规则』的话，\x01",
            "那么要做的事只有一件。\x02\x03",

            "#1840F暂时回一趟据点\x01",
            "把这块石头解放吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1448F#2P……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        "#560F#6P好、好的！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2619)
    OP_28(0x29, 0x1, 0x800)
    OP_64(0x0, 0x1)
    OP_6D(-1090, 2000, 91550, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1090, 2000, 91550, 180)
    SetChrPos(0x1, -1090, 2000, 91550, 180)
    SetChrPos(0x2, -1090, 2000, 91550, 180)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_A30 end

    def Function_8_DF6(): pass

    label("Function_8_DF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -1100, 2000, 83500, 0)
    SetChrPos(0x10F, -1100, 2000, 83500, 0)
    SetChrPos(0x107, -1100, 2000, 83500, 0)
    SetChrPos(0x10E, -1100, 2000, 83500, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-900, 2000, 84250, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(254, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_EC9():
        OP_6D(740, 1600, 94700, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EC9)

    def lambda_EE1():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EE1)

    def lambda_EF9():
        OP_6B(3310, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_EF9)

    def lambda_F09():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_F09)

    def lambda_F19():
        OP_6E(275, 4000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_F19)
    OP_43(0x10E, 0x0, 0x0, 0x9)
    Sleep(800)
    OP_43(0x109, 0x0, 0x0, 0xA)
    Sleep(1000)
    OP_43(0x10F, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0xC)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_DF6 end

    def Function_9_F81(): pass

    label("Function_9_F81")


    def lambda_F87():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F87)
    OP_8E(0xFE, 0xFFFFFACE, 0x7D0, 0x1631E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    Return()

    # Function_9_F81 end

    def Function_10_FCC(): pass

    label("Function_10_FCC")


    def lambda_FD2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD2)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF786, 0x7D0, 0x15C84, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_FCC end

    def Function_11_100E(): pass

    label("Function_11_100E")


    def lambda_1014():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1014)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF42, 0x7D0, 0x15AAE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_100E end

    def Function_12_1050(): pass

    label("Function_12_1050")


    def lambda_1056():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1056)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFF9CA, 0x7D0, 0x155AE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_1050 end

    def Function_13_1097(): pass

    label("Function_13_1097")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mpU70_03.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(5820, 0, 105730, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)

    def lambda_11CA():
        OP_6D(500, 2000, 93390, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_11CA)

    def lambda_11E2():
        OP_67(0, 5470, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_11E2)

    def lambda_11FA():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_11FA)

    def lambda_120A():
        OP_6E(315, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_120A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x14,
        "#176F#5P……配置完毕。\x02",
    )

    CloseMessageWindow()

    def lambda_1251():
        OP_6D(1000, 2000, 93000, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1251)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x18, 90, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(30)

    ChrTalk(    #12
        0x18,
        (
            "#1162F#6P始祖大人。\x01",
            "请开始吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12AA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_12AA)
    Sleep(100)

    def lambda_12BD():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12BD)
    Sleep(100)

    def lambda_12D0():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12D0)
    Sleep(100)
    OP_8C(0x21, 45, 400)
    Sleep(300)

    ChrTalk(    #13
        0x22,
        (
            "#1615F#5P#12C──明白了。\x02\x03",

            "#1610F那么各位……\x01",
            "请集中精神。\x02\x03",

            "这片『白翼』\x01",
            "在天空中飞舞的姿态……\x02\x03",

            "请各位在心中\x01",
            "仔细描绘。#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#1078F#6P明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1F,
        (
            "#1016F#6P啊哈哈……\x01",
            "似乎很容易就能想像出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#1932F#12P虽然是第一次见到这艘船……\x01",
            "但一定是非常美丽的光景吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x23,
        (
            "#1224F#11P这、这么说来……\x02\x03",

            "#1223F以前被逮捕的时候\x01",
            "就是被这艘船带到了\x01",
            "雷斯顿要塞去的吧……\x02\x03",

            "#1228F可恶，从那之后\x01",
            "我的人生就一片混乱……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14D3():
        OP_6D(1000, 2000, 92000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_14D3)

    def lambda_14EB():
        OP_67(0, 5180, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_14EB)

    def lambda_1503():
        OP_6B(3080, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1503)

    def lambda_1513():
        OP_6E(323, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1513)
    OP_8C(0x22, 180, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #18
        0x22,
        (
            "#1615F#5P#12C那位先生……\x01",
            "请协助我们。\x02\x03",

            "#1610F如果大家的思想不能合而为一，\x01",
            "这片『翼』便无法苏醒……\x02\x03",

            "……莫非你想\x01",
            "一个人留在『庭院』？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_15EF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15EF)
    Sleep(50)

    def lambda_1602():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1602)
    Sleep(50)
    SetChrFlags(0x18, 0x20)

    def lambda_161A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_161A)
    Sleep(50)

    def lambda_162D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_162D)
    Sleep(50)

    def lambda_1640():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1640)
    Sleep(50)

    def lambda_1653():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1653)
    Sleep(50)

    def lambda_1666():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1666)
    Sleep(50)

    def lambda_1679():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1679)
    Sleep(50)

    def lambda_168C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_168C)
    Sleep(50)

    def lambda_169F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_169F)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #19
        0x23,
        (
            "#1224F#12P我帮忙！\x01",
            "我一定帮忙！\x02\x03",

            "#1228F真是的……（嘀嘀咕咕）……\x01",
            "……为什么连我也要这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1F,
        "#1007F#5P哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x21,
        (
            "#1306F#5P嘻嘻……\x01",
            "真是有趣的哥哥啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_20(0x7D0)

    def lambda_1796():
        OP_6D(1000, 2000, 93000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1796)

    def lambda_17AE():
        OP_67(0, 5470, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_17AE)

    def lambda_17C6():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_17C6)

    def lambda_17D6():
        OP_6E(315, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_17D6)
    OP_8C(0x22, 0, 400)
    Sleep(50)

    def lambda_17F2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17F2)
    Sleep(50)

    def lambda_1805():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1805)
    Sleep(50)

    def lambda_1818():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1818)
    Sleep(50)

    def lambda_182B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_182B)
    Sleep(50)

    def lambda_183E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_183E)
    Sleep(50)

    def lambda_1851():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1851)
    Sleep(50)

    def lambda_1864():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1864)
    Sleep(50)

    def lambda_1877():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1877)
    Sleep(50)

    def lambda_188A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_188A)
    Sleep(50)

    def lambda_189D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_189D)
    WaitChrThread(0xEE, 0x0)
    ClearChrFlags(0x18, 0x20)
    Sleep(500)
    OP_21()

    ChrTalk(    #22
        0x22,
        (
            "#1616F#5P#12C……好了。\x01",
            "那就开始吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x22, 22)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_1D(0x99)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x1, 0xFF, 0x11, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x12, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x13, 0, 600, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x14, 0, 600, -200, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x15, -100, 600, -100, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x16, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 0, 1000, 0, 0, 0, 0, 1500, 2800, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 0, 700, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x11,
        "#1079F#6P哦哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        "#1934F#12P这、这是……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C28)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    OP_79(0x14, 0x2)
    OP_79(0x15, 0x2)
    OP_79(0x16, 0x2)
    OP_79(0x17, 0x2)
    OP_79(0x18, 0x2)
    OP_7A(0x19, 0x2)
    OP_7A(0x1A, 0x2)
    OP_7A(0x1B, 0x2)
    OP_78(0xE6, 0xFA, 0xFF)
    OP_7B()
    OP_76(0xFF, 0x12, 0x2, 0x4, 0x8, 0x64, 0x0, 0xF)
    OP_76(0xFF, 0x15, 0x2, 0x4, 0x8, 0x64, 0x0, 0xF)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1097 end

    def Function_14_1DF8(): pass

    label("Function_14_1DF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mpU70_03.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x22, 22)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    PlayEffect(0x1, 0xFF, 0x22, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x11, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x12, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x13, 0, 500, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x14, 0, 600, -200, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x15, -200, 500, -100, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x16, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 0, 1000, 0, 0, 0, 0, 1500, 2800, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 0, 700, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)
    LoadEffect(0x1, "map\\mp049_21.eff")
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x14,
        (
            "#179F#5P──启动完毕。\x02\x03",

            "#171F『埃尔赛尤』……\x01",
            "随时可以出发。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x18,
        "基库",
        "#311F#5P啾！\x02",
    )

    Jump("loc_23AB")

    label("loc_23AB")

    CloseMessageWindow()

    ChrTalk(    #27
        0x13,
        "#061F#11P成功了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x17,
        (
            "#1514F#5P呼……\x01",
            "真是紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x20,
        "#119F#5P这样就准备好了吗……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x18, 180, 400)
    Sleep(300)

    ChrTalk(    #30
        0x18,
        (
            "#1382F#5P凯文先生……\x01",
            "接下来打算怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#1075F#6P嗯……\x01",
            "就这样出发吧。\x02\x03",

            "#1063F前往『星层』的外侧──\x01",
            "『影之王』所在的\x01",
            "无尽荒野之彼端。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x18,
        "#1383F#5P明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 0, 400)
    ClearChrFlags(0x18, 0x20)
    Sleep(300)

    ChrTalk(    #33
        0x18,
        (
            "#1162F#6P尤莉亚小姐，\x01",
            "那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #34
        0x14,
        "#170F#5P明白。\x02",
    )

    CloseMessageWindow()

    def lambda_2573():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2573)

    def lambda_258B():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_258B)

    def lambda_25A3():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_25A3)

    def lambda_25B3():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_25B3)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)
    Sleep(150)

    ChrTalk(    #35
        0x14,
        (
            "#176F#11P王室亲卫队所属，\x01",
            "巡洋舰『埃尔赛尤』──\x02\x03",

            "#178F现在以最大战速\x01",
            "脱离『星层』。\x02\x03",

            "启动引擎，开始出击。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)
    SetChrName("临时机组成员们")

    AnonymousTalk(    #36
        "\x07\x00#4S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1DF8 end

    def Function_15_26CD(): pass

    label("Function_15_26CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(45000, 0)
    OP_6E(319, 0)

    def lambda_27ED():

        label("loc_27ED")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_27ED")

    QueueWorkItem2(0xEE, 0, lambda_27ED)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #37
        0x1C,
        "#814F#11P好、好厉害……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x15,
        "#277F#5P这就是『星层』真正的姿态吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1A,
        (
            "#1541F#11P呼……\x01",
            "简直像万花筒一样呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28DF():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_28DF)

    def lambda_28F7():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_28F7)

    def lambda_290F():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_290F)

    def lambda_291F():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_291F)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #40
        0x16,
        (
            "#210F#11P时速３０００、３１００、３２００……\x02\x03",

            "#216F等、等一下！\x01",
            "３５００……３８００……４３００……\x02\x03",

            "到达时速５０００塞尔矩！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x14,
        "#173F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "#1164F#6P竟然大幅超越了现在的最高战速\x01",
            "每小时３６００塞尔矩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x22,
        (
            "#1616F#11P#12C看来已经将性能提升到\x01",
            "理论上的极限值了。\x02\x03",

            "#1611F这也是大家的意念\x01",
            "融为一体的证据吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13,
        "#067F#11P太、太惊人了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        (
            "#1078F#6P照这个速度要到达目的地\x01",
            "看来也无需多少时间呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#1938F#11P……我们还没脱离\x01",
            "『星层』的领域吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x20,
        (
            "#110F#5P不……\x01",
            "距离上来说应该差不多了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)

    ChrTalk(    #48
        0x16,
        (
            "#214F#11P前方发现带状障壁！\x02\x03",

            "再过１２０秒就会撞上了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #49
        0x14,
        (
            "#176F#6P引擎保持全速，主炮发射准备！\x02\x03",

            "#172F用连续炮击\x01",
            "强行突破障壁！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x15,
        "#271F#5P#3S了解！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_26CD end

    def Function_16_2DD5(): pass

    label("Function_16_2DD5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(5820, 0, 104730, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)

    def lambda_2EF5():

        label("loc_2EF5")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_2EF5")

    QueueWorkItem2(0xEE, 0, lambda_2EF5)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()

    def lambda_2F1E():
        OP_6D(500, 2000, 93390, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2F1E)

    def lambda_2F36():
        OP_6D(1000, 2000, 93000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2F36)

    def lambda_2F4E():
        OP_67(0, 4370, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2F4E)

    def lambda_2F66():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2F66)

    def lambda_2F76():
        OP_6E(315, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2F76)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #51
        0x1E,
        "#052F#6P……这是………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        "#1942F#11P这就是『星层』的外侧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1D,
        "#1522F#11P真是寸草不生的荒野啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x22,
        (
            "#1615F#5P#12C目的地的坐标\x01",
            "与之前所说的一致。\x02\x03",

            "#1610F照这样笔直前进\x01",
            "很快就会到达的吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x1F,
        (
            "#1016F#6P呼……\x01",
            "这下就能松一口气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x21,
        (
            "#261F#6P嘻嘻……\x01",
            "还挺刺激的。\x02\x03",

            "#265F能快到如此地步的飞艇\x01",
            "连『结社』也没有呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #57
        0x1B,
        (
            "#074F#11P不过这等辽阔……\x02\x03",

            "#072F没想到所谓『影之国』\x01",
            "竟然是如此广大的地域。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x1A,
        (
            "#1545F#6P嗯，这居然只是\x01",
            "『辉之环』的子系统……\x02\x03",

            "#1540F我越来越\x01",
            "无法相信\x01",
            "『环』已经消失了呢。\x02",
        )
    )

    Jump("loc_31F2")

    label("loc_31F2")

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#1841F#5P嗯……\x01",
            "我也有同感。\x02\x03",

            "#1063F如果那么简单就能消失，\x01",
            "这规模也实在大过头了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24016C, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #60
        0x11,
        (
            "#1067F#5P（果然……\x01",
            "  那个时候回收的就是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x1F,
        "#1004F#6P凯文先生，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #62
        0x11,
        (
            "#1075F#5P不……\x01",
            "没什么大不了的。\x02\x03",

            "#1060F和这次的事件\x01",
            "应该没有直接联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1F,
        "#1015F？#6P\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)

    def lambda_3382():
        OP_6D(760, 1800, 96310, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3382)

    def lambda_339A():
        OP_67(0, 4800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_339A)

    def lambda_33B2():
        OP_6B(3030, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_33B2)

    def lambda_33C2():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_33C2)
    LoadEffect(0x1, "map\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)

    def lambda_3441():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3441)
    WaitChrThread(0xEE, 0x0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #64
        0x16,
        "#216F#11P这、这是什么……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #65
        0x16,
        (
            "#214F#11P#2S后方２００塞尔矩处\x01",
            "感知到小型飞行物体！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x14,
        "#173F#11P你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x18,
        (
            "#1163F#11P在、在这种地方\x01",
            "会有其它飞艇……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x22,
        (
            "#1613F#11P#12C……不。\x02\x03",

            "#1612F看来似乎是从\x01",
            "『星层』来的追击者呢。#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "#1847F#6P追击者……！？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #70
        0x14,
        (
            "#172F#6P展开监视器！\x02\x03",

            "用后部摄像机\x01",
            "捕捉飞行物体！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x17,
        "#1502F#5P……明白！\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)

    def lambda_3819():
        OP_67(0, 5150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3819)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    Sleep(50)
    OP_22(0x127, 0x0, 0x64)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_73(0xC)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x4)
    OP_74(0xC, 0x8, 0x4)
    OP_74(0xC, 0xA, 0x4)
    OP_0D()
    OP_1D(0x9D)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2509)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2DD5 end

    def Function_17_38BB(): pass

    label("Function_17_38BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_3A14():

        label("loc_3A14")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_3A14")

    QueueWorkItem2(0xEE, 0, lambda_3A14)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x1F,
        "#1020F#6P那、那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x17,
        "#1506F#5P白银德尔基昂……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD0")

    ChrTalk(    #74
        0x21,
        (
            "#267F#6P嗯……\x01",
            "是从来没见过的颜色呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD0")


    ChrTalk(    #75
        0x16,
        (
            "#212F#11P糟糕了……\x01",
            "它的速度比埃尔赛尤要快。\x02\x03",

            "这样下去会被捕捉到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x15,
        (
            "#276F#5P……被缠上了可就麻烦了。\x02\x03",

            "那种机体曾经\x01",
            "击落过埃尔赛尤号一次。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3C01")

    ChrTalk(    #77
        0x21,
        (
            "#267F#6P嗯……\x01",
            "虽然可以把帕蒂尔·玛蒂尔叫出来……\x02\x03",

            "#268F可是在空中的机动性\x01",
            "似乎也跟不上那孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C01")


    ChrTalk(    #78
        0x14,
        "#175F#6P……唔…………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #79
        0x14,
        (
            "#177F#11P准备空战！\x01",
            "调转方向迎击敌方龙机！\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #80
        0x23,
        (
            "#1226F#11P……不。\x01",
            "你们不必如此。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3E27():
        OP_6D(3080, 0, 92930, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3E27)

    def lambda_3E3F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3E3F)
    Sleep(50)

    def lambda_3E52():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3E52)
    Sleep(50)

    def lambda_3E65():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3E65)
    Sleep(50)
    SetChrFlags(0x18, 0x20)

    def lambda_3E7D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3E7D)
    Sleep(50)

    def lambda_3E90():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3E90)
    Sleep(50)

    def lambda_3EA3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3EA3)
    Sleep(50)

    def lambda_3EB6():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3EB6)
    Sleep(50)

    def lambda_3EC9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3EC9)
    Sleep(50)

    def lambda_3EDC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3EDC)
    Sleep(50)

    def lambda_3EEF():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3EEF)
    Sleep(50)

    def lambda_3F02():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3F02)
    Sleep(50)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #81
        0x14,
        "#173F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x11,
        (
            "#1063F#5P怎、怎么了小哥……\x01",
            "这么没头没脑的来一句。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x23,
        (
            "#1226F#12P呼呼呼……\x02\x03",

            "#1221F……看来终于\x01",
            "是时候向你们展示\x01",
            "我的真正实力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        "#1064F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x1F,
        "#1019F#5P你、你没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "#1942F#5P……是不是到下面的\x01",
            "医务室休息一下比较好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x23,
        (
            "#1221F#12P哈哈哈！\x01",
            "哼，你们就看着吧！\x02\x03",

            "真正的英雄活跃的英姿！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 180, 400)
    OP_43(0x23, 0x0, 0x0, 0x12)
    Sleep(500)

    def lambda_40C7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_40C7)
    Sleep(100)

    def lambda_40DA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_40DA)
    Sleep(100)

    def lambda_40ED():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_40ED)
    Sleep(100)

    def lambda_4100():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4100)
    WaitChrThread(0x23, 0x0)
    Sleep(1500)

    def lambda_4118():
        OP_6D(3080, 0, 92930, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4118)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #88
        0x1C,
        "#814F…#5P…走掉了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x1F,
        "#1007F#5P什、什么啊……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_38BB end

    def Function_18_4193(): pass

    label("Function_18_4193")

    OP_8E(0xFE, 0xFFFFFB78, 0x7D0, 0x14D16, 0xBB8, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_41B7():
        OP_6D(3080, 0, 91500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_41B7)

    def lambda_41CF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41CF)
    OP_8E(0xFE, 0xFFFFFB14, 0x7D0, 0x14730, 0xFA0, 0x0)
    Return()

    # Function_18_4193 end

    def Function_19_41F0(): pass

    label("Function_19_41F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_4334():

        label("loc_4334")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_4334")

    QueueWorkItem2(0xEE, 0, lambda_4334)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #90
        0x1F,
        "#1004F#6P……………………（张大嘴）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        "#1079F#6P那个时候的人形兵器……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        "#1934F#12P没想到里面居然可以让人乘坐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x16,
        (
            "#214F#11P那、那架机体……！？\x02\x03",

            "果然袭击山猫号的\x01",
            "就是那家伙啊……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x21,
        (
            "#263F#6P唔，不过他的想法不错。\x02\x03",

            "#1306F如果单论机动性的话，\x01",
            "那个倒是和德尔基昂平分秋色。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x250B)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_41F0 end

    def Function_20_44D7(): pass

    label("Function_20_44D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_461B():

        label("loc_461B")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_461B")

    QueueWorkItem2(0xEE, 0, lambda_461B)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #95
        0x12,
        "#1934F#12P漂亮……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x1D,
        "#1536F#12P嘿，有一手嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x1E,
        (
            "#051F#6P嘿……\x01",
            "本以为他不过是个普通的笨蛋，\x01",
            "没想到还挺有本事的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x1C,
        (
            "#811F#12P嗯嗯！\x01",
            "真是刮目相看了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x15,
        (
            "#276F#5P唔，不过要靠那个击坠对方\x01",
            "似乎也有一定难度啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x14,
        (
            "#176F#6P……是啊。\x02\x03",

            "#178F我们还是准备\x01",
            "调转方向迎击比较……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #101
        (
            "\x07\x05……我不是说了\x01",
            "不必如此吗！\x02",
        )
    )

    Jump("loc_47DB")

    label("loc_47DB")

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4951():
        OP_67(0, 3950, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4951)

    def lambda_4969():
        OP_6D(200, 2400, 93390, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4969)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x6)
    OP_74(0xC, 0x8, 0x6)
    OP_74(0xC, 0xA, 0x6)
    OP_0D()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #102
        0x14,
        "#173F#6P啊。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("基尔巴特")

    AnonymousTalk(    #103
        (
            "\x07\x05别管那么多了，赶快前进！\x02\x03",

            "反正就算带着我\x01",
            "对战斗也毫无帮助！\x02\x03",

            "既然如此，就让我\x01",
            "在这里大显身手吧！\x02",
        )
    )

    Jump("loc_4A72")

    label("loc_4A72")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #104
        0x14,
        "#178F#6P……你…………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("基尔巴特")

    AnonymousTalk(    #105
        (
            "\x07\x05别担心，就算不能击毁\x01",
            "也能这样持续扰乱它。\x02\x03",

            "我会找个机会逃走\x01",
            "去追你们的。\x02",
        )
    )

    Jump("loc_4B12")

    label("loc_4B12")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #106
        0x14,
        (
            "#170F#6P………………………………\x02\x03",

            "#179F……明白了。\x01",
            "祝你好运。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("基尔巴特")

    AnonymousTalk(    #107
        "\x07\x05呼，彼此彼此！\x02",
    )

    Jump("loc_4BA0")

    label("loc_4BA0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x0)
    OP_74(0xC, 0x8, 0x0)
    OP_74(0xC, 0xA, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #108
        0x1F,
        "#1008F#6P基尔巴特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x1B,
        (
            "#573F#12P哎呀哎呀……\x01",
            "功劳都被他抢走了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    ChrTalk(    #110
        0x16,
        (
            "#210F#11P反正，那家伙的本事\x01",
            "大概不用担心吧？\x02\x03",

            "我们的山猫号对付他\x01",
            "也都要陷入苦战呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "#1840F#6P的确……\x01",
            "这次就相信那位小哥吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12,
        (
            "#1937F#12P……我们至少可以\x01",
            "向女神祈祷他平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x14,
        "#179F#5P……也是。\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_4D49():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4D49)

    def lambda_4D61():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4D61)

    def lambda_4D79():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4D79)

    def lambda_4D89():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4D89)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #114
        0x14,
        (
            "#177F#11P──再次全速前进！\x02\x03",

            "就这样向着目的地\x01",
            "一口气冲过去！\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(400)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("临时机组成员们")

    AnonymousTalk(    #115
        "\x07\x00#4S是，长官！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_44D7 end

    def Function_21_4E86(): pass

    label("Function_21_4E86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)

    def lambda_4FAF():

        label("loc_4FAF")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_4FAF")

    QueueWorkItem2(0xEE, 0, lambda_4FAF)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #116
        0x1F,
        (
            "#1015F#5P咦……\x01",
            "刚才你们有没有听到什么声音？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x21, 90, 400)
    Sleep(300)

    ChrTalk(    #117
        0x21,
        (
            "#267F#6P有吗？\x01",
            "玲什么也没听到啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_505A():
        OP_6D(760, 1800, 96310, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_505A)

    def lambda_5072():
        OP_67(0, 4800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5072)

    def lambda_508A():
        OP_6B(3030, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_508A)

    def lambda_509A():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_509A)
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)

    def lambda_510A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_510A)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #118
        0x16,
        (
            "#214F#11P前方１２０塞尔矩处\x01",
            "感知到巨大建筑……！\x02\x03",

            "看起来好像是目的地哦！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x14,
        (
            "#176F#6P差不多应该可以看到了……\x02\x03",

            "#178F约修亚。\x01",
            "转动一下摄影机看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#1500F#5P明白了。\x02\x03",

            "#1503F以最大变焦\x01",
            "开始捕捉目的地……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x17,
        (
            "#1506F#5P……捕捉到了！\x01",
            "马上显示在监视器上！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x9D, 0x0, 0x64)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS479._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x0, -330000, -265000, 8000)
    OP_C6(0x0, 0x1, 2000, 2000, 8000)
    Sleep(5000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_74(0xC, 0x6, 0x7)
    OP_74(0xC, 0x8, 0x7)
    OP_74(0xC, 0xA, 0x7)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_6D(250, 2000, 94350, 0)
    OP_67(0, 3930, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_8C(0x18, 45, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #122
        0x1F,
        "#1004F#6P那、那是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x13,
        (
            "#560F#6P哇……！\x01",
            "好像童话里的情景……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x18,
        (
            "#1169F#6P………宫殿……………\x02\x03",

            "#1162F不，更确切的说\x01",
            "应该称之为城堡吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x20,
        (
            "#112F#6P矗立在茫茫荒野中的\x01",
            "『影之王』居城……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1A,
        (
            "#1545F#12P呼，\x01",
            "还真是有种浪漫的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        "#1942F#12P姐姐就在那里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "#1065F#6P啊啊……不会错的。\x02\x03",

            "#1840F话说回来……\x01",
            "这东西建得还\x01",
            "真是雄伟啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #129
        0x14,
        (
            "#178F#5P好了……\x01",
            "凯文先生，怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#1067F#6P这个嘛……\x02\x03",

            "#1060F保持警惕慢慢接近，\x01",
            "找找能够进入的地方吧。\x02\x03",

            "我想大概『影之王』\x01",
            "也在等着我们进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x14,
        "#176F#5P……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_5870():
        OP_6D(730, 2000, 97690, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5870)

    def lambda_5888():
        OP_67(0, 4430, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5888)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_8C(0x18, 0, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #132
        0x14,
        (
            "#172F#11P──埃尔赛尤，开始减速！\x02\x03",

            "到达目标地点后\x01",
            "即进入环绕飞行！\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    Sleep(500)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("临时机组成员们")

    AnonymousTalk(    #133
        "\x07\x00#4S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x7A, 0x3C)
    Sleep(500)
    OP_24(0x7A, 0x32)
    Sleep(500)
    OP_24(0x7A, 0x28)
    Sleep(500)
    OP_24(0x7A, 0x1E)
    Sleep(500)
    OP_24(0x7A, 0x14)
    Sleep(500)
    OP_24(0x7A, 0xA)
    Sleep(500)
    OP_23(0x7A)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_4E86 end

    SaveToFile()

Try(main)
