from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '米拉诺',                               # 9
        '秘书凯诺娜',                           # 10
        '诺曼市长',                             # 11
        '船',                                   # 12
        '目标用照相机',                         # 13
        '哈尔德',                               # 14
        '哈古',                                 # 15
        '布兰塔婆婆',                           # 16
        '阿伊纳街道方向',                       # 17
        '卢安市·北街区',                       # 18
        '',                                     # 19
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
        'ED6_DT07/CH01760 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01110 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH00472 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01080 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH01680 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01190 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01390 ._CH',             # 14
        'ED6_DT07/CH02530 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT26/CH20797 ._CH',             # 17
        'ED6_DT07/CH01200 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01760P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01110P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH00472P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01080P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH01680P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01190P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01390P._CP',             # 14
        'ED6_DT07/CH02530P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT26/CH20797P._CP',             # 17
        'ED6_DT07/CH01200P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xA0,
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
        X                   = 30790,
        Z                   = 0,
        Y                   = 9980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35750,
        Z                   = 0,
        Y                   = 25180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75930,
        Z                   = 0,
        Y                   = 10740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_3BF",          # 01, 1
        "Function_2_47B",          # 02, 2
        "Function_3_5F8",          # 03, 3
        "Function_4_618",          # 04, 4
        "Function_5_63C",          # 05, 5
        "Function_6_83B",          # 06, 6
        "Function_7_E31",          # 07, 7
        "Function_8_E8B",          # 08, 8
        "Function_9_1244",         # 09, 9
        "Function_10_12A5",        # 0A, 10
        "Function_11_12ED",        # 0B, 11
        "Function_12_12F4",        # 0C, 12
        "Function_13_12F8",        # 0D, 13
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_38C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_3BE")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3AB")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_3BE")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3BE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_3BE")

    Return()

    # Function_0_35E end

    def Function_1_3BF(): pass

    label("Function_1_3BF")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F8")
    OP_A3(0x0)
    OP_B1("T2101_1")
    Jump("loc_401")

    label("loc_3F8")

    OP_B1("T2101_0")

    label("loc_401")

    OP_72(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 60)
    OP_72(0x1012, 0x0)
    ExitThread()
    OP_72(0x1014, 0x0)
    ExitThread()
    OP_72(0x1015, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_64(0x3, 0x1)
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_1C(0x13, 0x0, 0xB)
    OP_82(0x87, 0x0)
    Return()

    # Function_1_3BF end

    def Function_2_47B(): pass

    label("Function_2_47B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5E2")

    label("loc_4A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5E2")

    label("loc_4B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5E2")

    label("loc_4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5E2")

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5E2")

    label("loc_504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5E2")

    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5E2")

    label("loc_536")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5E2")

    label("loc_54F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_568")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5E2")

    label("loc_568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5E2")

    label("loc_581")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5E2")

    label("loc_59A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5E2")

    label("loc_5B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5E2")

    label("loc_5CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5E2")

    label("loc_5F7")

    Return()

    # Function_2_47B end

    def Function_3_5F8(): pass

    label("Function_3_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x1, 0x7, 0xBB8)
    SetChrSubChip(0xFE, 0)
    Sleep(250)
    Jump("Function_3_5F8")

    label("loc_617")

    Return()

    # Function_3_5F8 end

    def Function_4_618(): pass

    label("Function_4_618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63B")
    OP_8D(0xFE, 48840, 21930, 53280, 24890, 2000)
    Jump("Function_4_618")

    label("loc_63B")

    Return()

    # Function_4_618 end

    def Function_5_63C(): pass

    label("Function_5_63C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 79860, 4000, -920, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, 83000, 3500, -920, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 45750, 0, 25250, 0)
    SetChrPos(0x16, 73700, 0, 21410, 270)

    def lambda_6AB():
        OP_8F(0xFE, 0x68CE, 0x0, 0x53A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6AB)
    OP_6D(51000, 0, 33880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(600, 0)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)

    def lambda_721():
        OP_6D(80560, 0, 2360, 14000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_721)

    def lambda_739():
        OP_67(0, 6540, -10000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_739)

    def lambda_751():
        OP_6C(135000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_751)

    def lambda_761():
        OP_6E(384, 14000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_761)
    WaitChrThread(0x14, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Ｒ＆Ａ Research　卢安事务所\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    ChrTalk(    #1
        0x10,
        "#4P哦哦，这不是……\x02",
    )

    CloseMessageWindow()
    SetPlaceName(0x69)

    NpcTalk(    #2
        0x10C,
        "所长",
        (
            "#3P如果能帮上忙的话\x01",
            "就再好不过了……\x02",
        )
    )

    Jump("loc_812")

    label("loc_812")

    CloseMessageWindow()

    def lambda_819():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_819)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2110   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_5_63C end

    def Function_6_83B(): pass

    label("Function_6_83B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(79240, 0, 6460, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(404, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10C, 79240, 500, 5000, 270)
    SetChrPos(0x11, 79240, 500, 5000, 270)
    SetChrPos(0x12, 79240, 500, 5000, 270)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8E8():
        OP_67(0, 6540, -10000, 7200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8E8)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x100F, 0x0)
    ExitThread()
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    Sleep(100)

    def lambda_91F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_91F)

    def lambda_931():
        OP_8E(0xFE, 0x123B8, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_931)
    Sleep(700)
    OP_43(0x11, 0x3, 0x0, 0x7)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 90, 400)

    def lambda_964():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_964)

    def lambda_976():
        OP_8E(0xFE, 0x1291C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_976)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    Fade(1000)
    OP_44(0x14, 0x0)
    OP_6D(75500, 0, 5080, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_6D(76280, 0, 5360, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10C)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_8C(0x12, 0, 400)

    def lambda_A79():

        label("loc_A79")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_A79")

    QueueWorkItem2(0x10C, 2, lambda_A79)

    def lambda_A8A():

        label("loc_A8A")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_A8A")

    QueueWorkItem2(0x11, 2, lambda_A8A)

    def lambda_A9B():
        OP_6D(76090, 0, 6470, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A9B)

    def lambda_AB3():
        OP_8E(0xFE, 0x1291C, 0x0, 0x445C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AB3)
    WaitChrThread(0x12, 0x1)

    def lambda_AD3():
        OP_6D(75890, 0, 5130, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_AD3)
    OP_44(0x10C, 0x2)
    OP_44(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    Sleep(500)

    NpcTalk(    #3
        0x10C,
        "理查德所长",
        (
            "#1850F#5P这个工作\x01",
            "终于也上了轨道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#1862F#12P嗯嗯…………\x02\x03",

            "#1861F虽说稍微欠缺紧张感\x01",
            "算是美中不足吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x11, 400)
    Sleep(300)

    NpcTalk(    #5
        0x10C,
        "理查德所长",
        (
            "#1851F#5P哈哈，忍耐一下吧。\x01",
            "我们现在也是平民了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#1861F#12P…………是啊。\x02\x03",

            "#1862F不过，\x01",
            "能在阁下出生的故乡\x01",
            "过这样的生活的确很荣幸……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10C,
        "理查德所长",
        (
            "#1855F#5P……凯诺娜。\x02\x03",

            "#1850F刚才你应该称呼我『所长』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        "#1864F#12P啊………………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #9
        0x11,
        "#1861F#12P失、失礼了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10C,
        "理查德所长",
        (
            "#1851F#5P哈哈，\x01",
            "不需要道歉啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x168, 0x0, 0x64)
    OP_77(0xA0, 0xA0, 0xA0, 0x0, 0x7D0)
    Sleep(2500)
    OP_8C(0x10C, 270, 400)
    Sleep(500)

    NpcTalk(    #11
        0x10C,
        "理查德所长",
        (
            "#1850F#5P…………进屋吧。\x01",
            "似乎快要变天了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_DA3():

        label("loc_DA3")

        TurnDirection(0xFE, 0x10C, 500)
        OP_48()
        Jump("loc_DA3")

    QueueWorkItem2(0x11, 2, lambda_DA3)
    OP_8C(0x10C, 90, 500)

    def lambda_DBB():
        OP_8E(0xFE, 0x13588, 0x1F4, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_DBB)
    Sleep(500)
    OP_44(0x11, 0x2)

    def lambda_DDF():
        OP_8E(0xFE, 0x12804, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DDF)
    WaitChrThread(0x11, 0x1)

    def lambda_DFF():
        OP_8E(0xFE, 0x13588, 0x1F4, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2110   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_6_83B end

    def Function_7_E31(): pass

    label("Function_7_E31")


    def lambda_E37():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_E37)

    def lambda_E49():
        OP_8E(0xFE, 0x12804, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E49)
    WaitChrThread(0x11, 0x1)

    def lambda_E69():
        OP_8E(0xFE, 0x123B8, 0x0, 0xF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E69)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 45, 400)
    Return()

    # Function_7_E31 end

    def Function_8_E8B(): pass

    label("Function_8_E8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    SoundLoad(457)
    OP_11(0x0, 0x0, 0x0, 0x80E8, 0x1FBD0, 0x0)
    OP_6D(72140, 0, 23640, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(500, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, 72220, 0, 7120, 0)
    OP_43(0x10C, 0x3, 0x0, 0x9)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1600)

    ChrTalk(    #12 op#A
        0x10C,
        "#11P#1855F#25A（………唔…………）\x02",
    )

    Sleep(400)

    def lambda_F60():
        OP_6D(50800, 0, 30160, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_F60)

    def lambda_F78():
        OP_6C(320000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F78)

    def lambda_F88():
        OP_6E(410, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_F88)
    Sleep(4400)

    ChrTalk(    #13 op#A
        0x10C,
        "#5P#1856F#15A（那封信是…………）\x02",
    )

    WaitChrThread(0x14, 0x0)
    Sleep(2000)
    PlayEffect(0x0, 0xFF, 0xFF, 50800, 0, 30160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x1, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Sleep(3000)
    WaitChrThread(0x10C, 0x3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x18\x07\x0C那封信的粘贴方法，\x01",
            "是情报部所使用的特殊方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x18\x07\x0C信的内容是伪装的，\x01",
            "实际的文章以信封的\x01",
            "粘贴方法作为暗号。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #16
        "\x18\x07\x0C……『速来飞艇坪』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x18\x07\x0C原情报部的人\x01",
            "在叫我出去……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x18\x07\x0C恐怕是怀有\x01",
            "想传达给我的负面感情―――……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x169, 0x0, 0x50)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x18\x07\x0C………我必须去一趟。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        "\x18\x07\x0C身为原情报部将校……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x18\x07\x0C也作为扰乱他们人生的\x01",
            "罪魁祸首…………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_E8B end

    def Function_9_1244(): pass

    label("Function_9_1244")


    def lambda_124A():
        OP_8E(0xFE, 0x11A1C, 0x0, 0x56E0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_124A)
    WaitChrThread(0x10C, 0x1)

    def lambda_126A():
        OP_8E(0xFE, 0xCABC, 0x0, 0x57A8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_126A)
    WaitChrThread(0x10C, 0x1)

    def lambda_128A():
        OP_8E(0xFE, 0xC738, 0x0, 0xA500, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_128A)
    WaitChrThread(0x10C, 0x1)
    Return()

    # Function_9_1244 end

    def Function_10_12A5(): pass

    label("Function_10_12A5")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_12A5 end

    def Function_11_12ED(): pass

    label("Function_11_12ED")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_11_12ED end

    def Function_12_12F4(): pass

    label("Function_12_12F4")

    SetPlaceName(0x69)
    Return()

    # Function_12_12F4 end

    def Function_13_12F8(): pass

    label("Function_13_12F8")

    SetPlaceName(0x52)
    Return()

    # Function_13_12F8 end

    SaveToFile()

Try(main)
