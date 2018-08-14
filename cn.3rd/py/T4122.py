from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4122   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4122.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '丹顿',                                 # 9
        '莉莉',                                 # 10
        '艾德尔店长',                           # 11
        '福鲁菲',                               # 12
        '蜜蒂',                                 # 13
        '基蒂',                                 # 14
        '特雷诺',                               # 15
        '希娜',                                 # 16
        '店员',                                 # 17
        '奈尔',                                 # 18
        '朵洛希',                               # 19
        '黑衣人',                               # 20
        '黑衣人',                               # 21
        '目标用照相机',                         # 22
        '',                                     # 23
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
        'ED6_DT27/CH03460 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02720 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01770 ._CH',             # 06
        'ED6_DT07/CH01070 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH01130 ._CH',             # 09
        'ED6_DT26/CH20680 ._CH',             # 0A
        'ED6_DT26/CH20681 ._CH',             # 0B
        'ED6_DT07/CH01010 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT27/CH03460P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02720P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01770P._CP',             # 06
        'ED6_DT07/CH01070P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH01130P._CP',             # 09
        'ED6_DT26/CH20680P._CP',             # 0A
        'ED6_DT26/CH20681P._CP',             # 0B
        'ED6_DT07/CH01010P._CP',             # 0C
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = 10,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13690,
        Z                   = 250,
        Y                   = 11270,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9140,
        Z                   = 0,
        Y                   = 10150,
        Direction           = 268,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9050,
        Z                   = 0,
        Y                   = 9400,
        Direction           = 271,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13590,
        Z                   = 0,
        Y                   = -8540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13060,
        Z                   = 0,
        Y                   = 6390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4590,
        Z                   = 0,
        Y                   = 9410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1370,
        TriggerZ            = 0,
        TriggerY            = 63610,
        TriggerRange        = 800,
        ActorX              = -1440,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1850,
        TriggerZ            = 0,
        TriggerY            = 63640,
        TriggerRange        = 800,
        ActorX              = 1970,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_3BA",          # 01, 1
        "Function_2_3CD",          # 02, 2
        "Function_3_54A",          # 03, 3
        "Function_4_56E",          # 04, 4
        "Function_5_573",          # 05, 5
        "Function_6_574",          # 06, 6
        "Function_7_579",          # 07, 7
        "Function_8_57A",          # 08, 8
        "Function_9_57F",          # 09, 9
        "Function_10_580",         # 0A, 10
        "Function_11_585",         # 0B, 11
        "Function_12_586",         # 0C, 12
        "Function_13_58B",         # 0D, 13
        "Function_14_58C",         # 0E, 14
        "Function_15_EF7",         # 0F, 15
        "Function_16_F21",         # 10, 16
        "Function_17_F82",         # 11, 17
        "Function_18_FBD",         # 12, 18
        "Function_19_1090",        # 13, 19
        "Function_20_1EAA",        # 14, 20
        "Function_21_1EF0",        # 15, 21
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3A8")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_3B9")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3B9")

    Return()

    # Function_0_386 end

    def Function_1_3BA(): pass

    label("Function_1_3BA")

    OP_B1("t4122_n")
    OP_10(0x6, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x4, 0x0)
    Return()

    # Function_1_3BA end

    def Function_2_3CD(): pass

    label("Function_2_3CD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_534")

    label("loc_3F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_534")

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_534")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_534")

    label("loc_43D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_456")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_534")

    label("loc_456")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_534")

    label("loc_46F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_534")

    label("loc_488")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_534")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_534")

    label("loc_4BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_534")

    label("loc_4D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_534")

    label("loc_4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_534")

    label("loc_505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_534")

    label("loc_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_534")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_549")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_534")

    label("loc_549")

    Return()

    # Function_2_3CD end

    def Function_3_54A(): pass

    label("Function_3_54A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56D")
    OP_8D(0xFE, -11560, -6690, -7260, -10580, 1000)
    Jump("Function_3_54A")

    label("loc_56D")

    Return()

    # Function_3_54A end

    def Function_4_56E(): pass

    label("Function_4_56E")

    Call(0, 5)
    Return()

    # Function_4_56E end

    def Function_5_573(): pass

    label("Function_5_573")

    Return()

    # Function_5_573 end

    def Function_6_574(): pass

    label("Function_6_574")

    Call(0, 7)
    Return()

    # Function_6_574 end

    def Function_7_579(): pass

    label("Function_7_579")

    Return()

    # Function_7_579 end

    def Function_8_57A(): pass

    label("Function_8_57A")

    Call(0, 9)
    Return()

    # Function_8_57A end

    def Function_9_57F(): pass

    label("Function_9_57F")

    Return()

    # Function_9_57F end

    def Function_10_580(): pass

    label("Function_10_580")

    Call(0, 11)
    Return()

    # Function_10_580 end

    def Function_11_585(): pass

    label("Function_11_585")

    Return()

    # Function_11_585 end

    def Function_12_586(): pass

    label("Function_12_586")

    Call(0, 13)
    Return()

    # Function_12_586 end

    def Function_13_58B(): pass

    label("Function_13_58B")

    Return()

    # Function_13_58B end

    def Function_14_58C(): pass

    label("Function_14_58C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_6D(600, 0, 600, 0)
    OP_67(0, 8640, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(65000, 0)
    OP_6E(332, 0)
    SetChrPos(0x103, 0, 0, 1300, 180)
    SetChrPos(0x151, 0, 0, -300, 270)

    def lambda_607():
        OP_67(0, 6640, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_607)

    def lambda_61F():
        OP_6B(2900, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_61F)

    def lambda_62F():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_62F)

    def lambda_63F():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_63F)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_8C(0x151, 90, 400)
    Sleep(1000)
    OP_8C(0x151, 180, 400)
    Sleep(1000)

    def lambda_675():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_675)
    WaitChrThread(0x151, 0x1)
    OP_43(0x151, 0x3, 0x0, 0xF)
    WaitChrThread(0x1D, 0x0)
    Sleep(1000)

    ChrTalk(    #0
        0x103,
        (
            "#1646F（……一开始\x01",
            "  就去百货店买东西啊。\x01",
            "  不愧是有钱人。）\x02\x03",

            "#1642F那，你要买什么？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x151, 0x3)
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #1
        0x151,
        (
            "#1654F是啊…………\x02\x03",

            "#1651F还是先补充一下\x01",
            "回复药吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x103,
        "#1643F啊？\x02",
    )

    CloseMessageWindow()

    def lambda_77F():

        label("loc_77F")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_77F")

    QueueWorkItem2(0x103, 3, lambda_77F)
    OP_62(0x151, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_7A7():
        OP_8E(0xFE, 0x94C, 0x0, 0x410, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7A7)
    WaitChrThread(0x151, 0x1)

    def lambda_7C7():
        OP_8E(0xFE, 0x14F0, 0x0, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7C7)
    WaitChrThread(0x151, 0x1)

    def lambda_7E7():
        OP_8E(0xFE, 0x2238, 0x0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7E7)
    Sleep(500)
    OP_44(0x103, 0x3)
    OP_43(0x103, 0x3, 0x0, 0x10)
    WaitChrThread(0x151, 0x1)

    def lambda_817():
        OP_8E(0xFE, 0x2238, 0x0, 0x2198, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_817)
    Fade(1000)
    OP_6D(9860, 0, 7840, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x151, 0x1)
    OP_43(0x151, 0x3, 0x0, 0x11)
    WaitChrThread(0x103, 0x3)
    Sleep(2000)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)
    OP_8C(0x103, 180, 400)
    Sleep(300)

    ChrTalk(    #3
        0x103,
        "#1648F（啊～好无聊～……）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_8C(0x103, 90, 400)
    Sleep(500)

    ChrTalk(    #4
        0x103,
        "#1643F……咦？\x02",
    )

    CloseMessageWindow()

    def lambda_91A():
        OP_8E(0xFE, 0x2774, 0x0, 0x139C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_91A)
    WaitChrThread(0x103, 0x1)
    Sleep(500)

    ChrTalk(    #5
        0x103,
        (
            "#1643F（这本书，\x01",
            "  不是克鲁茨前辈正在看的吗。）\x02\x03",

            "#1640F（哦，\x01",
            "  原来他是在这里买的啊……）\x02\x03",

            "（唔，\x01",
            "  还有很多看起来好难的书……）\x02",
        )
    )

    Jump("loc_9DD")

    label("loc_9DD")

    CloseMessageWindow()
    Sleep(1000)
    OP_44(0x151, 0x3)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x151, 270, 400)
    Sleep(500)

    def lambda_A15():
        OP_6D(3500, 0, 8600, 4000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_A15)
    WaitChrThread(0x1D, 0x0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1B, 0, 0, 10500, 180)
    SetChrPos(0x1C, 0, 0, 10500, 180)

    def lambda_A78():
        OP_8E(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A78)
    Sleep(1000)

    def lambda_A98():
        OP_8E(0xFE, 0x0, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A98)
    Sleep(1000)

    def lambda_AB8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_AB8)
    WaitChrThread(0x1B, 0x1)
    Sleep(300)

    def lambda_AD0():
        OP_8E(0xFE, 0x2238, 0x0, 0x139C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_AD0)
    OP_8C(0x1B, 0, 400)
    WaitChrThread(0x1C, 0x1)
    OP_70(0x0, 0x0)
    Sleep(1500)
    OP_8C(0x1B, 180, 400)
    Sleep(300)

    def lambda_B0F():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_B0F)

    def lambda_B2A():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B2A)
    Sleep(500)

    def lambda_B4A():
        OP_6D(9500, 0, 5020, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_B4A)
    Sleep(700)

    def lambda_B67():
        OP_8E(0xFE, 0x2328, 0x0, 0x139C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_B67)
    WaitChrThread(0x151, 0x1)
    WaitChrThread(0x1D, 0x0)

    ChrTalk(    #6
        0x151,
        "#1652F……雪拉扎德小姐！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #7
        0x103,
        "#1643F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x151,
        (
            "#1654F那个…………\x02\x03",

            "#1651F这附近，\x01",
            "有家很有名的冰淇淋店哦。\x02\x03",

            "…………你知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#1642F不、不知道啦。\x02\x03",

            "我不喜欢甜的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x151,
        (
            "#1651F我好久没吃冰淇淋了，\x01",
            "真想尝尝啊……\x02\x03",

            "好，走吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CCB():
        OP_8E(0xFE, 0x24CC, 0x0, 0x139C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_CCB)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #11
        0x103,
        "#1643F等……等一下！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x151, 270, 500)
    Sleep(300)
    OP_43(0x103, 0x3, 0x0, 0x12)

    def lambda_D26():
        OP_8E(0xFE, 0x2328, 0x0, 0x139C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D26)
    WaitChrThread(0x151, 0x1)

    def lambda_D46():
        OP_8E(0xFE, 0x2030, 0x0, 0x1068, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D46)
    WaitChrThread(0x151, 0x1)

    def lambda_D66():
        OP_8E(0xFE, 0x2030, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D66)
    WaitChrThread(0x151, 0x1)

    def lambda_D86():
        OP_8E(0xFE, 0x2328, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D86)
    WaitChrThread(0x151, 0x1)
    OP_70(0x1, 0x3B)

    def lambda_DAD():
        OP_8E(0xFE, 0x27D8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_DAD)
    WaitChrThread(0x151, 0x1)

    def lambda_DCD():
        OP_8E(0xFE, 0x30D4, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_DCD)

    def lambda_DE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_DE8)
    WaitChrThread(0x151, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    SetChrPos(0x1B, -3500, 0, 0, 90)
    SetChrPos(0x1C, 800, 0, -2000, 180)

    def lambda_E29():
        OP_6D(600, 0, 600, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_E29)

    def lambda_E41():
        OP_8E(0xFE, 0x320, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_E41)
    Sleep(300)

    def lambda_E61():
        OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_E61)
    WaitChrThread(0x1C, 0x1)
    OP_8C(0x1C, 270, 400)
    WaitChrThread(0x1B, 0x1)
    WaitChrThread(0x1D, 0x0)
    Sleep(1500)
    OP_8C(0x1C, 90, 400)

    def lambda_E9E():
        OP_8E(0xFE, 0x1A90, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_E9E)
    Sleep(300)
    OP_8C(0x1B, 0, 400)

    def lambda_EC5():
        OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_EC5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2F4B)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T4101   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_58C end

    def Function_15_EF7(): pass

    label("Function_15_EF7")

    Sleep(1000)
    OP_8C(0x151, 90, 400)
    Sleep(1000)
    OP_8C(0x151, 270, 400)
    Sleep(1000)
    OP_8C(0x151, 180, 400)
    Sleep(1000)
    Return()

    # Function_15_EF7 end

    def Function_16_F21(): pass

    label("Function_16_F21")


    def lambda_F27():
        OP_8E(0xFE, 0x14F0, 0x0, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F27)
    WaitChrThread(0x103, 0x1)

    def lambda_F47():
        OP_8E(0xFE, 0x2238, 0x0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F47)
    WaitChrThread(0x103, 0x1)

    def lambda_F67():
        OP_8E(0xFE, 0x2238, 0x0, 0x13D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F67)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_16_F21 end

    def Function_17_F82(): pass

    label("Function_17_F82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FBC")
    OP_62(0x151, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_17_F82")

    label("loc_FBC")

    Return()

    # Function_17_F82 end

    def Function_18_FBD(): pass

    label("Function_18_FBD")


    def lambda_FC3():
        OP_8F(0xFE, 0x2328, 0x0, 0x139C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FC3)
    WaitChrThread(0x103, 0x1)

    def lambda_FE3():
        OP_8F(0xFE, 0x2030, 0x0, 0x1068, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FE3)
    WaitChrThread(0x103, 0x1)

    def lambda_1003():
        OP_8F(0xFE, 0x2030, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1003)
    WaitChrThread(0x103, 0x1)

    def lambda_1023():
        OP_8F(0xFE, 0x2328, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1023)
    WaitChrThread(0x103, 0x1)

    def lambda_1043():
        OP_8F(0xFE, 0x27D8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1043)
    WaitChrThread(0x103, 0x1)

    def lambda_1063():
        OP_8F(0xFE, 0x30D4, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1063)

    def lambda_107E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_107E)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_18_FBD end

    def Function_19_1090(): pass

    label("Function_19_1090")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -7480, 0, 9900, 180)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 4)), scpexpr(EXPR_END)), "loc_16DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 2)), scpexpr(EXPR_END)), "loc_128E")
    OP_6D(13340, 0, -6080, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 4600, 0, 11400, 180)
    SetChrPos(0x151, 4600, 0, 11400, 180)
    SetChrPos(0x1A, 13040, 0, -7900, 90)
    SetChrPos(0x19, 11220, 0, -7220, 90)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)

    def lambda_1160():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1160)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1D, 0x1)

    NpcTalk(    #12
        0x19,
        "眼神凶恶的男子",
        (
            "#142F喂，把那个给我啦。\x02\x03",

            "我要拿去显像……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x1A,
        "长雀斑的少女",
        "#1661F啊，摆个胜利手势吧。\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("loc_16D9")

    label("loc_128E")

    OP_6D(13340, 0, -6080, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 4600, 0, 11400, 180)
    SetChrPos(0x151, 4600, 0, 11400, 180)
    SetChrPos(0x1A, 13040, 0, -7900, 90)
    SetChrPos(0x19, 11220, 0, -7220, 90)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)

    def lambda_131F():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_131F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1D, 0x1)

    NpcTalk(    #14
        0x19,
        "眼神凶恶的男子",
        (
            "#143F喂、喂……\x01",
            "这个照片，是你拍的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1A, 10)
    SetChrSubChip(0x1A, 0)
    OP_8C(0x1A, 270, 500)
    Sleep(300)

    NpcTalk(    #15
        0x1A,
        "长雀斑的少女",
        "#1660F#11P哎？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x19,
        "眼神凶恶的男子",
        (
            "#145F不、不可能吧。\x02\x03",

            "是不是偶然\x01",
            "混进来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x19, 270, 500)
    Sleep(300)

    NpcTalk(    #17
        0x19,
        "眼神凶恶的男子",
        (
            "#140F（虽然是寻常的街边树木……）\x02\x03",

            "（但那坚实挺拔的枝干\x01",
            "  和阳光下通透灵动的树叶，\x01",
            "  生机勃勃广延舒展的叶脉……）\x02\x03",

            "（一张一张\x01",
            "  刻画得都是那么生动……）\x02\x03",

            "#142F（这、这样的照片……\x01",
            "  不是专业人士怎么可能拍得出来……！）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x1A,
        "长雀斑的少女",
        "#1660F#11P看起来很好吃吧～？\x02",
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x19, 90, 500)
    Sleep(500)

    NpcTalk(    #19
        0x19,
        "眼神凶恶的男子",
        "#142F啊？\x02",
    )

    Jump("loc_15A6")

    label("loc_15A6")

    CloseMessageWindow()

    NpcTalk(    #20
        0x1A,
        "长雀斑的少女",
        (
            "#1661F#11P嘻嘻，\x01",
            "那棵树是薄荷味的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1A, 90, 500)
    Sleep(500)

    NpcTalk(    #21
        0x1A,
        "长雀斑的少女",
        (
            "#1660F照相机好有趣哦～。\x02\x03",

            "里面有好多东西骨碌碌地转着，\x01",
            "好像万花筒一样。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x19,
        "眼神凶恶的男子",
        (
            "#142F（莫、莫名其妙……）\x02\x03",

            "（她就是用这种乱七八糟的感觉\x01",
            "  拍出这样出色的照片的吗？？）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x2F5A)

    label("loc_16D9")

    Jump("loc_1E3C")

    label("loc_16DC")

    OP_6D(-8300, 0, 8720, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 4600, 0, 11400, 180)
    SetChrPos(0x151, 4600, 0, 11400, 180)
    SetChrPos(0x1A, -7020, 0, 1960, 90)
    SetChrFlags(0x1A, 0x8)
    SetChrPos(0x19, 11220, 0, -6920, 90)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)
    OP_43(0x1B, 0x3, 0x0, 0x14)

    def lambda_1779():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1779)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)

    NpcTalk(    #23 op#A
        0x1A,
        "少女的声音",
        "#20A#1P嗯，非常可爱哦～⊙\x02",
    )

    Sleep(2000)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 13040, 0, -7900, 90)

    def lambda_17E3():
        OP_6D(13340, 0, -6080, 5000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_17E3)
    WaitChrThread(0x1D, 0x0)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #24
        0x19,
        "眼神凶恶的男子",
        (
            "#142F喂，快还给我啦！\x02\x03",

            "这不是像你这样的小鬼\x01",
            "可以随便玩弄的东西啊！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #25
        0x1A,
        "长雀斑的少女",
        (
            "#1661F嘻嘻，\x01",
            "竟然有这么多表情呢～。\x02\x03",

            "我原来可是\x01",
            "一点都不知道～。\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x1A, 0x32F0, 0x0, 0xFFFFE37C, 0x5DC, 0x0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #26
        0x1A,
        "长雀斑的少女",
        (
            "#1660F好，\x01",
            "下次再华丽一点吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x1A, 0x32F0, 0x0, 0xFFFFDECC, 0x5DC, 0x0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1A, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x1A, 0x3, 0x0, 0x15)
    OP_62(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #27
        0x19,
        "眼神凶恶的男子",
        (
            "#145F不行了…………\x01",
            "开始胡言乱语了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "啊，客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "刚才的感光结晶回路，\x01",
            "已经显像好了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 500)
    Sleep(300)

    NpcTalk(    #30
        0x19,
        "眼神凶恶的男子",
        (
            "#147F#12P啊，好的。\x01",
            "抱歉，这么急着让你……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BBF():
        OP_8F(0xFE, 0x2D1E, 0x0, 0xFFFFE8AE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BBF)
    WaitChrThread(0x19, 0x1)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #31
        0x19,
        "眼神凶恶的男子",
        "#143F#12P这、这是…………！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x19, 135, 500)
    Sleep(300)

    NpcTalk(    #32
        0x1A,
        "长雀斑的少女",
        (
            "#1661F呼呼呼～……#100W哦#20W！\x02\x03",

            "啦啦啦～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #33
        0x19,
        "眼神凶恶的男子",
        (
            "#145F不、不，这不可能……\x02\x03",

            "那种小鬼，\x01",
            "不可能拍出这么好的照片……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "对了，这位客人，\x01",
            "请付一下显像\x01",
            "和感光结晶回路的钱……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 500)
    Sleep(300)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #35
        0x19,
        "眼神凶恶的男子",
        (
            "#140F#12P啊、啊啊……不好意思。\x01",
            "我稍微有点混乱……\x02\x03",

            "那么，嗯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        "７套一共１０５０米拉。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #37
        0x19,
        "眼神凶恶的男子",
        "#143F#3S#12P…………噗！？#2S\x02",
    )

    Sleep(50)
    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_A2(0x2F54)

    label("loc_1E3C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E64")
    NewScene("ED6_DT21/T4101   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1EA9")

    label("loc_1E64")

    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7C")
    NewScene("ED6_DT21/T4101   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_1EA9")

    label("loc_1E7C")

    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E94")
    NewScene("ED6_DT21/T4101   ._SN", 107, 0, 0)
    IdleLoop()
    Jump("loc_1EA9")

    label("loc_1E94")

    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA9")
    NewScene("ED6_DT21/T4101   ._SN", 108, 0, 0)
    IdleLoop()

    label("loc_1EA9")

    Return()

    # Function_19_1090 end

    def Function_20_1EAA(): pass

    label("Function_20_1EAA")


    def lambda_1EB0():
        OP_8E(0xFE, 0xFFFFE2C8, 0x0, 0x116C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1EB0)
    WaitChrThread(0x1B, 0x1)
    Sleep(300)

    def lambda_1ED5():
        OP_8E(0xFE, 0xFFFFCA2C, 0x0, 0x116C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1ED5)
    WaitChrThread(0x1B, 0x1)
    Return()

    # Function_20_1EAA end

    def Function_21_1EF0(): pass

    label("Function_21_1EF0")

    Sleep(1700)

    label("loc_1EF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F33")
    OP_8F(0x1A, 0x32F0, 0x0, 0xFFFFE37C, 0x3E8, 0x0)
    Sleep(2000)
    OP_8F(0x1A, 0x32F0, 0x0, 0xFFFFDECC, 0x3E8, 0x0)
    Sleep(2000)
    Jump("loc_1EF5")

    label("loc_1F33")

    Return()

    # Function_21_1EF0 end

    SaveToFile()

Try(main)
