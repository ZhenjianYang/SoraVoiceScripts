from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4139   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4139.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4139_1 ._SN',
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
        '爱尔莎大使',                           # 9
        '约克姆派驻官',                         # 10
        '法拉',                                 # 11
        '贝尼乔参事官',                         # 12
        '珊蒂',                                 # 13
        '莉卡妲夫人',                           # 14
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
        'ED6_DT27/CH03723 ._CH',             # 00
        'ED6_DT07/CH01490 ._CH',             # 01
        'ED6_DT07/CH01180 ._CH',             # 02
        'ED6_DT07/CH01680 ._CH',             # 03
        'ED6_DT07/CH02540 ._CH',             # 04
        'ED6_DT07/CH01230 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03723P._CP',             # 00
        'ED6_DT07/CH01490P._CP',             # 01
        'ED6_DT07/CH01180P._CP',             # 02
        'ED6_DT07/CH01680P._CP',             # 03
        'ED6_DT07/CH02540P._CP',             # 04
        'ED6_DT07/CH01230P._CP',             # 05
    )

    DeclNpc(
        X                   = 55000,
        Z                   = 200,
        Y                   = 65540,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -54910,
        Z                   = 0,
        Y                   = 61420,
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -51570,
        Z                   = 0,
        Y                   = -44740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55260,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -6760,
        Z                   = 0,
        Y                   = 7960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -52030,
        Z                   = 0,
        Y                   = 58230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 1030,
        TriggerZ            = 6000,
        TriggerY            = 33170,
        TriggerRange        = 800,
        ActorX              = 1030,
        ActorZ              = 6500,
        ActorY              = 33170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1030,
        TriggerZ            = 6000,
        TriggerY            = 33170,
        TriggerRange        = 800,
        ActorX              = 1030,
        ActorZ              = 6500,
        ActorY              = 33170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -46570,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -46470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -44950,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -44700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -43230,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -42960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_2C5",          # 01, 1
        "Function_2_33B",          # 02, 2
        "Function_3_4B8",          # 03, 3
        "Function_4_4DC",          # 04, 4
        "Function_5_D1D",          # 05, 5
        "Function_6_1107",         # 06, 6
        "Function_7_15A3",         # 07, 7
        "Function_8_1BF9",         # 08, 8
        "Function_9_1F9B",         # 09, 9
        "Function_10_20B4",        # 0A, 10
        "Function_11_22F3",        # 0B, 11
        "Function_12_2463",        # 0C, 12
        "Function_13_34CE",        # 0D, 13
        "Function_14_350C",        # 0E, 14
        "Function_15_354A",        # 0F, 15
        "Function_16_3588",        # 10, 16
        "Function_17_35C6",        # 11, 17
        "Function_18_35FA",        # 12, 18
        "Function_19_3779",        # 13, 19
        "Function_20_391D",        # 14, 20
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xD, 0x80)

    label("loc_266")

    Jump("loc_2A4")

    label("loc_269")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_289")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_2A4")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_293")
    Jump("loc_2A4")

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_29D")
    Jump("loc_2A4")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2A4")

    label("loc_2A4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2C4"),
    )


    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_2C1")

    Jump("loc_2C4")

    label("loc_2C4")

    Return()

    # Function_0_24E end

    def Function_1_2C5(): pass

    label("Function_1_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1")
    OP_B1("t4139_y")
    Jump("loc_2EA")

    label("loc_2E1")

    OP_B1("t4139_n")

    label("loc_2EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_309")
    OP_64(0x0, 0x1)
    OP_72(0x2, 0x10)
    Jump("loc_32A")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")
    OP_64(0x1, 0x1)
    OP_72(0x2, 0x10)
    Jump("loc_32A")

    label("loc_31D")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_71(0x2, 0x10)

    label("loc_32A")

    Jump("loc_33A")

    label("loc_32D")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_71(0x2, 0x10)

    label("loc_33A")

    Return()

    # Function_1_2C5 end

    def Function_2_33B(): pass

    label("Function_2_33B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A2")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4A2")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4A2")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4A2")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4A2")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4A2")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4A2")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4A2")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4A2")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4A2")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4A2")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4A2")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4A2")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A2")

    label("loc_4B7")

    Return()

    # Function_2_33B end

    def Function_3_4B8(): pass

    label("Function_3_4B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_8D(0xFE, -59290, 60000, -52170, 63360, 2000)
    Jump("Function_3_4B8")

    label("loc_4DB")

    Return()

    # Function_3_4B8 end

    def Function_4_4DC(): pass

    label("Function_4_4DC")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_501")
    SetChrSubChip(0x8, 1)
    Jump("loc_506")

    label("loc_501")

    SetChrSubChip(0x8, 2)

    label("loc_506")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 5)), scpexpr(EXPR_END)), "loc_58F")

    ChrTalk(    #0
        0x8,
        (
            "#1113F这样的话我们\x01",
            "在黑暗中行动绝非上策。\x02\x03",

            "#1110F虽然有不安，应该\x01",
            "整理情绪做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_881")

    label("loc_58F")


    ChrTalk(    #1
        0x101,
        "#1000F爱尔莎大使，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#1110F艾丝蒂尔……来得正好。\x02\x03",

            "#1112F我就单刀直入地问了，\x01",
            "有没有关于这个现象的情报？\x02\x03",

            "看到王国军\x01",
            "正式出动了，\x01",
            "是不是预测到什么事态了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1013F（呜，好敏锐……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#1113F…………………………\x02\x03",

            "呼，看来我\x01",
            "也是相当着急了。\x02\x03",

            "#1110F看来利贝尔\x01",
            "已经察觉有情况了。\x02\x03",

            "你即使知道什么\x01",
            "应该也不会\x01",
            "全盘告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1016F嗯……对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#1111F别介意。\x02\x03",

            "#1110F站在你的立场上想想，\x01",
            "我也没什么理由抱怨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1000F爱尔莎大使……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#1112F我就问一件事吧。\x02\x03",

            "我们就这样\x01",
            "等着没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1011F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1040F（就是说这事态就交给\x01",
            "　游击士协会……交给我们\x01",
            "　是吗。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1006F啊……是、是！\x02\x03",

            "现在，游击士协会和王国军\x01",
            "正在尽全力搜查。\x02\x03",

            "一定会解决这个现象，\x01",
            "将一切都恢复原状的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#1111F呵呵，那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DD)

    label("loc_881")

    Jump("loc_D14")

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_89A")
    Jump("loc_D14")

    label("loc_89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_C05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 6)), scpexpr(EXPR_END)), "loc_8F5")

    ChrTalk(    #13
        0x8,
        (
            "#1110F人一旦结缘\x01",
            "就有可能获得强大的力量。\x02\x03",

            "难得相识\x01",
            "希望珍惜这缘分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C02")

    label("loc_8F5")


    ChrTalk(    #14
        0x8,
        (
            "#1110F各位游击士……咦？\x02\x03",

            "#1111F……今日带着\x01",
            "好可爱的小姑娘啊。\x02\x03",

            "难道就是昨天说的\x01",
            "克洛斯贝尔的小姑娘？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1011F啊，不是……\x01",
            "不是这孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        (
            "#064F嗯、嗯……\x02\x03",

            "#060F初次见面。\x01",
            "我是提妲·拉赛尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1112F……拉赛尔？\x02\x03",

            "难道是那个有名的\x01",
            "拉赛尔博士的亲戚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#067F啊，是。拉赛尔博士\x01",
            "是我的爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1113F是听说他有女儿夫妇，\x01",
            "原来是孙女啊……\x02\x03",

            "#1111F呵呵，艾丝蒂尔也是，\x01",
            "能遇上各种缘分真令人高兴啊。\x02\x03",

            "在卡尔瓦德，\x01",
            "有『萍水相逢也是缘』\x01",
            "这句俗话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x108,
        (
            "#070F与素不相识的人\x01",
            "拂袖而过也是种缘分……\x02\x03",

            "记得是东方传来的话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1110F嗯嗯，能和提妲\x01",
            "相遇也是缘分啊。\x02\x03",

            "不仅如此……\x02\x03",

            "诸位能这样来到这里，\x01",
            "或许也有重要的意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1018F哦～真是浪漫的想法啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#1113F人一旦结缘\x01",
            "就有可能获得强大的力量。\x02\x03",

            "#1111F呵呵，当然不一定\x01",
            "适合所有情况……\x02\x03",

            "难得相识\x01",
            "希望珍惜这缘分。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1656)

    label("loc_C02")

    Jump("loc_D14")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_D14")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(    #24
        0x8,
        (
            "#1110F金先生几时预定\x01",
            "等级提高到Ｓ级？\x02\x03",

            "据说大陆只有四个人\x01",
            "的游击士专家……\x02\x03",

            "第五个Ｓ级游击士，\x01",
            "要是是出自于共和国的人就好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_CA0")


    ChrTalk(    #25
        0x8,
        (
            "#1110F艾丝蒂尔·布莱特吗……\x02\x03",

            "我们大使馆平时\x01",
            "也总是承蒙协会的关照。\x02\x03",

            "今后，如果我们有委托\x01",
            "你们能够接受就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_4_4DC end

    def Function_5_D1D(): pass

    label("Function_5_D1D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #26
        0xFE,
        (
            "过几天，共和国\x01",
            "应该会派出调查团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "我们在那之前也有必要\x01",
            "收集一些情报……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E28")

    label("loc_D8F")


    ChrTalk(    #28
        0xFE,
        (
            "利贝尔的通讯\x01",
            "要是全部断绝，这时候\x01",
            "共和国也是一片骚乱吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "过几天，会找个代表\x01",
            "应该会派出调查团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "我们在那之前也有必要\x01",
            "收集一些情报……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E28")

    Jump("loc_1103")

    label("loc_E2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_E41")
    Jump("loc_1103")

    label("loc_E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EB0")

    ChrTalk(    #31
        0xFE,
        (
            "此次只是交换最终的文件\x01",
            "确切的说还不是签字哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "不过，为了方便理解，\x01",
            "就这样称呼了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F50")

    label("loc_EB0")


    ChrTalk(    #33
        0xFE,
        (
            "条约的缔结手续\x01",
            "分为签字和批准两个阶段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "代表者确认条约的内容，\x01",
            "作为证据签名就是签字……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "关于条约的内容国家最后确认，\x01",
            "交换同意的文件就是批准。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F50")

    Jump("loc_1103")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_FE0")

    ChrTalk(    #36
        0xFE,
        (
            "爱尔莎大使的发言偶尔会过激\x01",
            "我也捏着一把冷汗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "但是，她对共和国的事\x01",
            "是真的深思熟虑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "对爱尔莎大使，\x01",
            "我也不惜协力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1103")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 7)), scpexpr(EXPR_END)), "loc_1044")

    ChrTalk(    #39
        0xFE,
        (
            "布置签字仪式真是\x01",
            "忙得不可开交了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不过，想到是为了祖国，\x01",
            "就一点儿也不觉得苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1103")

    label("loc_1044")


    ChrTalk(    #41
        0xFE,
        (
            "怎么，金先生。\x01",
            "又来利贝尔了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x108,
        (
            "#070F约克姆爷爷，\x01",
            "又得暂时麻烦你啦。\x02\x03",

            "话说回来，你好像\x01",
            "忙得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "当然了，因为\x01",
            "要布置条约的签字仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "哈哈，不好意思\x01",
            "暂时没空管你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1657)

    label("loc_1103")

    TalkEnd(0x9)
    Return()

    # Function_5_D1D end

    def Function_6_1107(): pass

    label("Function_6_1107")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(    #45
        0xFE,
        (
            "我年轻的时候\x01",
            "本就没有导力器之类的东西，\x01",
            "所以并不像大家那样吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "正是现在，才有机会\x01",
            "帮上大使的忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123F")

    label("loc_1194")


    ChrTalk(    #47
        0xFE,
        (
            "我年轻的时候\x01",
            "本就没有导力器之类的东西，\x01",
            "所以并不像大家那样吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "现在导力器是司空见惯的了，\x01",
            "我明白大家为何那么惊慌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "正是现在，才有机会\x01",
            "帮上大使的忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_123F")

    Jump("loc_159F")

    label("loc_1242")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12A9")

    ChrTalk(    #50
        0xFE,
        (
            "大使公开坦言\x01",
            "讨厌埃雷波尼亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "但其实其心里\x01",
            "想的却是别的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1315")

    label("loc_12A9")


    ChrTalk(    #52
        0xFE,
        (
            "大使公开坦言\x01",
            "讨厌埃雷波尼亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "但其实其心里\x01",
            "想的却是别的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "呼呼呼……\x01",
            "我深深地明白。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1315")

    Jump("loc_159F")

    label("loc_1318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1380")

    ChrTalk(    #55
        0xFE,
        (
            "为何要做发出恐吓信\x01",
            "这等悲哀的行为呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "国家之间亲密协作……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "到底有哪里\x01",
            "不利呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159F")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_159F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 0)), scpexpr(EXPR_END)), "loc_14BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_146B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13E0")

    ChrTalk(    #58
        0xFE,
        (
            "我的推荐……\x01",
            "还是『人偶骑士』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "真是暖人心怀的故事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_13E0")


    ChrTalk(    #60
        0xFE,
        (
            "如果有空，\x01",
            "读读这里的书吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "书是心灵的营养，\x01",
            "开卷有益哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "我的推荐……\x01",
            "还是『人偶骑士』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "真是暖人心怀的故事。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1468")

    Jump("loc_14BA")

    label("loc_146B")


    ChrTalk(    #64
        0xFE,
        (
            "金先生在利贝尔和共和国\x01",
            "之间来来去去也真是辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "可别勉强搞坏身体哦。\x02",
    )

    CloseMessageWindow()

    label("loc_14BA")

    Jump("loc_159F")

    label("loc_14BD")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #66
        0xFE,
        (
            "哎呀哎呀，那大个子\x01",
            "不是金先生吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "呵呵，无需看脸，\x01",
            "就知道是谁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#073F喂喂，就靠体格\x01",
            "来认我啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1001F……我们第一次\x01",
            "遇到金先生的时候\x01",
            "都误以为是熊来着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x108,
        "#070F……真是的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1658)

    label("loc_159F")

    TalkEnd(0xA)
    Return()

    # Function_6_1107 end

    def Function_7_15A3(): pass

    label("Function_7_15A3")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1613")

    ChrTalk(    #72
        0xFE,
        (
            "就连爱尔莎大使\x01",
            "也是精疲力竭的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "最近连日，为了收集情报\x01",
            "都不眠不休的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1613")

    Jump("loc_1BF5")

    label("loc_1616")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_16AC")

    ChrTalk(    #74
        0xFE,
        (
            "情报部什么的\x01",
            "也引起了相当过激的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "不过，看这状况应该\x01",
            "不会对签字仪式有什么影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "能看出艾莉茜雅女王的想法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_181A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1725")

    ChrTalk(    #77
        0xFE,
        (
            "『克洛斯贝尔问题』\x01",
            "对卡尔瓦德来说也是头痛问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "此次的互不侵犯条约会给议会\x01",
            "带来怎样的影响……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_1725")


    ChrTalk(    #79
        0xFE,
        (
            "『克洛斯贝尔问题』\x01",
            "对我们来说实在是头痛的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "现在，总统勉强\x01",
            "封住了在野党的主张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "但主张武力合并\x01",
            "的意见绝对不算少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "这就是每次，共和国议会\x01",
            "都会暴乱的重大原因之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "此次的互不侵犯条约会给议会\x01",
            "带来怎样的影响……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1817")

    Jump("loc_1BF5")

    label("loc_181A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 1)), scpexpr(EXPR_END)), "loc_199B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1893")

    ChrTalk(    #84
        0xFE,
        (
            "卢安是海上交通的要冲\x01",
            "共和国的船也大量地出入着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "市长选举的结果\x01",
            "必须经过检查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1945")

    label("loc_1893")


    ChrTalk(    #86
        0xFE,
        (
            "卢安的市长选举\x01",
            "不就是今天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "由于戴尔蒙家的垮台\x01",
            "将会有首个平民出身的卢安市长诞生吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "卢安是海上交通的要冲\x01",
            "共和国的船也大量地出入着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "这可必须经过检查。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1945")

    Jump("loc_1998")

    label("loc_1948")


    ChrTalk(    #90
        0xFE,
        (
            "恐吓信只不过是恶作剧\x01",
            "搞出来的勾当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "首先听听爱尔莎大使\x01",
            "的意见不好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    Jump("loc_1BF5")

    label("loc_199B")


    ChrTalk(    #92
        0xFE,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0xFE,
        "呀呀，这不是金先生吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x108,
        "#070F参事官，又给你添麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "今天还接二连三的……\x01",
            "难道是客人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x108,
        "#070F嗯嗯，是协会的工作伙伴。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "……莫非是为了恐吓信的事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x108,
        (
            "#070F你真是明察。\x01",
            "是来自王国军的委托。\x02\x03",

            "#072F有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "这个程度的恐吓信\x01",
            "在共和国不算新奇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "说实话，\x01",
            "我并没在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x108,
        (
            "#572F……的确国内是有\x01",
            "不少过激的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "啊啊，牵涉到移民问题\x01",
            "每次必定引起事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "……嗯，有关这次的事\x01",
            "我也没什么好说的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF2")

    ChrTalk(    #104
        0xFE,
        (
            "首先听听爱尔莎大使\x01",
            "的意见不好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x108,
        (
            "#070F嗯嗯，事不宜迟就这样吧。\x02\x03",

            "那么，告辞了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF2")

    OP_A2(0x1659)

    label("loc_1BF5")

    TalkEnd(0xB)
    Return()

    # Function_7_15A3 end

    def Function_8_1BF9(): pass

    label("Function_8_1BF9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(    #106
        0xFE,
        (
            "油灯不方便\x01",
            "使用时需要注意\x01",
            "不过总觉得有温暖的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "这样的时候\x01",
            "可能是有点不谨慎……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D05")

    label("loc_1C76")


    ChrTalk(    #108
        0xFE,
        (
            "导力灯不能使用之后，\x01",
            "就用火的油灯照明了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "油灯不方便\x01",
            "使用时需要注意\x01",
            "不过总觉得有温暖的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "这样的时候\x01",
            "可能是有点不谨慎……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D05")

    Jump("loc_1F97")

    label("loc_1D08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1D70")

    ChrTalk(    #111
        0xFE,
        (
            "爱尔莎大使的话，\x01",
            "去艾尔贝离宫视察了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "怎么说\x01",
            "都是签字仪式进行的会场嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F97")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DDA")

    ChrTalk(    #113
        0xFE,
        (
            "帝国的女佣\x01",
            "毫无多余的举止，\x01",
            "做事真是爽利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "我也试着学了学，\x01",
            "还真是十分累人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E68")

    label("loc_1DDA")


    ChrTalk(    #115
        0xFE,
        (
            "去百货商店采购\x01",
            "偶然遇到了帝国\x01",
            "大使馆的女佣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "帝国的女佣\x01",
            "毫无多余的举止，\x01",
            "真是精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "我也试着学了学，\x01",
            "还真是十分累人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E68")

    Jump("loc_1F97")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 2)), scpexpr(EXPR_END)), "loc_1EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1EAE")

    ChrTalk(    #118
        0xFE,
        "哼哼哼⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "今天难得全家\x01",
            "去采购吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF6")

    label("loc_1EAE")


    ChrTalk(    #120
        0xFE,
        (
            "金先生，随时\x01",
            "都可以来住宿哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "我会打扫\x01",
            "得干干净净地等你来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF6")

    Jump("loc_1F97")

    label("loc_1EF9")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #122
        0xFE,
        "……啊，金先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x108,
        (
            "#071F哟，我又来了。\x02\x03",

            "#070F可能要借用你的房间，\x01",
            "到时候就靠你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "嘿嘿，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "我会打扫\x01",
            "得干干净净地等你来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165A)

    label("loc_1F97")

    TalkEnd(0xC)
    Return()

    # Function_8_1BF9 end

    def Function_9_1F9B(): pass

    label("Function_9_1F9B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_200D")

    ChrTalk(    #126
        0xFE,
        (
            "丈夫为了见女王，\x01",
            "出发去格兰赛尔城了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "明明如果没有预约\x01",
            "只能白白等着……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B0")

    label("loc_200D")


    ChrTalk(    #128
        0xFE,
        (
            "丈夫现在出门去\x01",
            "格兰赛尔城了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "为了想办法和本国联络，\x01",
            "说要找女王\x01",
            "直接询问什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "明明如果没有预约\x01",
            "只能白白等着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "还是那么不得要领的人。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_20B0")

    TalkEnd(0xD)
    Return()

    # Function_9_1F9B end

    def Function_10_20B4(): pass

    label("Function_10_20B4")

    EventBegin(0x0)
    OP_6D(-2640, 6000, 31460, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(315000, 0)
    OP_6E(467, 0)
    SetChrPos(0x101, 1740, 0, 4440, 0)
    SetChrPos(0x108, 470, 0, 4430, 0)
    SetChrPos(0x104, 660, 0, 2980, 0)
    SetChrPos(0x105, 2100, 0, 3060, 0)

    def lambda_213D():
        OP_6D(1080, 0, 6030, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_213D)

    def lambda_2155():
        OP_67(0, 9000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2155)
    OP_C8(0x200, 0x46, "C_PLAC12._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(1080, 0, 6030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #132
        0x104,
        "#033F嗬，这可真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1011F#5P哦～这就是\x01",
            "卡尔瓦德大使馆啊。\x02\x03",

            "到底是宏伟豪华啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x105,
        (
            "#048F还有这独特的\x01",
            "异国情趣的内部装潢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x108,
        (
            "#070F#5P嗯，因为是接受了\x01",
            "东方移民的国家嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 90, 400)

    ChrTalk(    #136
        0x108,
        (
            "#070F#5P顺带一提爱尔莎大使的房间\x01",
            "在2楼最里面。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #137
        0x101,
        "#1006F#4P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x161C)
    EventEnd(0x0)
    Return()

    # Function_10_20B4 end

    def Function_11_22F3(): pass

    label("Function_11_22F3")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1240, 6000, 30810, 0)
    SetChrPos(0x105, 1990, 6000, 29630, 0)
    SetChrPos(0x104, 890, 6000, 29500, 0)
    SetChrPos(0x108, 990, 6000, 32270, 180)
    OP_6D(880, 6000, 31940, 0)
    OP_67(0, 9360, -10000, 0)
    OP_6B(2360, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #138
        0x108,
        (
            "#070F#5P这里就是大使的房间。\x01",
            "马上去问吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【问问看】\x01",          # 0
            "【过一会再来】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_240C"),
        (1, "loc_245D"),
        (SWITCH_DEFAULT, "loc_2460"),
    )


    label("loc_240C")


    ChrTalk(    #139
        0x108,
        (
            "#070F#5P好，那么我们\x01",
            "我来介绍你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 0, 400)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 12)
    Jump("loc_2460")

    label("loc_245D")

    Jump("loc_2460")

    label("loc_2460")

    EventEnd(0x0)
    Return()

    # Function_11_22F3 end

    def Function_12_2463(): pass

    label("Function_12_2463")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrPos(0x101, 55250, 0, 53510, 0)
    SetChrPos(0x105, 55250, 0, 53510, 0)
    SetChrPos(0x104, 55250, 0, 53510, 0)
    SetChrPos(0x108, 53600, 0, 57290, 0)
    OP_6D(54510, 0, 65790, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(500, 0)
    OP_0D()
    OP_62(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #140
        0x8,
        (
            "#1112F#2P……？\x02\x03",

            "请，可以进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x108,
        "#2P……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_6D(54860, 0, 59130, 1500)
    SetChrPos(0x108, 55250, 0, 53510, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_2589():
        OP_6D(54870, 0, 64209, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2589)
    OP_43(0x108, 0x1, 0x0, 0xD)
    Sleep(700)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_43(0x105, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #142
        0x8,
        (
            "#1111F哎呀，这不是金先生吗！\x02\x03",

            "前阵子才刚回国\x01",
            "又来利贝尔了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x108,
        (
            "#070F#6P呀，协会的工作\x01",
            "还有些需要收尾。\x02\x03",

            "所以大概还会\x01",
            "暂时在利贝尔逗留吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        (
            "#1113F呵呵，不愧是Ａ级游击士。\x01",
            "真是忙碌啊。\x02\x03",

            "#1110F对了，这些人是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1011F#6P嗯，幸会。\x02\x03",

            "我是游击士协会所属的\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "这边的两位是协力的\x01",
            "科洛丝和奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x104,
        "#035F呼，请多指教大使殿下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x105,
        "#048F初次见面。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#1111F请多指教。\x01",
            "我是卡尔瓦德共和国大使\x01",
            "爱尔莎·柯库兰。\x02\x03",

            "#1110F你们似乎是有麻烦\x01",
            "才来拜访的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x108,
        "#074F#6P嗯嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #150
        (
            "\x07\x05艾丝蒂尔等，询问了关于\x01",
            "送到大使馆的恐吓信的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #151
        0x8,
        (
            "#1113F那个恐吓信的事啊……\x02\x03",

            "#1112F这么说你们\x01",
            "是因王国军的委托而行动的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1002F#6P算是这样吧。\x02\x03",

            "不过，作为游击士协会\x01",
            "也不能置之不理。\x02\x03",

            "关于这个，可以配合我们\x01",
            "做一个调查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "#1113F……嗯，也罢。\x01",
            "和我们也有关系嘛。\x02\x03",

            "#1110F那么，你们想问什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1015F#6P嗯，首先是关于威胁者\x01",
            "您有没有线索？\x02\x03",

            "在共和国，是否有对条约缔结\x01",
            "反对的势力存在等……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "#1111F当然有了。\x02\x03",

            "譬如我就是。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #156
        0x101,
        "#1020F#6P咦咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x108,
        (
            "#075F#6P我说大使……\x02\x03",

            "不要太戏弄\x01",
            "年轻人行不行？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#1110F哎呀，事实就是事实嘛。\x02\x03",

            "我讨厌埃雷波尼亚\x01",
            "这你也知道的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x108,
        "#073F#6P这倒是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#1111F呵呵，别误会。\x02\x03",

            "总统已经决定\x01",
            "议会也承认了这议案。\x02\x03",

            "我不会带个人感情\x01",
            "去做事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1007F#6P是，是吗……\x02\x03",

            "#1015F那么其他\x01",
            "反对的人们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#1113F有是有，不过是少数派。\x02\x03",

            "那些势力也应该\x01",
            "不是当真要反对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1004F#6P不是当真反对？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#1110F其实呢，互不侵犯条约本就\x01",
            "不是具有实效性的条约。\x02\x03",

            "『国家间的对立不要经过战争\x01",
            "用协商来和平解决吧』\x01",
            "只是在提倡这种观点而已。\x02\x03",

            "从这个意义来说\x01",
            "与其说是条约不如说是共同宣言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        (
            "#030F只要情况需要，随时都可以\x01",
            "破坏的口头约定而已吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#1111F呵呵，正是如此。\x02\x03",

            "#1110F不过这十几年来，\x01",
            "卡尔瓦德和埃雷波尼亚之间的关系\x01",
            "变得越来越冷淡……\x02\x03",

            "通过这次机会\x01",
            "来交流协商一下\x01",
            "倒也是很有意义的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1015F#6P嗯、嗯……\x02\x03",

            "确实不至于\x01",
            "发出恐吓信来阻止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        (
            "#047F请问，爱尔莎大使。\x02\x03",

            "#042F如果卡尔瓦德相关人员\x01",
            "不是恐吓犯……\x02\x03",

            "那您认为谁比较可疑呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        (
            "#1110F呵呵，这个嘛。\x02\x03",

            "以个人之见来说\x01",
            "埃雷波尼亚的主战派\x01",
            "非常可疑……\x02\x03",

            "#1113F不过加上新型引擎的事\x01",
            "这个可能性看来也不大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1004F#6P新型引擎……\x01",
            "莫非是埃尔赛尤用的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#1111F对，其样本会被\x01",
            "呈送给卡尔瓦德和\x01",
            "埃雷波尼亚双方。\x02\x03",

            "在互不侵犯条约的签字仪式上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1004F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x104,
        (
            "#031F呼，不愧是艾莉茜雅女王。\x02\x03",

            "完全将帝国和共和国\x01",
            "掌控于股掌之间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        (
            "#1113F嗯嗯……\x01",
            "虽然不甘心，但确实是个大人物。\x02\x03",

            "#1112F新型引擎可说是新一代\x01",
            "飞船的核心部件。\x02\x03",

            "虽说只是样品，\x01",
            "但到手的机会也是极为难得。\x02\x03",

            "就算是帝国的主战派\x01",
            "应该也不想错失吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1016F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x108,
        (
            "#070F#6P唔，这么说……\x02\x03",

            "帝国或共和国的人\x01",
            "妨碍互不侵犯条约的可能性\x01",
            "都是相当低的，没错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#1110F是吧。\x02\x03",

            "没帮上忙\x01",
            "十分抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1006F#6P不，哪儿的话。\x02\x03",

            "嫌疑犯减少了\x01",
            "就更容易判断状况了。\x02\x03",

            "#1004F啊，此外还有\x01",
            "别的事想问问……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #179
        "\x07\x05询问了爱尔莎大使关于玲的父母的事。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #180
        0x8,
        (
            "#1112F克洛斯贝尔的贸易商\x01",
            "哈罗德·海瓦斯……\x02\x03",

            "#1113F唔，没有印象呢。\x02\x03",

            "至少应该没\x01",
            "来过大使馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1007F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#1110F说到克洛斯贝尔，\x01",
            "那是帝国和共和国交界处的地区吧。\x02\x03",

            "去帝国大使馆\x01",
            "问问或许更好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1006F#6P好的，明白了。\x02\x03",

            "嗯，多谢您告诉我们\x01",
            "这么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#1110F哎呀，客气什么。\x02\x03",

            "对了你……\x01",
            "叫艾丝蒂尔·布莱特对吧。\x02\x03",

            "难道是卡西乌斯准将的女儿？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1004F#6P啊，您认识我的父亲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x8,
        (
            "#1111F呵呵，当然了。\x02\x03",

            "曾经战胜帝国军的英雄，\x01",
            "王国军的新领导人嘛。\x02\x03",

            "是听说他有个女儿\x01",
            "没想到能以这种形式见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1015F#6P嗯，我还只是\x01",
            "新手游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "#1110F嗯嗯，我明白。\x02\x03",

            "我们大使馆平时\x01",
            "承蒙关照了。\x02\x03",

            "今后如果我们有委托的话，\x01",
            "你们能接下就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "如果有机会的话，非常愿意效劳。\x02\x03",

            "#1006F那么告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 55140, 0, 59720, 180)
    SetChrPos(0x1, 55140, 0, 59720, 180)
    SetChrPos(0x2, 55140, 0, 59720, 180)
    SetChrPos(0x3, 55140, 0, 59720, 180)
    OP_6D(55140, 0, 59720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x161D)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_28(0x8B, 0x2, 0x8)
    OP_28(0x8B, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_12_2463 end

    def Function_13_34CE(): pass

    label("Function_13_34CE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_34E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34E4)
    OP_8E(0xFE, 0xDA7A, 0x0, 0xF528, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_34CE end

    def Function_14_350C(): pass

    label("Function_14_350C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3522():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3522)
    OP_8E(0xFE, 0xD6EC, 0x0, 0xF2EE, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_14_350C end

    def Function_15_354A(): pass

    label("Function_15_354A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3560():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3560)
    OP_8E(0xFE, 0xDA52, 0x0, 0xEDEE, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_15_354A end

    def Function_16_3588(): pass

    label("Function_16_3588")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_359E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_359E)
    OP_8E(0xFE, 0xD566, 0x0, 0xEDA8, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_16_3588 end

    def Function_17_35C6(): pass

    label("Function_17_35C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #190
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_17_35C6 end

    def Function_18_35FA(): pass

    label("Function_18_35FA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #191
        "\x07\x05书架上有『人偶骑士』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第１卷】\x01",      # 0
            "【读第２卷】\x01",      # 1
            "【读第３卷】\x01",      # 2
            "【读第４卷】\x01",      # 3
            "【读第５卷】\x01",      # 4
            "【读第６卷】\x01",      # 5
            "【读第７卷】\x01",      # 6
            "【读第８卷】\x01",      # 7
            "【放弃】\x01",          # 8
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F7")
    OP_B8(0x2EE, 0x0)

    label("loc_36F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3709")
    OP_B8(0x2EF, 0x0)

    label("loc_3709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371B")
    OP_B8(0x2F0, 0x0)

    label("loc_371B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372D")
    OP_B8(0x2F1, 0x0)

    label("loc_372D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373F")
    OP_B8(0x2F2, 0x0)

    label("loc_373F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3751")
    OP_B8(0x2F3, 0x0)

    label("loc_3751")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3763")
    OP_B8(0x2F4, 0x0)

    label("loc_3763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3775")
    OP_B8(0x2F5, 0x0)

    label("loc_3775")

    TalkEnd(0xFF)
    Return()

    # Function_18_35FA end

    def Function_19_3779(): pass

    label("Function_19_3779")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #192
        "\x07\x05书架上有『人偶骑士』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第９卷】\x01",      # 0
            "【读第10卷】\x01",      # 1
            "【读第11卷】\x01",      # 2
            "【读第12卷】\x01",      # 3
            "【读第13卷】\x01",      # 4
            "【读第14卷】\x01",      # 5
            "【读第15卷】\x01",      # 6
            "【读第16卷】\x01",      # 7
            "【放弃】\x01",          # 8
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3876")
    OP_B8(0x2F6, 0x0)

    label("loc_3876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3888")
    OP_B8(0x2F7, 0x0)

    label("loc_3888")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389A")
    OP_B8(0x2F8, 0x0)

    label("loc_389A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AC")
    OP_B8(0x2F9, 0x0)

    label("loc_38AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BE")
    OP_B8(0x2FA, 0x0)

    label("loc_38BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D0")
    OP_B8(0x2FB, 0x0)

    label("loc_38D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3907")
    OP_B8(0x2FC, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3907")
    Sleep(500)
    Call(1, 0)

    label("loc_3907")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3919")
    OP_B8(0x2FD, 0x0)

    label("loc_3919")

    TalkEnd(0xFF)
    Return()

    # Function_19_3779 end

    def Function_20_391D(): pass

    label("Function_20_391D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05书架上有『人偶骑士』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第17卷】\x01",      # 0
            "【读第18卷】\x01",      # 1
            "【读第19卷】\x01",      # 2
            "【读第20卷】\x01",      # 3
            "【读第21卷】\x01",      # 4
            "【读最终卷】\x01",      # 5
            "【放弃】\x01",          # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A00")
    OP_B8(0x2FE, 0x0)

    label("loc_3A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A12")
    OP_B8(0x2FF, 0x0)

    label("loc_3A12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A24")
    OP_B8(0x300, 0x0)

    label("loc_3A24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A36")
    OP_B8(0x301, 0x0)

    label("loc_3A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A48")
    OP_B8(0x302, 0x0)

    label("loc_3A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5A")
    OP_B8(0x303, 0x0)

    label("loc_3A5A")

    TalkEnd(0xFF)
    Return()

    # Function_20_391D end

    SaveToFile()

Try(main)
