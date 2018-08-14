from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
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
        '艾南',                                 # 9
        '金',                                   # 10
        '爱娜',                                 # 11
        '克鲁茨',                               # 12
        '卡西乌斯',                             # 13
        '费瑟尔',                               # 14
        '罗伊德',                               # 15
        '搬家公司职员',                         # 16
        '拜舍尔',                               # 17
        '目标用照相机',                         # 18
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH00070 ._CH',             # 01
        'ED6_DT07/CH02710 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01450 ._CH',             # 06
        'ED6_DT07/CH01460 ._CH',             # 07
        'ED6_DT07/CH00071 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH00070P._CP',             # 01
        'ED6_DT07/CH02710P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01450P._CP',             # 06
        'ED6_DT07/CH01460P._CP',             # 07
        'ED6_DT07/CH00071P._CP',             # 08
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        X                   = 26440,
        Z                   = 0,
        Y                   = 59870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 32080,
        Z                   = 0,
        Y                   = 63600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 32080,
        Z                   = 0,
        Y                   = 61480,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 33280,
        Z                   = 0,
        Y                   = 63470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TriggerX            = -3480,
        TriggerZ            = 0,
        TriggerY            = -450,
        TriggerRange        = 800,
        ActorX              = -4480,
        ActorZ              = 1500,
        ActorY              = -550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28140,
        TriggerZ            = 0,
        TriggerY            = 61240,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3370,
        TriggerZ            = 0,
        TriggerY            = 40,
        TriggerRange        = 1400,
        ActorX              = -3370,
        ActorZ              = 1600,
        ActorY              = 40,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_3C8",          # 01, 1
        "Function_2_466",          # 02, 2
        "Function_3_5E3",          # 03, 3
        "Function_4_5E8",          # 04, 4
        "Function_5_5E9",          # 05, 5
        "Function_6_656",          # 06, 6
        "Function_7_9A9",          # 07, 7
        "Function_8_1CF5",         # 08, 8
        "Function_9_1D7D",         # 09, 9
        "Function_10_1DDE",        # 0A, 10
        "Function_11_1FFA",        # 0B, 11
        "Function_12_21EC",        # 0C, 12
        "Function_13_23A6",        # 0D, 13
        "Function_14_2470",        # 0E, 14
        "Function_15_286E",        # 0F, 15
        "Function_16_3174",        # 10, 16
        "Function_17_31F7",        # 11, 17
        "Function_18_499D",        # 12, 18
        "Function_19_4A41",        # 13, 19
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_10(0x6, 0x0)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2F3")
    Jump("loc_380")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_355")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_END)), "loc_31A")
    SetChrPos(0x13, -5880, 0, -3660, 270)
    Jump("loc_32B")

    label("loc_31A")

    SetChrPos(0x13, -5600, 0, 100, 270)

    label("loc_32B")

    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, 34270, 0, 56020, 90)
    SetChrPos(0x16, 32080, 0, 63600, 90)
    Jump("loc_380")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_35F")
    Jump("loc_380")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_380")
    OP_65(0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -4480, 0, -550, 90)

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A8")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_3A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3C7")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_3C7")

    Return()

    # Function_0_2C2 end

    def Function_1_3C8(): pass

    label("Function_1_3C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E0")
    OP_B1("t4121_n")
    Jump("loc_3E9")

    label("loc_3E0")

    OP_B1("t4121_y")

    label("loc_3E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()

    label("loc_401")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_465")

    Return()

    # Function_1_3C8 end

    def Function_2_466(): pass

    label("Function_2_466")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5CD")

    label("loc_48B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5CD")

    label("loc_4A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5CD")

    label("loc_4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5CD")

    label("loc_4D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5CD")

    label("loc_4EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5CD")

    label("loc_508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5CD")

    label("loc_521")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5CD")

    label("loc_53A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5CD")

    label("loc_553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5CD")

    label("loc_56C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5CD")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5CD")

    label("loc_59E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5CD")

    label("loc_5B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5CD")

    label("loc_5E2")

    Return()

    # Function_2_466 end

    def Function_3_5E3(): pass

    label("Function_3_5E3")

    Call(0, 7)
    Return()

    # Function_3_5E3 end

    def Function_4_5E8(): pass

    label("Function_4_5E8")

    Return()

    # Function_4_5E8 end

    def Function_5_5E9(): pass

    label("Function_5_5E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_655")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05没有什么委托。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #1
        0x103,
        "#1642F唉…………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_655")

    Return()

    # Function_5_5E9 end

    def Function_6_656(): pass

    label("Function_6_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6AD")

    ChrTalk(    #2
        0x103,
        (
            "#1646F我啊……\x01",
            "到底什么时候才能……\x02\x03",

            "…………嘟嘟囔囔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A5")

    label("loc_6AD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05　　　　◆　  委托公告板  　◆　　\x01",
            " 6:02 替换街道路灯（王都前）　  　　Ｋ\x01",
            " 6:14 庭院大道·通缉魔兽　　　　　　Ｋ\x01",
            " 6:17 发送物资（格鲁纳门）　　　　　Ｋ\x01",
            " 7:44 艾利兹街道·安全性调查　　　　Ｋ\x01",
            " 9:32 帮忙搬家（隔壁？）　 　　  　 Ｓ\x01",
            " 9:33 药草配送　　　　　　　　　　　Ｋ\x01",
            " 9:55 护卫旅行者（圣海姆门～王都）　Ｋ\x01",
            "10:02 搜索遗失物（共和国大使馆）　　Ｋ\x01",
            "10:28 运送货物（王都＋艾尔贝离宫）　Ｓ\x01",
            "10:32 修理屋顶（西街区·民家）　　　Ｋ\x01",
            "10:58 监督危险品的运输（港口）　　　Ｋ\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #4
        0x103,
        (
            "#1646F（唔…………）\x02\x03",

            "（克鲁茨前辈，\x01",
            "  身手还是这么麻利……）\x02\x03",

            "#1642F（等一下……\x01",
            "  『6:02 替换街道路灯』是什么啊。）\x02\x03",

            "#1645F这任务\x01",
            "也太没意思了吧……\x01",
            "…………（嘟嘟囔囔）……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 0)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x5)

    label("loc_9A5")

    TalkEnd(0xFF)
    Return()

    # Function_6_656 end

    def Function_7_9A9(): pass

    label("Function_7_9A9")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9B6")
    Jump("loc_1CF1")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_144E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 6)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A23")
    OP_8C(0x13, 270, 0)

    ChrTalk(    #5
        0x13,
        (
            "#840F资料的排列顺序都乱了啊。\x02\x03",

            "要重新整理好才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_A23")

    OP_8C(0x13, 270, 0)

    ChrTalk(    #6
        0x13,
        (
            "#842F哎…………？\x02\x03",

            "’９３·６……’９５·２……\x01",
            "……’９３·４……\x02\x03",

            "#843F资料的排列顺序都乱了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        "#1643F（糟糕…………！？）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AD2")

    Jump("loc_BBD")

    label("loc_AD5")

    OP_8C(0x13, 270, 0)

    ChrTalk(    #8
        0x13,
        "#841F呼，这样就行了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#1643F……前辈，您在做什么呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #10
        0x13,
        (
            "#840F啊，稍微清扫一下。\x02\x03",

            "一楼进进出出的人很多，\x01",
            "很快就会积上灰尘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        "#1645F（……这也太认真了吧……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F56)

    label("loc_BBD")

    Jump("loc_144B")

    label("loc_BC0")

    OP_8C(0x13, 270, 0)
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x103, -5560, 0, -1440, 0)
    SetChrPos(0x151, -4440, 0, -1480, 315)
    OP_6D(-5600, 0, 100, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x13, 0)
    Sleep(500)

    ChrTalk(    #12
        0x13,
        (
            "#841F#2P……哈哈，的确是呢……\x02\x03",

            "不，我已经和\x01",
            "卢格兰先生取得过联络了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #13
        0x13,
        (
            "#840F#2P啊，雪拉扎德。\x01",
            "正好。\x02",
        )
    )

    Jump("loc_CE7")

    label("loc_CE7")

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "\x07\x00#1643F咦…………？？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #15
        0x13,
        (
            "#840F#2P是雪拉扎德。\x02\x03",

            "……嗯，我让她来接听。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #16
        0x13,
        "#840F#2P是卡西乌斯先生打过来的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DB2():
        OP_8F(0xFE, 0xFFFFEA20, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DB2)
    Sleep(300)

    def lambda_DD2():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x64, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DD2)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)
    Sleep(300)

    ChrTalk(    #17
        0x103,
        (
            "#1640F#4P请、请问…………\x01",
            "……是卡西乌斯老师？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -6760, 0, -40, 0)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #18
        "\x07\x05哦，雪拉扎德。\x02",
    )

    Jump("loc_E82")

    label("loc_E82")

    CloseMessageWindow()

    AnonymousTalk(    #19
        (
            "\x07\x05我听说了。\x01",
            "你在王都很努力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #20
        0x103,
        (
            "#1640F#4P啊，是的。\x01",
            "谢谢您的赞赏！\x02\x03",

            "对了，老师是在洛连特吗？\x01",
            "我很快就要升为正……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #21
        (
            "\x07\x05不，其实我正在共和国，\x01",
            "要在这里待一段时间。\x01",
            "暂时回不去了。\x02",
        )
    )

    Jump("loc_F79")

    label("loc_F79")

    CloseMessageWindow()

    AnonymousTalk(    #22
        (
            "\x07\x05反正后面的事情\x01",
            "都拜托给了老练的家伙们，\x01",
            "不需要太过担心……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #23
        0x103,
        (
            "#1640F#4P………………………………\x02\x03",

            "#1645F………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #24
        (
            "\x07\x05雪拉扎德？\x01",
            "……听得到吗？\x02",
        )
    )

    Jump("loc_105C")

    label("loc_105C")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #25
        0x103,
        (
            "#1640F#4P啊，是。\x01",
            "…………没问题。\x02\x03",

            "#1641F老师您要是太专注于工作的话\x01",
            "艾丝蒂尔会生气的哦。\x02\x03",

            "如果不适时地抽身\x01",
            "回家看看的话……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #26
        "\x07\x05唔～是啊………\x02",
    )

    Jump("loc_112F")

    label("loc_112F")

    CloseMessageWindow()

    AnonymousTalk(    #27
        (
            "\x07\x05哦，对了。\x01",
            "还有一件事要拜托你帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #28
        0x103,
        (
            "#1643F#4P咦…………？\x02\x03",

            "#1640F让我帮忙……吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #29
        (
            "\x07\x05你要是回洛连特的话，\x01",
            "一定会大吃一惊的………\x02",
        )
    )

    Jump("loc_11F9")

    label("loc_11F9")

    CloseMessageWindow()

    AnonymousTalk(    #30
        (
            "\x07\x05我的工作还要花上不少时间。\x01",
            "帮我照顾一下孩子们。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #31
        0x103,
        "#1642F#4P？？　啊，好…………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("卡西乌斯")

    AnonymousTalk(    #32
        (
            "\x07\x05……啊，时间差不多了。\x01",
            "不好意思，能让克鲁茨接一下吗？\x02",
        )
    )

    Jump("loc_12C2")

    label("loc_12C2")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #33
        0x103,
        "#1643F#4P啊…………好。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x103, 0, 400)
    Sleep(200)

    def lambda_1309():
        OP_8F(0xFE, 0xFFFFEA48, 0x0, 0xFFFFFA60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1309)
    Sleep(300)

    def lambda_1329():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x64, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1329)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #34
        0x13,
        (
            "#840F#2P……嗯…………嗯……\x02\x03",

            "这个就交给我吧。\x01",
            "几天之内就可以处理好的。\x02\x03",

            "还有您送过来的资料……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_13E6():

        label("loc_13E6")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_13E6")

    QueueWorkItem2(0x151, 2, lambda_13E6)
    Sleep(1000)
    OP_63(0x103)
    OP_43(0x103, 0x3, 0x0, 0x8)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x151, 0x2)
    OP_43(0x151, 0x3, 0x0, 0x9)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2F55)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_144B")

    Jump("loc_1CF1")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1458")
    Jump("loc_1CF1")

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 1)), scpexpr(EXPR_END)), "loc_169B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 2)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14D3")

    ChrTalk(    #35
        0x13,
        (
            "#840F……雪拉扎德，\x01",
            "你不用做其它的任务了。\x02\x03",

            "集中精力做好现在的任务就行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1547")

    label("loc_14D3")


    ChrTalk(    #36
        0x13,
        (
            "#840F雪拉扎德，\x01",
            "这个任务完成了就来汇报吧。\x02\x03",

            "在此之前不用做其它的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        "#1645F好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1547")

    Jump("loc_1698")

    label("loc_154A")

    OP_8C(0x13, 90, 0)

    ChrTalk(    #38
        0x151,
        (
            "#1653F啊，不过……\x02\x03",

            "所谓『通缉魔兽』应该是\x01",
            "克鲁茨前辈自己通缉的吧？\x02\x03",

            "#1650F我觉得既然是\x01",
            "自己亲手打倒的，\x01",
            "贴通缉告示就没有什么意义了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x151, 500)
    Sleep(300)

    ChrTalk(    #39
        0x13,
        (
            "#845F哎、哎呀……\x01",
            "规定是这样写的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#1645F……我说，这太顽固了吧？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F52)

    label("loc_1698")

    Jump("loc_1CF1")

    label("loc_169B")

    OP_8C(0x13, 90, 0)

    ChrTalk(    #41
        0x151,
        (
            "#1650F那个，\x01",
            "刚才非常感谢您。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x151, 500)
    Sleep(300)

    ChrTalk(    #42
        0x13,
        (
            "#840F不，我应该为\x01",
            "擅离接待岗位表示道歉。\x02\x03",

            "请原谅我现在才自我介绍……\x01",
            "我是王都支部的负责人\x01",
            "克鲁茨·纳尔当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x151,
        (
            "#1650F谢谢您这么有责任心。\x02\x03",

            "#1651F呵呵，我叫爱娜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x103,
        (
            "#1645F啊，到此为止。\x01",
            "你的自我介绍太长了。\x02\x03",

            "#1640F对了，前辈……\x01",
            "请给我地下水路的钥匙。\x02\x03",

            "西街区的地下水路\x01",
            "不是出现了通缉魔兽吗。\x02\x03",

            "我马上去把它们解决……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #45
        0x13,
        (
            "#843F……你所接受的任务\x01",
            "不是为她带路吗？\x02\x03",

            "我好像说过\x01",
            "你不用接受别的任务吧……？\x02\x03",

            "#840F难道说你打算带着普通人\x01",
            "去剿灭通缉魔兽吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#1642F唔……\x02\x03",

            "#1645F这、这个嘛……\x01",
            "完成这个任务之后\x01",
            "回来的路上顺便就可以去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x13,
        (
            "#843F………………………………\x02\x03",

            "#843F雪拉扎德，\x01",
            "我再三说明过……\x02\x03",

            "对游击士的评价\x01",
            "并不是根据战斗能力来的。\x02\x03",

            "#842F无论有多强，\x01",
            "只要不能帮助他人，就没有任何意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        "#1646F哼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "#843F…………雪拉扎德，\x01",
            "这么说可能有点啰嗦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#1645F啊，好的好的。\x01",
            "我明白了。\x02\x03",

            "只是单纯变得更厉害\x01",
            "是没有意义的对吧。\x02\x03",

            "……就算你再怎么说，\x01",
            "明明自己就是个十足的厉害人物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x151,
        "#1653F哎，是这样吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #52
        0x103,
        (
            "#1645F是呀。\x02\x03",

            "上次我亲眼看到，\x01",
            "只靠擦身而过的一击\x01",
            "就把通缉魔兽给干掉了。\x02\x03",

            "而且行走的速度\x01",
            "居然完全没什么变化。\x02\x03",

            "在近处看还真是心惊胆战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x13,
        (
            "#843F…………啊，是说那次吗。\x02\x03",

            "#840F雪拉扎德，\x01",
            "那是因为之后我和人有约会。\x01",
            "所以才那么着急。\x02\x03",

            "如果时间充裕的话，\x01",
            "我一定会严格按照兵法展开战术的。\x02\x03",

            "就算对手是通缉魔兽，\x01",
            "也不能轻易偷工减料啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        "#1645F（…………老顽固……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F51)

    label("loc_1CF1")

    TalkEnd(0x13)
    Return()

    # Function_7_9A9 end

    def Function_8_1CF5(): pass

    label("Function_8_1CF5")

    OP_8C(0x103, 180, 400)

    def lambda_1D02():
        OP_8E(0xFE, 0xFFFFE9E4, 0x0, 0xFFFFF5C4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D02)
    WaitChrThread(0x103, 0x1)

    def lambda_1D22():
        OP_8E(0xFE, 0xFFFFED7C, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D22)
    WaitChrThread(0x103, 0x1)

    def lambda_1D42():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D42)
    WaitChrThread(0x103, 0x1)

    def lambda_1D62():
        OP_8E(0xFE, 0xFFFFFD58, 0xFFFFFE0C, 0xFFFFE3B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D62)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_8_1CF5 end

    def Function_9_1D7D(): pass

    label("Function_9_1D7D")


    def lambda_1D83():
        OP_8E(0xFE, 0xFFFFEEA8, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1D83)
    WaitChrThread(0x151, 0x1)

    def lambda_1DA3():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1DA3)
    WaitChrThread(0x151, 0x1)

    def lambda_1DC3():
        OP_8E(0xFE, 0xFFFFFD58, 0xFFFFFE0C, 0xFFFFE3B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1DC3)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_9_1D7D end

    def Function_10_1DDE(): pass

    label("Function_10_1DDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1DEB")
    Jump("loc_1FF6")

    label("loc_1DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E51")

    ChrTalk(    #55
        0xFE,
        (
            "从今天开始，\x01",
            "这里就是钓公师团的总部了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "…………这名字听起来真是响亮。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EFE")

    label("loc_1E51")


    ChrTalk(    #57
        0xFE,
        (
            "王都格兰赛尔……\x01",
            "作为我们钓公师团的总部\x01",
            "真是再适合不过的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "既可以在码头垂钓，\x01",
            "也可以从飞艇坪出发\x01",
            "到利贝尔各地去钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "…………这正是我的愿望。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1EFE")

    Jump("loc_1FF6")

    label("loc_1F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1F0B")
    Jump("loc_1FF6")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F67")

    ChrTalk(    #60
        0xFE,
        (
            "虽然本人之前\x01",
            "一直住在王都郊外……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "但从今天开始就住在这里了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FF6")

    label("loc_1F67")


    ChrTalk(    #62
        0xFE,
        (
            "我们钓公师团\x01",
            "终于实现了进军王都的梦想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "虽然本人把\x01",
            "自己的房子都卖掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "不过不要紧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "从今天开始就住在这里了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1FF6")

    TalkEnd(0xFE)
    Return()

    # Function_10_1DDE end

    def Function_11_1FFA(): pass

    label("Function_11_1FFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2007")
    Jump("loc_21E8")

    label("loc_2007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_20E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2072")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #66
        0xFE,
        (
            "嗯，那些事项\x01",
            "就由团长进行详细的说明……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "虽然只是一些常识性的问题……\x02",
    )

    CloseMessageWindow()
    Jump("loc_20E3")

    label("loc_2072")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #68
        0xFE,
        "请问客人是希望入团吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "嗯，非常欢迎！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "只需要接受一个\x01",
            "很简单的入团测试就可以了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_20E3")

    Jump("loc_21E8")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_20F0")
    Jump("loc_21E8")

    label("loc_20F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_21E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2160")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #71
        0xFE,
        (
            "要赶快把搬家搞定，\x01",
            "去打探一下情况才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "不、不能着急。\x01",
            "鱼竿要轻搬轻放……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E8")

    label("loc_2160")


    ChrTalk(    #73
        0xFE,
        "你们知道吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "最近，瓦雷利亚湖的鱼王\x01",
            "似乎把格兰赛尔附近\x01",
            "当成了饵场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "要、要赶快把搬家搞定，\x01",
            "去打探一下情况才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_21E8")

    TalkEnd(0xFE)
    Return()

    # Function_11_1FFA end

    def Function_12_21EC(): pass

    label("Function_12_21EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_21F9")
    Jump("loc_23A2")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_229A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_223A")

    ChrTalk(    #76
        0xFE,
        "钓公……师团？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "真是一群奇怪的人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_223A")


    ChrTalk(    #78
        0xFE,
        (
            "搬运的东西全都是渔具，\x01",
            "这样的工作还是第一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "总觉得和普通的\x01",
            "行李不一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2297")

    Jump("loc_23A2")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_22A4")
    Jump("loc_23A2")

    label("loc_22A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_23A2")
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2355")
    OP_4A(0x16, 255)
    TurnDirection(0x16, 0xFE, 500)
    Sleep(300)

    ChrTalk(    #80
        0x16,
        "啊啊，我说你！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x16,
        (
            "那个很容易折断，\x01",
            "给我小心一点！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x16, 500)
    Sleep(300)

    ChrTalk(    #82
        0xFE,
        "啊！？\x02",
    )

    Jump("loc_2328")

    label("loc_2328")

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "好、好的，我会小心的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 270, 500)
    OP_4B(0x16, 255)
    Jump("loc_23A2")

    label("loc_2355")


    ChrTalk(    #84
        0xFE,
        (
            "这个，\x01",
            "放在这里可以吗？\x02",
        )
    )

    Jump("loc_237C")

    label("loc_237C")

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "哎……这个是什么什么竿呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_23A2")

    TalkEnd(0xFE)
    Return()

    # Function_12_21EC end

    def Function_13_23A6(): pass

    label("Function_13_23A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_23B3")
    Jump("loc_246C")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_245B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_240F")

    ChrTalk(    #86
        0xFE,
        "我有一个疑问……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "钓公师团里面，\x01",
            "会不会有规定之类的条款呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2458")

    label("loc_240F")


    ChrTalk(    #88
        0xFE,
        "嗯，虽然我想入团……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "可是，我这样的水平也可以加入吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2458")

    Jump("loc_246C")

    label("loc_245B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2465")
    Jump("loc_246C")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_246C")

    label("loc_246C")

    TalkEnd(0xFE)
    Return()

    # Function_13_23A6 end

    def Function_14_2470(): pass

    label("Function_14_2470")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -4600, 0, 560, 90)
    SetChrPos(0x11, -2320, 0, 450, 270)
    OP_6D(4390, -250, 910, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(328, 0)
    Sleep(500)

    def lambda_2504():
        OP_6D(-4830, -250, 1680, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2504)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(-5060, 0, 2040, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #90
        0x10,
        (
            "#760F#5P――是吗。\x02\x03",

            "金先生果然还是要回共和国……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#070F是啊，之前的任务\x01",
            "一直都是让同伴处理的。\x02\x03",

            "可毕竟Ａ级游击士\x01",
            "肩负着很大的社会责任嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10,
        (
            "#760F#5P呼，原来如此……\x02\x03",

            "虽然希望您能留下来，\x01",
            "但既然这样我也不能强行挽留。\x02\x03",

            "――那么，打算什么时候出发呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#070F本来打算立刻出发的，\x01",
            "但是突然有些事情要办。\x02\x03",

            "大使馆的爱尔莎大使\x01",
            "邀请我去做个小小的旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10,
        (
            "#760F#5P爱尔莎大使？\x02\x03",

            "她找金先生\x01",
            "会有什么事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x11,
        (
            "#070F不，\x01",
            "其实是找雾香有事。\x02\x03",

            "总而言之，\x01",
            "我就是个作陪的。\x02",
        )
    )

    Jump("loc_277D")

    label("loc_277D")

    CloseMessageWindow()

    ChrTalk(    #96
        0x10,
        (
            "#760F#5P唔，这么一说，\x01",
            "我就更不明白了……\x02\x03",

            "不管怎样，祝您旅途愉快。\x02\x03",

            "就把这次旅行当作是\x01",
            "回国之前的纪念吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        (
            "#070F哈哈，谢谢了。\x02\x03",

            "我也打算\x01",
            "好好享受一下呢。\x02",
        )
    )

    Jump("loc_2846")

    label("loc_2846")

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2470 end

    def Function_15_286E(): pass

    label("Function_15_286E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -4600, 0, 560, 90)
    SetChrPos(0x11, -2320, 0, 450, 270)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(4390, -250, 910, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_1D(0xE)
    Sleep(500)

    def lambda_290A():
        OP_6D(-4830, -250, 1680, 3500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_290A)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    Fade(1000)
    OP_6D(-5060, 0, 2040, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0x10,
        (
            "#764F#5P――是吗。\x02\x03",

            "#760F您马上就要回\x01",
            "卡尔瓦德共和国了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x11,
        (
            "#573F#12P是啊，之前的任务\x01",
            "一直都是让同伴处理的。\x02\x03",

            "#070F可毕竟Ａ级游击士\x01",
            "肩负着很大的社会责任嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#764F#5P呼，原来如此……\x02\x03",

            "虽然希望您能留下来，\x01",
            "但既然这样我也不能强行挽留。\x02\x03",

            "#760F那么，打算什么时候出发呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#074F#12P唔，依照现在的情况\x01",
            "我必须尽早回去才行。\x02\x03",

            "#070F如果可以的话，\x01",
            "我是打算明天就出发的……\x02\x03",

            "你能帮我准备一张\x01",
            "前往共和国的船票吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10,
        (
            "#763F#5P嗯，\x01",
            "那倒是没什么问题……\x02\x03",

            "#760F不过，\x01",
            "您不去和雾香打个招呼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        (
            "#075F#12P哎呀，\x01",
            "我倒是有这样的打算……\x02\x03",

            "可是却被她本人\x01",
            "教训了一番。\x02\x03",

            "#072F说什么『与其这么闲着\x01",
            "还不如早点回国』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "#761F#5P哈哈……是这样啊。\x02\x03",

            "#760F那还真是无可奈何啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#573F#12P唉……算了。\x02\x03",

            "#070F反正也不是\x01",
            "以后再也见不到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "#760F#5P嗯，说的也是。\x02\x03",

            "#761F而且，\x01",
            "你们两人的缘分\x01",
            "就算藕断也会丝连啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        (
            "#071F#12P哈哈，\x01",
            "可以说是不是冤家不聚头吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "#761F#5P呵呵……\x02\x03",

            "#760F好了，虽然很惋惜，\x01",
            "但也不能一直这么聊下去。\x02\x03",

            "我马上为您\x01",
            "去准备定期船票。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(800)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x10,
        (
            "#763F#5P哦，通讯器响了。\x01",
            "……失陪一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 400)

    def lambda_2EB4():
        OP_6D(-5400, 0, 1800, 1200)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2EB4)
    OP_8E(0x10, 0xFFFFEA20, 0x0, 0x0, 0x5DC, 0x0)
    OP_8C(0x10, 270, 400)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_23(0xC3)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #110
        0x10,
        (
            "#760F#11P您好，这里是\x01",
            "游击士协会格兰赛尔支部。\x02\x03",

            "#764F……哦，好的。\x02\x03",

            "#763F……好。\x02\x03",

            "#760F嗯，\x01",
            "他正好在这里……\x02",
        )
    )

    Jump("loc_2FD4")

    label("loc_2FD4")

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2FF2():
        OP_6D(-5060, 0, 2040, 1000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2FF2)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #111
        0x10,
        "#760F#5P金先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        "#073F#12P嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10,
        (
            "#760F#5P是共和国大使馆\x01",
            "爱尔莎大使打来的。\x02\x03",

            "#761F她说无论如何\x01",
            "也想邀请您去温泉旅行……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)

    ChrTalk(    #114
        0x11,
        "#073F#11P#4S啊！？\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_3114():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3114)
    FadeToDark(2000, 0, -1)

    def lambda_312E():

        label("loc_312E")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_312E")

    QueueWorkItem2(0x10, 2, lambda_312E)
    OP_43(0x11, 0x3, 0x0, 0x10)
    Sleep(500)

    def lambda_314B():
        OP_8F(0xFE, 0xFFFFEA20, 0x0, 0x4D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_314B)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_286E end

    def Function_16_3174(): pass

    label("Function_16_3174")

    OP_8C(0x11, 180, 500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_318B():
        OP_8E(0xFE, 0xFFFFF6F0, 0x0, 0xFFFFF3E4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_318B)
    WaitChrThread(0x11, 0x1)

    def lambda_31AB():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0xFFFFF3E4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31AB)
    WaitChrThread(0x11, 0x1)

    def lambda_31CB():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31CB)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 270, 500)
    Return()

    # Function_16_3174 end

    def Function_17_31F7(): pass

    label("Function_17_31F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #115 op#5
        "\x07\x00#150W七耀历１１９７年　王都格兰赛尔#20W――\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x00百日战役５年后。\x01",
            "１１９７年的利贝尔王国，\x01",
            "战争的伤痕逐渐愈合，到处重现生机。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #117
        (
            "\x07\x00人们再次聚集在复兴的城市，\x01",
            "重开的导力器贸易为王国带来了繁荣。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x00――和平年代终于到来。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #119
        (
            "\x07\x00但与此同时，\x01",
            "也是军队开始逐渐腐败的时期。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #120
        (
            "\x07\x00金钱、地位、名誉…………\x01",
            "许多军官都忙于中饱私囊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #121
        (
            "\x07\x00随着导力器的发达，在喧嚣之中\x01",
            "很多事情被人们忘却了――#40W……#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(0, 2000, 0, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, -8300, 0, -3300, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -500, -7700, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)

    def lambda_3460():
        OP_6D(0, 0, 0, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3460)
    WaitChrThread(0x19, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    def lambda_3487():
        OP_6D(0, 0, -2340, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3487)

    def lambda_349F():
        OP_6B(3060, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_349F)

    def lambda_34AF():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_34AF)

    def lambda_34CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_34CA)
    WaitChrThread(0x12, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #122
        0x12,
        "女性",
        "#1653F…………哎呀？\x02",
    )

    Jump("loc_3510")

    label("loc_3510")

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)
    Sleep(800)
    OP_8C(0x12, 315, 400)
    Sleep(800)
    OP_8C(0x12, 0, 400)
    Sleep(500)

    NpcTalk(    #123
        0x12,
        "女性",
        "#1653F没有人呢……\x02",
    )

    Jump("loc_355E")

    label("loc_355E")

    CloseMessageWindow()

    def lambda_3565():
        OP_6D(0, 0, -400, 1600)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3565)

    def lambda_357D():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF614, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_357D)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    OP_8C(0x12, 315, 400)
    Sleep(200)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_35C5():
        OP_6D(-1380, 0, 1300, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_35C5)

    def lambda_35DD():
        OP_8E(0xFE, 0xFFFFF6B4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_35DD)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #124
        (
            "\x07\x05尊敬的委托人，请将委托内容写在您右手边的纸上，\x01",
            "并置于纸箱之中。\x01",
            "　　　　――游击士协会　王都格兰赛尔支部\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_8C(0x12, 90, 400)
    Sleep(300)

    def lambda_36CE():
        OP_6D(3280, 0, 1600, 5000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_36CE)

    def lambda_36E6():
        OP_8E(0xFE, 0x76C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_36E6)
    WaitChrThread(0x12, 0x1)

    def lambda_3706():
        OP_8E(0xFE, 0x116C, 0x0, 0xEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3706)
    WaitChrThread(0x12, 0x1)

    def lambda_3726():
        OP_8E(0xFE, 0x17AC, 0x0, 0xEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3726)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 500)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    def lambda_3771():
        OP_8E(0xFE, 0xD20, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3771)
    WaitChrThread(0x12, 0x1)

    def lambda_3791():
        OP_8E(0xFE, 0x744, 0xFA, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3791)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    def lambda_37D5():
        OP_8F(0xFE, 0xD20, 0x0, 0x12C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_37D5)
    WaitChrThread(0x12, 0x1)

    def lambda_37F5():
        OP_6D(-300, 0, 300, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_37F5)

    def lambda_380D():
        OP_8E(0xFE, 0xD20, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_380D)
    WaitChrThread(0x12, 0x1)

    def lambda_382D():
        OP_8E(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_382D)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 500)
    Sleep(300)

    NpcTalk(    #125
        0x12,
        "女性",
        "#1654F（这里面连人影都没有。）\x02",
    )

    Jump("loc_3888")

    label("loc_3888")

    CloseMessageWindow()
    OP_8C(0x12, 270, 500)
    Sleep(300)

    NpcTalk(    #126
        0x12,
        "女性",
        (
            "#1652F（……不过有通讯器。\x01",
            "  我就先借来用用……）\x02",
        )
    )

    Jump("loc_38DD")

    label("loc_38DD")

    CloseMessageWindow()
    SetChrPos(0x103, 0, -500, -7700, 0)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3900():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3900)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_392A():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_392A)

    def lambda_3938():
        OP_6D(0, 500, -1920, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3938)

    def lambda_3950():
        OP_6B(3160, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3950)

    def lambda_3960():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3960)
    Sleep(1500)

    def lambda_397D():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_397D)

    def lambda_3998():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3998)
    WaitChrThread(0x103, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #127
        0x103,
        (
            "#1645F呼…………好累啊……\x02\x03",

            "为什么我要做这种杂事……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x12, 500)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #128
        0x103,
        (
            "#1643F哎呀，是客人吗？\x01",
            "有什么委托吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A56():
        OP_6D(-1280, 0, -780, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3A56)

    def lambda_3A6E():
        OP_6B(3240, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3A6E)

    def lambda_3A7E():
        OP_67(0, 4840, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3A7E)

    def lambda_3A96():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A96)
    Sleep(400)
    OP_8C(0x12, 135, 500)

    def lambda_3ABD():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFFBF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3ABD)
    WaitChrThread(0x103, 0x1)

    def lambda_3ADD():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3ADD)
    WaitChrThread(0x12, 0x1)

    def lambda_3AF0():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3AF0)
    Sleep(300)

    NpcTalk(    #129
        0x12,
        "女性",
        (
            "#1650F#2P嗯，\x01",
            "我有件事想委托协会……\x02\x03",

            "哎，您是……？\x02",
        )
    )

    Jump("loc_3B4F")

    label("loc_3B4F")

    CloseMessageWindow()

    ChrTalk(    #130
        0x103,
        (
            "#1640F我叫雪拉扎德·哈维。\x01",
            "…………是游击士。\x02\x03",

            "虽然还只是准游击士，\x01",
            "不过你可以对我的实力放心。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #131
        0x12,
        "女性",
        (
            "#1653F#2P啊，您就是游击士啊？\x02\x03",

            "#1651F呵呵，真抱歉。\x01",
            "因为看您这么年轻，所以……\x02\x03",

            "我叫爱娜。\x01",
            "请多关照，雪拉扎德小姐。\x02",
        )
    )

    Jump("loc_3C5A")

    label("loc_3C5A")

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        (
            "#1640F嗯，不用打招呼了。\x01",
            "快点告诉我委托内容吧。\x02\x03",

            "今天王都支部这里\x01",
            "只有两个游击士。\x02\x03",

            "#1640F所以工作非常忙，\x01",
            "请你长话短说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x12,
        (
            "#1653F#2P哎呀，是这样吗。\x02\x03",

            "对不起。\x01",
            "我总是……\x02",
        )
    )

    Jump("loc_3D3C")

    label("loc_3D3C")

    CloseMessageWindow()

    ChrTalk(    #134
        0x103,
        (
            "#1645F…………我刚才说了。\x02\x03",

            "请你长话短说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x12,
        (
            "#1651F#2P啊，对了。\x02\x03",

            "#1650F实际上我……\x01",
            "是第一次来王都。\x02\x03",

            "所以想来找一位\x01",
            "可以为我带路\x01",
            "参观王都的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        "#1642F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#1651F#2P呵呵，王都不是很大吗？\x01",
            "看起来很容易迷路。\x02\x03",

            "我想如果要是游击士的话\x01",
            "应该对城里的道路很清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#1645F呼～………………\x02\x03",

            "这样的事情\x01",
            "我不想接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x12,
        "#1653F#2P咦…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        (
            "#1646F我想你是搞错了。\x02\x03",

            "游击士既不是志愿者\x01",
            "也不是随叫随到的钟点工。\x02\x03",

            "#1642F我们这边也很忙，\x01",
            "请不要提出这样无意义的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x12,
        (
            "#1650F#2P这、这个……\x01",
            "我本来也不打算这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x103,
        (
            "#1645F要想参观的话\x01",
            "自己到处逛逛就行了。\x02\x03",

            "#1645F（真是的，\x01",
            "  不谙世事的大小姐……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_403E():

        label("loc_403E")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_403E")

    QueueWorkItem2(0x12, 3, lambda_403E)

    def lambda_404F():
        OP_8E(0xFE, 0xCBC, 0x0, 0xFFFFFEAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_404F)
    WaitChrThread(0x103, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0x103, 90, 500)
    Sleep(400)

    ChrTalk(    #143
        0x103,
        (
            "#1646F#3P我呀，要做一些重要的任务，\x01",
            "然后在自己的正游击士推荐信上\x01",
            "添上光辉的一笔。\x02\x03",

            "下次来的时候，\x01",
            "请带来一些正经的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12,
        (
            "#1656F#5P（嗯…………………………\x01",
            "  ……没办法了……）\x02\x03",

            "对不起，在您正忙的时候打扰了……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x13)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 200, -500, -7700, 0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x13, 255)

    def lambda_41AD():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_41AD)

    def lambda_41BB():
        OP_8E(0xFE, 0xC8, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_41BB)

    def lambda_41D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_41D6)
    WaitChrThread(0x13, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #145
        0x13,
        (
            "#840F哦，是委托人吗？\x02\x03",

            "抱歉，\x01",
            "现在接待员的工作是由我兼任的……\x02",
        )
    )

    Jump("loc_4262")

    label("loc_4262")

    CloseMessageWindow()

    def lambda_4269():
        OP_8E(0xFE, 0xC8, 0x0, 0xFFFFF3E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4269)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x12, 500)
    Sleep(300)

    ChrTalk(    #146
        0x12,
        "#1653F#2P啊，不……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #147
        0x103,
        (
            "#1646F#3P前辈，\x01",
            "不要管她。\x02\x03",

            "#1642F她把游击士当成是\x01",
            "用钱就可以雇来的钟点工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x12,
        (
            "#1655F#2P……对不起，\x01",
            "我告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4348():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFF06, 0xFFFFEB4C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4348)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13)

    ChrTalk(    #149 op#A op#5
        0x13,
        "#843F#13A#5P…………唔。\x05\x02",
    )

    Sleep(500)

    ChrTalk(    #150
        0x13,
        "#843F#5P请稍等片刻好吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x12, 0x13, 400)
    Sleep(500)
    OP_44(0x103, 0x3)

    def lambda_43FD():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFFD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43FD)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #151
        0x13,
        "#840F#5P雪拉扎德。\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x103, 0x13, 500)
    Sleep(300)

    ChrTalk(    #152
        0x103,
        (
            "#1643F咦……？\x02\x03",

            "前、前辈，什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x13,
        (
            "#840F#5P请接受\x01",
            "她的委托。\x02\x03",

            "帮助有困难的人\x01",
            "也是游击士的任务。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44F6():
        OP_8F(0xFE, 0x834, 0x0, 0xFFFFFB50, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44F6)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #154
        0x103,
        (
            "#1642F啊………………可、可是，\x01",
            "我现在很忙啊！？\x02\x03",

            "没有空陪她去\x01",
            "参观王都什么的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x13,
        (
            "#843F#5P你现在不用接受其它的任务。\x01",
            "交给我来处理就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#1644F这、这怎么行……！\x01",
            "前辈您还要兼任接待员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x13,
        (
            "#842F#5P你不是准游击士吗？\x01",
            "现在还只是向前辈学习的身份。\x02\x03",

            "#843F……去吧。\x02\x03",

            "完成了这个任务，\x01",
            "我就给你写推荐信。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #158
        0x103,
        (
            "#1643F哎……正游击士的推荐信？\x02\x03",

            "可、可是，这么简单的任务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x13,
        (
            "#840F#5P『无论什么任务都不会置之不管』。\x01",
            "这不是你的信念吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        "#1645F是、是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x13,
        "#840F#5P那就拜托了。\x02",
    )

    CloseMessageWindow()

    def lambda_477C():

        label("loc_477C")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_477C")

    QueueWorkItem2(0x12, 3, lambda_477C)

    def lambda_478D():

        label("loc_478D")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_478D")

    QueueWorkItem2(0x103, 3, lambda_478D)
    OP_8C(0x13, 315, 500)

    def lambda_47A5():
        OP_8E(0xFE, 0xFFFFF768, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_47A5)
    WaitChrThread(0x13, 0x1)
    OP_44(0x103, 0x3)
    OP_44(0x12, 0x3)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #162
        0x12,
        "#1650F那、那个，谢谢您。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)
    Sleep(300)

    ChrTalk(    #163
        0x13,
        (
            "#840F#2P…………不用……\x02\x03",

            "你们两个要注意安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        "#1645F……好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        "#1650F请多多指教。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 500)
    Sleep(300)

    def lambda_4894():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFF06, 0xFFFFE91C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4894)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_43(0x103, 0x3, 0x0, 0x12)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_48CA():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_48CA)

    def lambda_48E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_48E5)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    WaitChrThread(0x103, 0x3)
    Sleep(1500)

    def lambda_490B():
        OP_6D(-2400, 200, 60, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_490B)

    def lambda_4923():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4923)
    OP_8C(0x13, 270, 400)
    Sleep(3000)

    ChrTalk(    #166
        0x13,
        (
            "#843F#6P……也好，\x01",
            "算是给她一个好的学习机会吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_497B():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_497B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_17_31F7 end

    def Function_18_499D(): pass

    label("Function_18_499D")

    OP_8C(0x103, 225, 500)
    Sleep(300)

    def lambda_49AF():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49AF)
    WaitChrThread(0x103, 0x1)

    def lambda_49CF():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEBEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49CF)
    WaitChrThread(0x103, 0x1)

    def lambda_49EF():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFE91C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49EF)
    WaitChrThread(0x103, 0x1)

    def lambda_4A0F():
        OP_8E(0xFE, 0x0, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A0F)

    def lambda_4A2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A2A)
    WaitChrThread(0x103, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_18_499D end

    def Function_19_4A41(): pass

    label("Function_19_4A41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4ABC")
    Sleep(2000)

    def lambda_4A55():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFC54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A55)
    WaitChrThread(0x103, 0x1)
    Sleep(2500)

    def lambda_4A7A():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFEAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A7A)
    WaitChrThread(0x103, 0x1)
    Sleep(2500)

    def lambda_4A9F():
        OP_8F(0xFE, 0xCBC, 0x0, 0x104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A9F)
    WaitChrThread(0x103, 0x1)
    Jump("Function_19_4A41")

    label("loc_4ABC")

    Return()

    # Function_19_4A41 end

    SaveToFile()

Try(main)
