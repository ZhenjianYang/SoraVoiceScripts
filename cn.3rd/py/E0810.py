from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0810   ._SN',
        MapName             = 'Event',
        Location            = 'E0810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '飞空船',                               # 9
        '飞空船',                               # 10
        '古代龙',                               # 11
        '古怪的魔兽',                           # 12
        '目标用照相机',                         # 13
        '玛丽',                                 # 14
        '古怪的魔兽',                           # 15
        '玛丽',                                 # 16
        '基尔巴特',                             # 17
        '奥利维特皇子',                         # 18
        '穆拉少校',                             # 19
        '奥斯本宰相',                           # 20
        '雷克特书记官',                         # 21
        '艾莉卡',                               # 22
        '丹',                                   # 23
        '目标角色',                             # 24
        '假设镜头',                             # 25
        '',                                     # 26
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
        'ED6_DT29/CH14373 ._CH',             # 00
        'ED6_DT29/CH14800 ._CH',             # 01
        'ED6_DT27/CH03260 ._CH',             # 02
        'ED6_DT27/CH03570 ._CH',             # 03
        'ED6_DT27/CH03950 ._CH',             # 04
        'ED6_DT26/CH20805 ._CH',             # 05
        'ED6_DT27/CH04267 ._CH',             # 06
        'ED6_DT27/CH04269 ._CH',             # 07
        'ED6_DT27/CH04262 ._CH',             # 08
        'ED6_DT26/CH20809 ._CH',             # 09
        'ED6_DT26/CH20758 ._CH',             # 0A
        'ED6_DT26/CH20759 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14373P._CP',             # 00
        'ED6_DT29/CH14800P._CP',             # 01
        'ED6_DT27/CH03260P._CP',             # 02
        'ED6_DT27/CH03570P._CP',             # 03
        'ED6_DT27/CH03950P._CP',             # 04
        'ED6_DT26/CH20805P._CP',             # 05
        'ED6_DT27/CH04267P._CP',             # 06
        'ED6_DT27/CH04269P._CP',             # 07
        'ED6_DT27/CH04262P._CP',             # 08
        'ED6_DT26/CH20809P._CP',             # 09
        'ED6_DT26/CH20758P._CP',             # 0A
        'ED6_DT26/CH20759P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1A4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1A4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1A4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xEE,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xEE,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_4AD",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_51D",          # 03, 3
        "Function_4_73A",          # 04, 4
        "Function_5_78A",          # 05, 5
        "Function_6_D80",          # 06, 6
        "Function_7_DC5",          # 07, 7
        "Function_8_DD8",          # 08, 8
        "Function_9_E2D",          # 09, 9
        "Function_10_E92",         # 0A, 10
        "Function_11_10DF",        # 0B, 11
        "Function_12_156E",        # 0C, 12
        "Function_13_17BF",        # 0D, 13
        "Function_14_1DC5",        # 0E, 14
        "Function_15_1ED6",        # 0F, 15
        "Function_16_1F1A",        # 10, 16
        "Function_17_1F6F",        # 11, 17
        "Function_18_1F96",        # 12, 18
        "Function_19_264C",        # 13, 19
        "Function_20_2725",        # 14, 20
        "Function_21_2782",        # 15, 21
        "Function_22_285F",        # 16, 22
        "Function_23_2876",        # 17, 23
        "Function_24_288D",        # 18, 24
        "Function_25_28C0",        # 19, 25
        "Function_26_2C4E",        # 1A, 26
        "Function_27_4032",        # 1B, 27
        "Function_28_40ED",        # 1C, 28
        "Function_29_422E",        # 1D, 29
        "Function_30_426D",        # 1E, 30
        "Function_31_43EA",        # 1F, 31
        "Function_32_4420",        # 20, 32
        "Function_33_4445",        # 21, 33
        "Function_34_494E",        # 22, 34
        "Function_35_49B7",        # 23, 35
        "Function_36_4A3B",        # 24, 36
        "Function_37_50F6",        # 25, 37
        "Function_38_51D7",        # 26, 38
        "Function_39_5260",        # 27, 39
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    OP_A3(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_353")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 36)
    Jump("loc_36A")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_36A")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)

    label("loc_36A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_393")
    OP_A3(0x2509)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_415")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_3AD")
    OP_A3(0x2508)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_415")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_3CA")
    OP_A3(0x2507)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1)
    Event(0, 12)
    Jump("loc_415")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_3E4")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_415")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3FE")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_415")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_415")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_415")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_43D")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_43D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_45C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_45C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_484")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 26)

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_4AC")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 25)

    label("loc_4AC")

    Return()

    # Function_0_32A end

    def Function_1_4AD(): pass

    label("Function_1_4AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CE")
    OP_B1("E0810_1")
    Jump("loc_4ED")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4E4")
    OP_A3(0x1)
    OP_B1("E0810_1")
    Jump("loc_4ED")

    label("loc_4E4")

    OP_B1("E0810_0")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_506")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506")

    Return()

    # Function_1_4AD end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_507")

    label("loc_51C")

    Return()

    # Function_2_507 end

    def Function_3_51D(): pass

    label("Function_3_51D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_A1(0x10, 0x5)
    SetChrPos(0x10, -30000, 0, -10000, 90)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-32710, 6500, 41650, 0)
    OP_67(0, 3100, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(315000, 0)
    OP_6E(527, 0)

    def lambda_5AD():
        OP_6D(-30160, 10500, 10250, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5AD)

    def lambda_5C5():
        OP_67(0, 1240, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5C5)

    def lambda_5DD():
        OP_6B(6760, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5DD)

    def lambda_5ED():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5ED)

    def lambda_5FD():
        OP_6E(704, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5FD)

    def lambda_60D():
        OP_91(0xFE, 0x0, 0x1388, 0x493E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_60D)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5500)
    OP_44(0x0, 0x0)
    OP_43(0x0, 0x0, 0x0, 0x4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x0, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00Episode『启程的清晨』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D")
    Sleep(1000)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x4, 0x20)
    OP_3E(0x2CF, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xCF\x02\x07\x00。\x02",
    )

    Jump("loc_6F6")

    label("loc_6F6")

    CloseMessageWindow()
    AddMira(8000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x00得到了\x07\x02８０００米拉\x07\x00。\x02",
    )

    Jump("loc_721")

    label("loc_721")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_72D")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5505   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_51D end

    def Function_4_73A(): pass

    label("Function_4_73A")

    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x79, 0x0)
    OP_23(0x79)
    Return()

    # Function_4_73A end

    def Function_5_78A(): pass

    label("Function_5_78A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x80)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -75210, 5050, -18190, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_1D(0x1)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00卡尔瓦德共和国西部，\x01",
            "利贝尔王国的国境附近――\x02\x03",

            "上空２２００亚矩――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(-208950, -12600, -29370, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(10830, 0)
    OP_6C(292000, 0)
    OP_6E(550, 0)
    FadeToBright(2000, 0)

    def lambda_8FF():
        OP_6E(610, 7000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8FF)
    Sleep(1000)

    def lambda_914():
        OP_6D(-110390, 7000, 14140, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_914)

    def lambda_92C():
        OP_67(0, 1000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_92C)

    def lambda_944():
        OP_6B(8770, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_944)

    def lambda_954():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_954)
    WaitChrThread(0x10B, 0x0)
    OP_43(0x12, 0x1, 0x0, 0x6)

    def lambda_970():
        OP_6D(-80390, 4000, 15140, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_970)

    def lambda_988():
        OP_67(0, 1600, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_988)

    def lambda_9A0():
        OP_6B(15000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_9A0)

    def lambda_9B0():
        OP_6C(45000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_9B0)

    QueueWorkItem(0x12, 0, None)
    OP_43(0x10, 0x1, 0x0, 0x9)

    def lambda_9CD():
        OP_91(0xFE, 0xFFFFC568, 0xFFFFF830, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9CD)
    WaitChrThread(0x10, 0x0)

    def lambda_9ED():
        OP_91(0xFE, 0xFFFFB9B0, 0x7D0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9ED)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10, 0x1)

    def lambda_A12():
        OP_91(0xFE, 0x2710, 0xFFFFF830, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A12)

    def lambda_A2D():
        OP_D1(254, 0, 270000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A2D)
    WaitChrThread(0x10, 0x3)

    def lambda_A4C():
        OP_D1(254, 0, 270000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A4C)
    WaitChrThread(0x10, 0x0)

    def lambda_A6B():
        OP_D1(254, -10000, 250000, 60000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A6B)
    OP_43(0x12, 0x1, 0x0, 0x7)

    def lambda_A8C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A8C)
    Sleep(100)

    def lambda_AAC():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AAC)
    Sleep(100)

    def lambda_ACC():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_ACC)
    Sleep(100)

    def lambda_AEC():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AEC)
    Sleep(100)

    def lambda_B0C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B0C)
    Sleep(100)

    def lambda_B2C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B2C)
    Sleep(100)

    def lambda_B4C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B4C)
    Sleep(100)

    def lambda_B6C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B6C)
    Sleep(100)

    def lambda_B8C():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B8C)
    Sleep(100)

    def lambda_BAC():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BAC)
    Sleep(1500)
    OP_44(0x10B, 0x0)
    OP_44(0x10B, 0x1)
    OP_44(0x10B, 0x2)
    OP_44(0x10B, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x3)
    SetChrPos(0x10, -59790, -5000, -4880, 270)
    OP_D1(16, 0, 270000, -30000, 0)
    OP_6D(-101260, -10100, 8020, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(4130, 0)
    OP_6C(269000, 0)
    OP_6E(869, 0)
    OP_D0(-25000, 0)

    def lambda_C4E():
        OP_D1(254, 0, 270000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_C4E)

    def lambda_C68():
        OP_6D(-71660, -10100, -8530, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_C68)

    def lambda_C80():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_C80)

    def lambda_C98():
        OP_6B(6000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_C98)
    Sleep(2000)

    def lambda_CAD():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_CAD)
    OP_24(0x79, 0x5A)
    WaitChrThread(0x10B, 0x0)
    WaitChrThread(0x10B, 0x1)
    WaitChrThread(0x10B, 0x2)
    WaitChrThread(0x10B, 0x3)

    def lambda_CD5():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_CD5)

    def lambda_CEF():
        OP_6D(-62000, -5550, 1720, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CEF)

    def lambda_D07():
        OP_67(0, 5780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_D07)

    def lambda_D1F():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_D1F)

    def lambda_D2F():
        OP_D0(0, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_D2F)
    WaitChrThread(0x10B, 0x0)
    Sleep(1000)

    def lambda_D49():
        OP_6E(700, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_D49)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_43(0x12, 0x1, 0x0, 0x8)
    OP_0D()
    OP_44(0x10B, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_5_78A end

    def Function_6_D80(): pass

    label("Function_6_D80")

    OP_22(0x79, 0x1, 0xA)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x50)
    Return()

    # Function_6_D80 end

    def Function_7_DC5(): pass

    label("Function_7_DC5")

    Sleep(800)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Return()

    # Function_7_DC5 end

    def Function_8_DD8(): pass

    label("Function_8_DD8")

    OP_24(0x79, 0x5A)
    Sleep(150)
    OP_24(0x79, 0x50)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0xA)
    Sleep(150)
    OP_23(0x79)
    Return()

    # Function_8_DD8 end

    def Function_9_E2D(): pass

    label("Function_9_E2D")

    Sleep(1000)
    OP_D1(16, 0, 270000, 5000, 1500)
    OP_D1(16, 0, 270000, -10000, 800)
    OP_D1(16, 0, 270000, 0, 1000)
    OP_D1(16, 0, 270000, 15000, 1300)
    OP_D1(16, 0, 270000, 0, 1000)
    Return()

    # Function_9_E2D end

    def Function_10_E92(): pass

    label("Function_10_E92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x8)
    OP_6D(-53740, 25000, 17680, 0)
    OP_67(0, 1340, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -37600, 25000, -54800, 0)
    FadeToBright(2000, 0)

    def lambda_F1D():
        OP_6D(-37600, 25980, -54830, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_F1D)

    def lambda_F35():
        OP_6C(190000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_F35)

    def lambda_F45():
        OP_8C(0xFE, 45, 5000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F45)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)
    WaitChrThread(0x10B, 0x0)
    Sleep(300)

    NpcTalk(    #4
        0x18,
        "青发的猎兵",
        (
            "不愧是空贼团出身……\x01",
            "还挺厉害的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x18,
        "青发的猎兵",
        (
            "哼哼，\x01",
            "没想到需要劳烦我\x01",
            "基尔巴特大人亲自出马。\x02",
        )
    )

    Jump("loc_1015")

    label("loc_1015")

    CloseMessageWindow()

    def lambda_101C():
        OP_6B(3700, 1000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_101C)

    def lambda_102C():
        OP_6C(218000, 1000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_102C)
    WaitChrThread(0x10B, 0x0)
    Sleep(500)

    ChrTalk(    #6
        0x18,
        (
            "#1226F载人型人形兵器『Ｇ－阿帕奇』――\x02\x03",

            "#1225F出击摧毁『山猫号』！\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10AA():
        OP_6B(0, 1500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10AA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_E92 end

    def Function_11_10DF(): pass

    label("Function_11_10DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x8)
    SetChrFlags(0x10B, 0x4)
    SetChrPos(0x10B, -37600, 25000, -54800, 0)
    OP_6D(-37600, 25800, -54800, 0)
    OP_67(0, 1340, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -37600, 25000, -54800, 0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "map\\\\mpsmk0.eff")
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x2, 0x0, 0x18, 500, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x18, 1500, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x18, -1000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x18, 0, 0, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_129F():
        OP_9E(0xFE, 0x14, 0xFFFFFFFB, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_129F)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x64)

    def lambda_12C3():
        OP_6B(4200, 2000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12C3)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #7
        0x18,
        (
            "#1224F#5P怎、怎么回事……\x01",
            "『Ｇ－阿帕奇』居然会被打败……\x02\x03",

            "#1225F降、降落伞在哪里！？\x01",
            "这、这个……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0xFFFFFCF4, 1820, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x18)
    Sleep(500)

    ChrTalk(    #8
        0x18,
        (
            "#1227F#5P#3S……不对！\x01",
            "这是胜利彩球用的彩带！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x18, 0x20)
    OP_4A(0x18, 255)
    OP_23(0x77)
    OP_23(0x135)
    OP_22(0x13B, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x18, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x18, 1500, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x4, 0x18, -1500, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x18, 0, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    def lambda_14C5():
        OP_6D(-37600, 8800, -54800, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_14C5)

    def lambda_14DD():
        OP_67(0, 5860, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_14DD)

    def lambda_14F5():
        OP_6B(14200, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_14F5)

    def lambda_1505():
        OP_8F(0xFE, 0xFFFF6D20, 0xFFFFD8F0, 0xFFFF29F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1505)
    Sleep(400)

    ChrTalk(    #9 op#A
        0x18,
        "#5P#15A#4S啊～～～呀～～～～！#2S\x02",
    )

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_10DF end

    def Function_12_156E(): pass

    label("Function_12_156E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10B, 0x80)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_6D(71500, 0, 0, 0)
    OP_67(0, 1120, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(90000, 0)
    OP_6E(760, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x64)
    OP_A1(0x10, 0x6)
    SetChrPos(0x10, 120000, 0, 0, 0)
    ClearChrFlags(0x10, 0x100)
    OP_D1(16, 0, 270000, 0, 0)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 800)
    OP_70(0x6, 0x384)

    def lambda_1670():
        OP_8F(0xFE, 0xC350, 0x0, 0x0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1670)
    FadeToBright(2000, 0)
    WaitChrThread(0x10, 0x0)

    def lambda_1699():
        OP_6D(-26420, 0, -20260, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1699)

    def lambda_16B1():
        OP_6C(134000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16B1)

    def lambda_16C1():
        OP_6B(8460, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_16C1)

    def lambda_16D1():
        OP_D0(-6000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_16D1)

    def lambda_16E1():
        OP_D1(254, 0, 250000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_16E1)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0x0, 0x0, 0x0)
    OP_98(0x1, 0xFFFF8AD0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFEDB08)

    def lambda_1729():
        OP_98(0x2, 0xFE, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1729)
    WaitChrThread(0x10, 0x0)

    def lambda_173E():
        OP_8F(0xFE, 0xFFFEEE90, 0x0, 0xFFFBBA40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_173E)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_23(0x79)
    OP_0D()
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_156E end

    def Function_13_17BF(): pass

    label("Function_13_17BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_6D(-61040, -10000, -5750, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(9240, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x10B, 0x80)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -75210, 15000, -18190, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_6D(-49710, -11090, -210, 0)
    OP_67(0, 8470, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(57000, 0)
    OP_6E(1056, 0)

    def lambda_18F3():
        OP_6D(-58000, -11090, 40, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_18F3)

    def lambda_190B():
        OP_67(0, 9070, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_190B)

    def lambda_1923():
        OP_6B(4850, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1923)
    OP_22(0x79, 0x1, 0x64)
    LoadEffect(0x1, "map\\mp077_00.eff")
    LoadEffect(0x2, "map\\mp096_00.eff")
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1968():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1968)
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_D8(0x3, 0x3E8)
    OP_B0(0x3, 0x2)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x154)
    OP_73(0x1)
    OP_B0(0x3, 0x1E)
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 240)
    OP_70(0x3, 0x154)
    WaitChrThread(0x10, 0x0)

    def lambda_19BF():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_19BF)
    Sleep(200)

    def lambda_19DF():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_19DF)
    Sleep(200)

    def lambda_19FF():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_19FF)
    Sleep(200)

    def lambda_1A1F():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A1F)
    Sleep(200)

    def lambda_1A3F():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A3F)
    Sleep(200)

    def lambda_1A5F():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A5F)
    Sleep(200)

    def lambda_1A7F():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A7F)
    Sleep(200)

    def lambda_1A9F():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A9F)
    Sleep(200)

    def lambda_1ABF():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1ABF)
    Sleep(200)

    def lambda_1ADF():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1ADF)
    Sleep(100)
    OP_44(0x10B, 0x0)
    OP_44(0x10B, 0x1)
    OP_44(0x10B, 0x2)
    OP_44(0x10, 0x0)
    SetChrPos(0x10, -70210, 20000, -5190, 0)
    OP_D1(16, 0, 270000, 45000, 0)
    OP_43(0x10, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x2, 0x0, 0x11)
    OP_6D(-119800, 10800, -21040, 0)
    OP_67(0, -4100, -10000, 0)
    OP_6B(7010, 0)
    OP_6C(303000, 0)
    OP_6E(628, 0)

    def lambda_1B7E():
        OP_6C(250000, 11000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1B7E)

    def lambda_1B8E():
        OP_6D(-94100, 19500, -19610, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1B8E)

    def lambda_1BA6():
        OP_67(0, -4070, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1BA6)

    def lambda_1BBE():
        OP_6B(4850, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1BBE)

    def lambda_1BCE():
        OP_6E(689, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_1BCE)
    WaitChrThread(0x10B, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, -75320, 20000, -30020, 40, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_1C18():
        OP_6D(-185440, -14150, -8840, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1C18)

    def lambda_1C30():
        OP_67(0, 8250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1C30)

    def lambda_1C48():
        OP_6B(10770, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1C48)

    def lambda_1C58():
        OP_6E(869, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_1C58)
    Sleep(4000)
    PlayEffect(0x1, 0xFF, 0xFF, -205000, -10000, -2610, 270, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -208000, -11000, 2610, 270, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -212450, -12000, 11610, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -216450, -13000, 15610, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x12, 0x1, 0x0, 0x10)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00Episode『山猫卡普亚的特急便』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Call(0, 14)
    Return()

    # Function_13_17BF end

    def Function_14_1DC5(): pass

    label("Function_14_1DC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E78")
    OP_28(0x24, 0x4, 0x20)
    OP_3E(0x2CE, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xCE\x02\x07\x00。\x02",
    )

    Jump("loc_1E26")

    label("loc_1E26")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E78")
    OP_35(0xA, 0x112)
    OP_BB(0xA, 0x6, 0x112)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05乔丝特学会了Ｓ战技\x01",
            "\x07\x02『山猫号』\x07\x05。\x02",
        )
    )

    Jump("loc_1E77")

    label("loc_1E77")

    CloseMessageWindow()

    label("loc_1E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBE")
    OP_28(0x24, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00得到了\x07\x02３０００米拉\x07\x00。\x02",
    )

    Jump("loc_1EBD")

    label("loc_1EBD")

    CloseMessageWindow()

    label("loc_1EBE")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1DC5 end

    def Function_15_1ED6(): pass

    label("Function_15_1ED6")

    Sleep(1000)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0xFFFE2A6E, 0x3A98, 0xFFFF6302)
    OP_98(0x1, 0xFFFCF1EE, 0xFFFFD8F0, 0xFFFFD832)
    OP_98(0x1, 0xFFFBB96E, 0xFFFF3CB0, 0xEB1E)

    def lambda_1F0F():
        OP_98(0x2, 0xFE, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F0F)
    Return()

    # Function_15_1ED6 end

    def Function_16_1F1A(): pass

    label("Function_16_1F1A")

    OP_24(0x79, 0x5A)
    Sleep(150)
    OP_24(0x79, 0x50)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0xA)
    Sleep(150)
    OP_23(0x79)
    Return()

    # Function_16_1F1A end

    def Function_17_1F6F(): pass

    label("Function_17_1F6F")

    OP_D1(16, 0, 270000, 0, 2500)
    OP_D1(16, -30000, 310000, -40000, 4000)
    Return()

    # Function_17_1F6F end

    def Function_18_1F96(): pass

    label("Function_18_1F96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x100000)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    ClearMapFlags(0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x8)
    SetChrPos(0x14E, 0, 0, 0, 270)
    SetChrPos(0x13, 0, -1500, 0, 270)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x15, 0, -900, 0, 270)
    SetChrPos(0x16, 0, -1500, 0, 270)
    SetChrPos(0x17, 0, -1300, 0, 270)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_43(0x15, 0x0, 0x0, 0x13)
    OP_43(0x16, 0x0, 0x0, 0x13)
    OP_43(0x17, 0x0, 0x0, 0x13)
    OP_43(0x13, 0x2, 0x0, 0x14)
    OP_43(0x14E, 0x3, 0x0, 0x16)
    OP_6D(-45010, 12700, -18610, 0)
    OP_67(0, 1210, -10000, 0)
    OP_6B(4450, 0)
    OP_6C(33000, 0)
    OP_6E(417, 0)

    def lambda_212C():
        OP_6D(-13310, 8000, -17410, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_212C)

    def lambda_2144():
        OP_67(0, 3220, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2144)

    def lambda_215C():
        OP_6B(4340, 6000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_215C)

    def lambda_216C():
        OP_6E(341, 6000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_216C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x20, 0x0)
    Fade(1000)
    OP_6D(0, 0, 0, 0)
    OP_67(0, 4480, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    OP_43(0x14E, 0x3, 0x0, 0x17)
    OP_0D()
    Sleep(300)

    ChrTalk(    #14
        0x15,
        "#1714F#2P你、你是……！\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x13, 0xFFFFFE0C, 2000, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x13)

    ChrTalk(    #15
        0x15,
        "#1714F#2P你、你能飞吗？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x16,
        "#3P嗯，因为我还是小孩嘛～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x15,
        "#1714F#2P是小孩就能飞吗？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x16,
        (
            "#3P如果是大人的话，\x01",
            "就会有各种各样的麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        "#3P……大概就是这个原因吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0xC8, 2800, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #20
        0x15,
        "#1714F#2P我、我不明白啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x16,
        "#3P呵呵………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2354():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2354)
    Sleep(200)

    def lambda_2374():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2374)
    Sleep(200)

    def lambda_2394():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2394)
    Sleep(200)

    def lambda_23B4():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23B4)
    WaitChrThread(0x13, 0x1)
    SetChrPos(0x13, 0, 5000, 15000, 270)
    Fade(1000)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFA, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF7, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFEC, 0xFFFFFFFA, 0x0, 0x0, 0x0)
    OP_6D(-22600, 4000, 0, 0)
    OP_67(0, 1140, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(270000, 0)
    OP_6E(456, 0)
    OP_43(0x13, 0x3, 0x0, 0x15)
    OP_0D()
    Sleep(500)

    def lambda_2479():
        OP_6D(-46340, 3000, -2840, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2479)

    def lambda_2491():
        OP_6C(310000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2491)

    def lambda_24A1():
        OP_6E(320, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_24A1)
    WaitChrThread(0x13, 0x3)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x14E, 0, 0, 0, 270)
    SetChrPos(0x13, 0, -1500, 0, 270)
    OP_6D(0, 0, 0, 0)
    OP_67(0, 240, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(270000, 0)
    OP_6E(284, 0)
    OP_D0(6000, 0)
    OP_0D()
    FadeToDark(4000, 16777215, -126)
    OP_0D()

    def lambda_2534():
        OP_6B(3100, 15000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2534)

    NpcTalk(    #22
        0x16,
        "声音",
        "……今天真是开心。\x02",
    )

    Jump("loc_2566")

    label("loc_2566")

    CloseMessageWindow()

    ChrTalk(    #23
        0x17,
        "#1714F#5P咦…………？\x02",
    )

    CloseMessageWindow()

    def lambda_258F():
        OP_6B(3600, 10000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_258F)
    OP_44(0x14E, 0x3)
    Sleep(1000)
    OP_20(0x1388)
    FadeToDark(4000, 16777215, -1)
    OP_43(0x14E, 0x3, 0x0, 0x18)
    OP_24(0x1C3, 0x5A)
    Sleep(400)
    OP_24(0x1C3, 0x50)
    Sleep(400)
    OP_24(0x1C3, 0x46)
    Sleep(400)
    OP_24(0x1C3, 0x3C)
    Sleep(400)
    OP_24(0x1C3, 0x32)
    Sleep(400)
    OP_24(0x1C3, 0x28)
    Sleep(400)
    OP_24(0x1C3, 0x1E)
    Sleep(400)
    OP_24(0x1C3, 0x14)
    OP_0D()
    Sleep(1000)
    OP_21()
    OP_23(0x1C3)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_44(0x14, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    ClearChrFlags(0x14E, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2101   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1F96 end

    def Function_19_264C(): pass

    label("Function_19_264C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2724")
    OP_44(0x13, 0x2)

    def lambda_265F():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_265F)
    Sleep(355)

    def lambda_2674():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0xDC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2674)
    Sleep(485)
    OP_44(0xFE, 0x1)
    SetChrPos(0x15, 0, -1000, 0, 270)
    SetChrPos(0x16, 0, -1600, 0, 270)
    SetChrPos(0x17, 0, -1400, 0, 270)
    Sleep(185)

    def lambda_26D0():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26D0)
    Sleep(315)
    OP_44(0xFE, 0x1)
    SetChrPos(0x15, 0, -900, 0, 270)
    SetChrPos(0x16, 0, -1500, 0, 270)
    SetChrPos(0x17, 0, -1300, 0, 270)
    Jump("Function_19_264C")

    label("loc_2724")

    Return()

    # Function_19_264C end

    def Function_20_2725(): pass

    label("Function_20_2725")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2781")
    SetChrSubChip(0xFE, 2)
    Sleep(167)
    SetChrSubChip(0xFE, 3)
    Sleep(168)
    SetChrSubChip(0xFE, 4)
    Sleep(167)
    SetChrSubChip(0xFE, 5)
    Sleep(168)
    SetChrSubChip(0xFE, 6)
    Sleep(167)
    SetChrSubChip(0xFE, 7)
    Sleep(168)
    SetChrSubChip(0xFE, 0)
    Sleep(167)
    SetChrSubChip(0xFE, 1)
    Sleep(168)
    Jump("Function_20_2725")

    label("loc_2781")

    Return()

    # Function_20_2725 end

    def Function_21_2782(): pass

    label("Function_21_2782")

    OP_97(0x13, 0x0, 0x0, 0xFFFEA070, 0x2710, 0x0)
    OP_97(0x13, 0xFFFF9E58, 0x0, 0x15F90, 0x2710, 0x0)
    OP_62(0x13, 0x96, 2450, 0x26, 0x27, 0xC8, 0x2)

    def lambda_27C4():
        OP_8F(0xFE, 0xFFFF3CB0, 0x5DC, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_27C4)
    WaitChrThread(0x13, 0x1)

    def lambda_27E4():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_27E4)
    Sleep(200)

    def lambda_2804():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2804)
    Sleep(200)

    def lambda_2824():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2824)
    Sleep(200)

    def lambda_2844():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2844)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_21_2782 end

    def Function_22_285F(): pass

    label("Function_22_285F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2875")
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1400)
    Jump("Function_22_285F")

    label("loc_2875")

    Return()

    # Function_22_285F end

    def Function_23_2876(): pass

    label("Function_23_2876")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_288C")
    OP_22(0x120, 0x0, 0x46)
    Sleep(1400)
    Jump("Function_23_2876")

    label("loc_288C")

    Return()

    # Function_23_2876 end

    def Function_24_288D(): pass

    label("Function_24_288D")

    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1300)
    Return()

    # Function_24_288D end

    def Function_25_28C0(): pass

    label("Function_25_28C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_A1(0x10, 0x4)
    OP_A1(0x11, 0x5)
    OP_D1(16, 0, 270000, -15000, 0)
    OP_D1(17, 0, 270000, -10000, 0)
    SetChrPos(0x10, 30000, 0, 10000, 0)
    SetChrPos(0x11, 35000, 500, 14000, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 30300, 0, 10000, 270)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 35300, 500, 14000, 270)
    LoadEffect(0x1, "map\\\\mp065_01.eff")
    OP_6D(12820, -4000, -3150, 0)
    OP_67(0, 2380, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(207000, 0)
    OP_6E(860, 0)
    OP_D0(10000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x113, 0x1, 0x14)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)

    def lambda_2A2C():
        OP_6D(-14040, -4000, -3150, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2A2C)

    def lambda_2A44():
        OP_6C(227000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A44)

    def lambda_2A54():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2A54)

    def lambda_2A64():
        OP_D0(-10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2A64)
    PlayEffect(0x1, 0x1, 0x10, -800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x10, 800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2ADE():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2ADE)

    def lambda_2AF8():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFFD8F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AF8)

    def lambda_2B13():
        OP_8F(0xFE, 0xFFFE7A8C, 0x0, 0xFFFFD8F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2B13)
    PlayEffect(0x1, 0x3, 0x11, -800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x11, 800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2B98():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B98)

    def lambda_2BB2():
        OP_8F(0xFE, 0xFFFE7960, 0x1F4, 0xFFFFE890, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BB2)

    def lambda_2BCD():
        OP_8F(0xFE, 0xFFFE7A8C, 0x1F4, 0xFFFFE890, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2BCD)
    Sleep(3000)
    OP_24(0x113, 0x64)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(20)
    OP_24(0x113, 0x14)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x113)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_28C0 end

    def Function_26_2C4E(): pass

    label("Function_26_2C4E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C3, 0x0, 0x64)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_22(0x79, 0x1, 0x46)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp296_00.eff")
    LoadEffect(0x4, "map\\\\mp296_01.eff")
    LoadEffect(0x1, "map\\\\mp297_00.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    LoadEffect(0x3, "battle\\btgun00.eff")
    LoadEffect(0x5, "map\\\\mp296_04.eff")
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 197210, -30000, 8810, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, -15000, 270000, 4000, 0)
    OP_71(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_B0(0x2, 0x1E)
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, -75210, 10000, -18190, 0)
    ClearChrFlags(0x11, 0x100)
    OP_8C(0x11, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1B, 0x20)
    SetChrBattleFlags(0x1C, 0x20)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    SetChrPos(0x1B, -71180, 17200, -15000, 0)
    SetChrPos(0x1C, -70420, 17200, -16100, 0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_6D(-115120, 17200, -18290, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(5860, 0)
    OP_6C(270000, 0)
    OP_6E(334, 0)

    def lambda_2E59():
        OP_6D(-73000, 17200, -18040, 14000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2E59)

    def lambda_2E71():
        OP_6C(225000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2E71)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x0)
    Fade(1000)
    OP_6D(-71580, 17200, -16360, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x1B,
        (
            "#1485F#5P奥利维特皇子……\x01",
            "哼哼，真是增色不少啊。\x02\x03",

            "#1481F不管他会怎么行动，\x01",
            "最终都会被我利用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1C,
        (
            "#1884F#5P……对于你来说，\x01",
            "所有的要素都是『棋子』呢。\x02\x03",

            "#1882F那位皇子和我，\x01",
            "还有『噬身之蛇』都包括在内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1B,
        (
            "#1480F#5P是啊，而且我自己也是。\x02\x03",

            "#1485F将帝国这样大的地盘当作舞台，\x01",
            "玩起震人心魂的激动游戏……\x02\x03",

            "#1481F你不也是想见识一下\x01",
            "才会跟随我的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1C,
        (
            "#1885F#5P嗯，我无法否认。\x02\x03",

            "#1887F……但是我这颗棋子\x01",
            "什么时候会背叛可是说不准的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x1B,
        (
            "#1485F#5P那样也没有关系。\x02\x03",

            "#1480F你认为我没有\x01",
            "考虑过这种可能性吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1C,
        (
            "#1884F#5P哼，只是说说而已嘛。\x02\x03",

            "#1880F不过……\x01",
            "其他的『孩子们』怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1B,
        (
            "#1481F#5P呵呵，每个孩子都很好。\x02\x03",

            "这样下去的话，\x01",
            "皇子的努力说不定就付诸东流了。\x02\x03",

            "#1485F唉……\x01",
            "我要不要稍微手下留情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1C,
        "#1884F#5P哼……真是个低级趣味的大叔啊。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x1C, 90, 400)
    SetChrSubChip(0x1C, 0)
    Sleep(300)

    ChrTalk(    #32
        0x1C,
        (
            "#1883F#11P……对了，宰相阁下。\x02\x03",

            "#1886F你最好别\x01",
            "小看那个家伙哦……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1B,
        "#1482F#5P什么……\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x1B, 90, 400)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    SetChrBattleFlags(0x19, 0x20)
    SetChrBattleFlags(0x1A, 0x20)
    OP_48()
    OP_89(0x19, 184420, -27640, 6520, 180)
    OP_89(0x1A, 183780, -27560, 7620, 180)
    OP_43(0x1A, 0x3, 0x0, 0x1E)
    OP_43(0x10, 0x3, 0x0, 0x1C)
    Sleep(3000)

    def lambda_3340():
        OP_D1(254, 0, 270000, 4000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3340)
    Sleep(7000)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34 op#A
        0x1B,
        "#1483F#11P#3S#15A嗯……！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x10, 0x3)
    Fade(1000)
    OP_6D(-68320, 16440, -2720, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_8C(0x19, 225, 0)
    SetChrChipByIndex(0x19, 7)
    SetChrSubChip(0x19, 3)

    def lambda_3424():
        OP_99(0xFE, 0x3, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3424)
    WaitChrThread(0x19, 0x2)
    Sleep(300)

    ChrTalk(    #35 op#A
        0x19,
        "#1545F#5P#15A呼……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 13)
    Sleep(100)
    OP_8C(0x19, 180, 0)
    Sleep(100)

    def lambda_3474():
        OP_99(0xFE, 0xE, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3474)
    WaitChrThread(0x19, 0x2)

    def lambda_3489():
        OP_6D(-68150, 17300, -6670, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3489)

    def lambda_34A1():
        OP_67(0, 3550, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34A1)

    def lambda_34B9():
        OP_6C(23000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_34B9)

    def lambda_34C9():
        OP_6B(1850, 1500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_34C9)

    def lambda_34D9():
        OP_6E(556, 1500)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_34D9)

    def lambda_34E9():
        OP_D0(11000, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_34E9)
    OP_22(0x23B, 0x0, 0x64)
    SetChrPos(0x1F, -69900, 17300, -14320, 0)
    PlayEffect(0x0, 0x0, 0x19, 500, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    Sleep(800)

    def lambda_3553():
        OP_99(0xFE, 0x0, 0x4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3553)
    WaitChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 8)
    SetChrSubChip(0x19, 0)
    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x19, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_35B1():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_35B1)
    PlayEffect(0x5, 0x3, 0xFF, -69500, 21500, -13660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x19, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_6D(-69700, 17200, -17200, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()

    def lambda_364F():
        OP_67(0, 8500, -10000, 40000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_364F)

    def lambda_3667():
        OP_6B(6000, 40000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3667)
    OP_43(0x1B, 0x3, 0x0, 0x20)
    OP_43(0x1C, 0x3, 0x0, 0x1F)
    WaitChrThread(0x1B, 0x3)
    Sleep(500)

    ChrTalk(    #36 op#A
        0x1B,
        "#1483F#5P#15A……这个是…………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0x3)
    Sleep(500)

    ChrTalk(    #37 op#A
        0x1C,
        "#1883F#11P#35A好像是……蔷薇花。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #38 op#A
        (
            "\x07\x05#100A各位乘客，在飞船右侧出现的\x01",
            "就是众所周知的利贝尔王家的\x01",
            "高速巡洋舰『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetChrName("女性的声音")

    AnonymousTalk(    #39 op#A op#5
        (
            "\x07\x05#95A今天，埃雷波尼亚帝国的\x01",
            "奥利维特皇子殿下\x01",
            "乘坐该飞艇返回帝国首都……\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetChrName("女性的声音")

    AnonymousTalk(    #40 op#A
        (
            "\x07\x05#65A那位皇子殿下\x01",
            "向各位乘客表示了问候。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetChrName("女性的声音")

    AnonymousTalk(    #41 op#A
        (
            "\x07\x05#55A『今天在此相遇十分荣幸，\x01",
            "  在此向空之女神表示感谢。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("女性的声音")

    AnonymousTalk(    #42 op#A
        (
            "\x07\x05#50A『愿你们的旅途有美丽的蔷薇\x01",
            "  和女神的祝福陪伴。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("女性的声音")

    AnonymousTalk(    #43 op#A
        (
            "\x07\x05#55A『并且祝愿你们能够\x01",
            "  顺利平安地返回自己的故乡。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetChrName("女性的声音")

    AnonymousTalk(    #44 op#A
        "\x07\x05#10A──就是这些了。\x07\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_44(0x14, 0xFF)
    Fade(1000)
    OP_6D(-68320, 16440, -2720, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()
    PlayEffect(0x1, 0x1, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(300)
    SetChrChipByIndex(0x19, 6)
    SetChrSubChip(0x19, 2)
    OP_0D()

    def lambda_3AAD():
        OP_99(0xFE, 0x2, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3AAD)
    WaitChrThread(0x19, 0x2)
    Sleep(500)

    def lambda_3AC7():
        OP_6D(-76510, 17200, -5270, 9000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3AC7)

    def lambda_3ADF():
        OP_67(0, 3680, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3ADF)

    def lambda_3AF7():
        OP_6C(303000, 9000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3AF7)

    def lambda_3B07():
        OP_6B(3020, 9000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_3B07)

    def lambda_3B17():
        OP_6E(686, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_3B17)
    OP_43(0x19, 0x3, 0x0, 0x1D)

    def lambda_3B2E():
        OP_D1(254, 0, 310000, -14000, 15000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3B2E)

    def lambda_3B48():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B48)
    Sleep(300)

    def lambda_3B68():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B68)
    Sleep(400)

    def lambda_3B88():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B88)
    Sleep(500)

    def lambda_3BA8():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3BA8)
    Sleep(600)

    def lambda_3BC8():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3BC8)
    Sleep(700)

    def lambda_3BE8():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3BE8)
    Sleep(800)

    def lambda_3C08():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C08)
    Sleep(900)

    def lambda_3C28():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C28)
    Sleep(1000)

    def lambda_3C48():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C48)
    Sleep(1000)

    def lambda_3C68():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C68)
    WaitChrThread(0x19, 0x3)
    Fade(1000)
    OP_6D(-71580, 17200, -16360, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 270, 0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x1B)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #45
        0x1B,
        "#1484F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1C,
        (
            "#1883F#6P白痴……\x01",
            "……居然还有比我更白痴的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1B,
        "#1481F#5P……呵呵呵………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #48
        0x1B,
        "#1486F#5P#4S哈哈哈哈哈哈哈！！#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-69380, 17200, -15640, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(110000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x1B,
        "#1481F#5P#3S好吧，放荡皇子！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x1B,
        (
            "#1485F#5P你能与我这个『铁血宰相』\x01",
            "纠缠到何种地步……\x02\x03",

            "#1481F就让我好好\x01",
            "开开眼界吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3ED9():
        OP_6E(562, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3ED9)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_24(0x1C3, 0x5A)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x79, 0xA)
    OP_23(0x1C3)
    OP_23(0x79)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00Episode『返回帝都』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4025")
    Sleep(1000)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x4, 0x20)
    OP_3E(0x2ED, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x00得到了\x1F\xED\x02\x07\x00。\x02",
    )

    Jump("loc_3FEE")

    label("loc_3FEE")

    CloseMessageWindow()
    AddMira(7000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #53
        "\x07\x00得到了\x07\x02７０００米拉\x07\x00。\x02",
    )

    Jump("loc_4019")

    label("loc_4019")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4025")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M7204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_2C4E end

    def Function_27_4032(): pass

    label("Function_27_4032")

    PlayEffect(0x4, 0x2, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2500)
    Sleep(3000)

    label("loc_406C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40EC")
    PlayEffect(0x4, 0x1, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1500)
    Sleep(4000)
    PlayEffect(0x4, 0x2, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1500)
    Sleep(4000)
    Jump("loc_406C")

    label("loc_40EC")

    Return()

    # Function_27_4032 end

    def Function_28_40ED(): pass

    label("Function_28_40ED")


    def lambda_40F3():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_40F3)
    Sleep(6000)

    def lambda_4113():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4113)
    Sleep(1000)

    def lambda_4133():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4133)
    Sleep(900)

    def lambda_4153():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4153)
    Sleep(800)

    def lambda_4173():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4173)
    Sleep(700)

    def lambda_4193():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4193)
    Sleep(600)

    def lambda_41B3():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41B3)
    Sleep(500)

    def lambda_41D3():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41D3)
    Sleep(400)

    def lambda_41F3():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41F3)
    Sleep(300)

    def lambda_4213():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4213)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_28_40ED end

    def Function_29_422E(): pass

    label("Function_29_422E")

    OP_24(0x125, 0x46)
    Sleep(2000)
    OP_24(0x125, 0x3C)
    Sleep(2000)
    OP_24(0x125, 0x32)
    Sleep(2000)
    OP_24(0x125, 0x28)
    Sleep(2000)
    OP_24(0x125, 0x1E)
    Sleep(2000)
    OP_24(0x125, 0x14)
    Sleep(2000)
    OP_23(0x125)
    Sleep(1000)
    Return()

    # Function_29_422E end

    def Function_30_426D(): pass

    label("Function_30_426D")

    Fade(1000)
    OP_6D(110380, 1230, -17180, 0)
    OP_67(0, 3140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(316000, 0)
    OP_6E(696, 0)
    OP_D0(9000, 0)
    OP_22(0x125, 0x1, 0x46)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 102000, -10000, 640, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 87000, -10000, 640, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x1C, 0, 0)
    OP_8C(0x1B, 0, 0)

    def lambda_4345():
        OP_6D(-68760, 17300, -8820, 7000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4345)

    def lambda_435D():
        OP_67(0, 3140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_435D)

    def lambda_4375():
        OP_6C(86000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4375)

    def lambda_4385():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4385)

    def lambda_4395():
        OP_6E(696, 7000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_4395)

    def lambda_43A5():
        OP_D0(-9000, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_43A5)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 72000, -10000, 640, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_30_426D end

    def Function_31_43EA(): pass

    label("Function_31_43EA")

    Sleep(100)
    OP_8C(0x1C, 45, 600)
    Sleep(600)
    OP_8C(0x1C, 0, 600)
    Sleep(700)
    OP_8C(0x1C, 45, 600)
    Sleep(600)
    OP_8C(0x1C, 0, 600)
    Sleep(300)
    Return()

    # Function_31_43EA end

    def Function_32_4420(): pass

    label("Function_32_4420")

    OP_8C(0x1B, 270, 600)
    Sleep(800)
    OP_8C(0x1B, 80, 600)
    Sleep(800)
    OP_8C(0x1B, 0, 600)
    Sleep(300)
    Return()

    # Function_32_4420 end

    def Function_33_4445(): pass

    label("Function_33_4445")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, -75000, 30000, -18700, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 271000, 0, 0)
    OP_E5(0x0, 0x0, 0x0, 262144)
    OP_E5(0x0, 0x0, 0x1, 262144)
    OP_E5(0x0, 0x0, 0x2, 262144)
    OP_E5(0x0, 0x0, 0x3, 262144)
    OP_E5(0x0, 0x0, 0x4, 262144)
    OP_E5(0x0, 0x0, 0x5, 262144)
    OP_E5(0x0, 0x0, 0x6, 262144)
    OP_E5(0x0, 0x0, 0x7, 262144)
    OP_E5(0x0, 0x0, 0x8, 262144)
    OP_E5(0x0, 0x0, 0x9, 262144)
    OP_E5(0x0, 0x0, 0xA, 262144)
    OP_E5(0x0, 0x0, 0xB, 262144)
    OP_E5(0x0, 0x0, 0xC, 262144)
    OP_E5(0x0, 0x0, 0xD, 262144)
    OP_E5(0x0, 0x0, 0xE, 262144)
    OP_E5(0x0, 0x0, 0xF, 262144)
    OP_E5(0x0, 0x0, 0x10, 262144)
    OP_E5(0x0, 0x0, 0x11, 262144)
    OP_E5(0x0, 0x0, 0x13, 262144)
    OP_E5(0x0, 0x0, 0x14, 262144)
    OP_E5(0x0, 0x0, 0x15, 262144)
    OP_E5(0x0, 0x0, 0x16, 262144)
    OP_E5(0x0, 0x0, 0x17, 262144)
    OP_E5(0x0, 0x0, 0x18, 262144)
    OP_E5(0x0, 0x0, 0x19, 262144)
    OP_E5(0x0, 0x0, 0x1A, 262144)
    OP_E5(0x0, 0x0, 0x1B, 262144)
    OP_E5(0x0, 0x0, 0x1C, 262144)
    OP_E5(0x0, 0x0, 0x1D, 262144)
    OP_E5(0x0, 0x0, 0x1E, 262144)
    OP_E5(0x2, 0x0, 0x0, 200)
    OP_E5(0x2, 0x0, 0x1, 200)
    OP_E5(0x2, 0x0, 0x2, 200)
    OP_E5(0x2, 0x0, 0x3, 200)
    OP_E5(0x2, 0x0, 0x4, 200)
    OP_E5(0x2, 0x0, 0x5, 200)
    OP_E5(0x2, 0x0, 0x6, 200)
    OP_E5(0x2, 0x0, 0x7, 200)
    OP_E5(0x2, 0x0, 0x8, 200)
    OP_E5(0x2, 0x0, 0x9, 200)
    OP_E5(0x2, 0x0, 0xA, 200)
    OP_E5(0x2, 0x0, 0xB, 200)
    OP_E5(0x2, 0x0, 0xC, 200)
    OP_E5(0x2, 0x0, 0xD, 200)
    OP_E5(0x2, 0x0, 0xE, 200)
    OP_E5(0x2, 0x0, 0xF, 200)
    OP_E5(0x2, 0x0, 0x10, 200)
    OP_E5(0x2, 0x0, 0x11, 200)
    OP_E5(0x2, 0x0, 0x13, 200)
    OP_E5(0x2, 0x0, 0x14, 200)
    OP_E5(0x2, 0x0, 0x15, 200)
    OP_E5(0x2, 0x0, 0x16, 200)
    OP_E5(0x2, 0x0, 0x17, 200)
    OP_E5(0x2, 0x0, 0x18, 200)
    OP_E5(0x2, 0x0, 0x19, 200)
    OP_E5(0x2, 0x0, 0x1A, 200)
    OP_E5(0x2, 0x0, 0x1B, 200)
    OP_E5(0x2, 0x0, 0x1C, 200)
    OP_E5(0x2, 0x0, 0x1D, 200)
    OP_E5(0x2, 0x0, 0x1E, 200)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x3C)
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFB0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFD8, 0xFFFFFFF6, 0x0, 0x0, 0x0)

    def lambda_47A8():

        label("loc_47A8")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_47A8")

    QueueWorkItem2(0x10, 2, lambda_47A8)
    OP_22(0x1C3, 0x0, 0x64)
    Sleep(3000)
    OP_6D(-200850, 45000, 4180, 0)
    OP_67(0, -2340, -10000, 0)
    OP_6B(6500, 0)
    OP_6C(10000, 0)
    OP_6E(748, 0)
    FadeToBright(2000, 0)

    def lambda_4813():
        OP_6D(-140000, 9000, 1500, 8000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4813)

    def lambda_482B():
        OP_67(0, 8500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_482B)

    def lambda_4843():
        OP_6B(7380, 8000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4843)

    def lambda_4853():
        OP_6C(30000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_4853)

    def lambda_4863():
        OP_6E(848, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4863)

    def lambda_4873():
        OP_D0(-3000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4873)
    WaitChrThread(0x20, 0x0)
    OP_43(0x10, 0x3, 0x0, 0x22)

    def lambda_488F():
        OP_6D(-57500, 9000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_488F)

    def lambda_48A7():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_48A7)
    WaitChrThread(0x20, 0x0)

    def lambda_48BC():
        OP_6B(6300, 15000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_48BC)

    def lambda_48CC():
        OP_6E(760, 15000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_48CC)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x69, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS542._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(4000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_43(0x10, 0x3, 0x0, 0x23)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_4445 end

    def Function_34_494E(): pass

    label("Function_34_494E")

    OP_22(0x2D5, 0x1, 0x0)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x32)
    Sleep(200)
    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x3C)
    Sleep(200)
    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x50)
    Sleep(200)
    OP_24(0x2D5, 0x5A)
    Sleep(200)
    OP_24(0x2D5, 0x64)
    Return()

    # Function_34_494E end

    def Function_35_49B7(): pass

    label("Function_35_49B7")

    OP_24(0x1C3, 0x5A)
    OP_24(0x2D5, 0x5A)
    Sleep(300)
    OP_24(0x1C3, 0x50)
    OP_24(0x2D5, 0x50)
    Sleep(300)
    OP_24(0x1C3, 0x46)
    OP_24(0x2D5, 0x46)
    Sleep(300)
    OP_24(0x1C3, 0x3C)
    OP_24(0x2D5, 0x3C)
    Sleep(300)
    OP_24(0x1C3, 0x32)
    OP_24(0x2D5, 0x32)
    Sleep(300)
    OP_24(0x1C3, 0x28)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    OP_23(0x1C3)
    OP_23(0x2D5)
    Return()

    # Function_35_49B7 end

    def Function_36_4A3B(): pass

    label("Function_36_4A3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 220000, 30000, -18700, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 271000, 0, 0)
    OP_E5(0x0, 0x0, 0x0, 262144)
    OP_E5(0x0, 0x0, 0x1, 262144)
    OP_E5(0x0, 0x0, 0x2, 262144)
    OP_E5(0x0, 0x0, 0x3, 262144)
    OP_E5(0x0, 0x0, 0x4, 262144)
    OP_E5(0x0, 0x0, 0x5, 262144)
    OP_E5(0x0, 0x0, 0x6, 262144)
    OP_E5(0x0, 0x0, 0x7, 262144)
    OP_E5(0x0, 0x0, 0x8, 262144)
    OP_E5(0x0, 0x0, 0x9, 262144)
    OP_E5(0x0, 0x0, 0xA, 262144)
    OP_E5(0x0, 0x0, 0xB, 262144)
    OP_E5(0x0, 0x0, 0xC, 262144)
    OP_E5(0x0, 0x0, 0xD, 262144)
    OP_E5(0x0, 0x0, 0xE, 262144)
    OP_E5(0x0, 0x0, 0xF, 262144)
    OP_E5(0x0, 0x0, 0x10, 262144)
    OP_E5(0x0, 0x0, 0x11, 262144)
    OP_E5(0x0, 0x0, 0x13, 262144)
    OP_E5(0x0, 0x0, 0x14, 262144)
    OP_E5(0x0, 0x0, 0x15, 262144)
    OP_E5(0x0, 0x0, 0x16, 262144)
    OP_E5(0x0, 0x0, 0x17, 262144)
    OP_E5(0x0, 0x0, 0x18, 262144)
    OP_E5(0x0, 0x0, 0x19, 262144)
    OP_E5(0x0, 0x0, 0x1A, 262144)
    OP_E5(0x0, 0x0, 0x1B, 262144)
    OP_E5(0x0, 0x0, 0x1C, 262144)
    OP_E5(0x0, 0x0, 0x1D, 262144)
    OP_E5(0x0, 0x0, 0x1E, 262144)
    OP_E5(0x2, 0x0, 0x0, 200)
    OP_E5(0x2, 0x0, 0x1, 200)
    OP_E5(0x2, 0x0, 0x2, 200)
    OP_E5(0x2, 0x0, 0x3, 200)
    OP_E5(0x2, 0x0, 0x4, 200)
    OP_E5(0x2, 0x0, 0x5, 200)
    OP_E5(0x2, 0x0, 0x6, 200)
    OP_E5(0x2, 0x0, 0x7, 200)
    OP_E5(0x2, 0x0, 0x8, 200)
    OP_E5(0x2, 0x0, 0x9, 200)
    OP_E5(0x2, 0x0, 0xA, 200)
    OP_E5(0x2, 0x0, 0xB, 200)
    OP_E5(0x2, 0x0, 0xC, 200)
    OP_E5(0x2, 0x0, 0xD, 200)
    OP_E5(0x2, 0x0, 0xE, 200)
    OP_E5(0x2, 0x0, 0xF, 200)
    OP_E5(0x2, 0x0, 0x10, 200)
    OP_E5(0x2, 0x0, 0x11, 200)
    OP_E5(0x2, 0x0, 0x13, 200)
    OP_E5(0x2, 0x0, 0x14, 200)
    OP_E5(0x2, 0x0, 0x15, 200)
    OP_E5(0x2, 0x0, 0x16, 200)
    OP_E5(0x2, 0x0, 0x17, 200)
    OP_E5(0x2, 0x0, 0x18, 200)
    OP_E5(0x2, 0x0, 0x19, 200)
    OP_E5(0x2, 0x0, 0x1A, 200)
    OP_E5(0x2, 0x0, 0x1B, 200)
    OP_E5(0x2, 0x0, 0x1C, 200)
    OP_E5(0x2, 0x0, 0x1D, 200)
    OP_E5(0x2, 0x0, 0x1E, 200)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x3C)
    LoadEffect(0x2, "map\\mp096_00.eff")
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFB0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFD8, 0xFFFFFFF6, 0x0, 0x0, 0x0)

    def lambda_4DB1():

        label("loc_4DB1")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_4DB1")

    QueueWorkItem2(0x10, 2, lambda_4DB1)
    OP_22(0x1C3, 0x0, 0x64)
    OP_6D(94640, 37400, -25730, 0)
    OP_67(0, -2910, -10000, 0)
    OP_6B(9310, 0)
    OP_6C(278000, 0)
    OP_6E(600, 0)

    def lambda_4E0E():
        OP_6D(93740, 41000, -19000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4E0E)

    def lambda_4E26():
        OP_67(0, -50, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4E26)

    def lambda_4E3E():
        OP_6B(14000, 15000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4E3E)

    def lambda_4E4E():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_4E4E)

    def lambda_4E5E():
        OP_6E(800, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_4E5E)
    StopSound(0x4E20, 0x927C0, 0x32C8)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 135000, 40000, -20700, 40, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_43(0x10, 0x3, 0x0, 0x27)
    OP_43(0x10, 0x0, 0x0, 0x25)
    Sleep(1000)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0x26)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("瑟尔纳特总长")

    AnonymousTalk(    #54 op#A op#5
        (
            "\x07\x0C#40A如果你不想\x01",
            "今后丢更多丑的话……\x02\x03\x05",

            "#45A就不要说胡话了。\x01",
            "还是和莉丝商量一下再决定吧。\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x10, 0x3)
    Sleep(3000)
    OP_1D(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0x0, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS477._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x96, 0x78, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS478._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x7, 0, -320000, 7000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(3000)
    OP_56(0x2)
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    OP_A2(0x2C27)
    OP_A2(0x2582)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2502)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05保存通关数据吗？\x18\x02",
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_50B1")

    label("loc_50B1")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50CA")
    OP_DC(0x0, 0x3)
    ShowSaveMenu()
    EventBegin(0x4)

    label("loc_50CA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    FadeToDark(0, 0, -1)
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_36_4A3B end

    def Function_37_50F6(): pass

    label("Function_37_50F6")


    def lambda_50FC():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_50FC)
    Sleep(500)

    def lambda_511C():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_511C)
    Sleep(500)

    def lambda_513C():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_513C)
    Sleep(3500)

    def lambda_515C():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_515C)
    Sleep(2500)

    def lambda_517C():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_517C)
    Sleep(1500)

    def lambda_519C():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_519C)
    Sleep(1000)

    def lambda_51BC():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_51BC)
    Sleep(500)
    Return()

    # Function_37_50F6 end

    def Function_38_51D7(): pass

    label("Function_38_51D7")

    Sleep(5000)
    OP_24(0x1C3, 0x5A)
    OP_24(0x2D5, 0x5A)
    Sleep(1000)
    OP_24(0x1C3, 0x50)
    OP_24(0x2D5, 0x50)
    Sleep(1000)
    OP_24(0x1C3, 0x46)
    OP_24(0x2D5, 0x46)
    Sleep(1000)
    OP_24(0x1C3, 0x3C)
    OP_24(0x2D5, 0x3C)
    Sleep(1000)
    OP_24(0x1C3, 0x32)
    OP_24(0x2D5, 0x32)
    Sleep(1000)
    OP_24(0x1C3, 0x28)
    OP_24(0x2D5, 0x28)
    Sleep(1000)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(1000)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(1000)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    Sleep(1000)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    OP_23(0x1C3)
    OP_23(0x2D5)
    Return()

    # Function_38_51D7 end

    def Function_39_5260(): pass

    label("Function_39_5260")

    OP_22(0x2D5, 0x1, 0x0)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x32)
    Sleep(100)
    OP_24(0x2D5, 0x46)
    Sleep(100)
    OP_24(0x2D5, 0x3C)
    Sleep(100)
    OP_24(0x2D5, 0x46)
    Sleep(100)
    OP_24(0x2D5, 0x50)
    Sleep(100)
    OP_24(0x2D5, 0x5A)
    Sleep(100)
    OP_24(0x2D5, 0x64)
    Return()

    # Function_39_5260 end

    SaveToFile()

Try(main)
