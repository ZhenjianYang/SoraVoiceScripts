from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4402   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4402.x',
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
        '菲利奥',                               # 9
        '王国军士兵',                           # 10
        '格斯塔夫维修长',                       # 11
        '菲',                                   # 12
        '桑顿',                                 # 13
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH02440 ._CH',             # 02
        'ED6_DT07/CH01550 ._CH',             # 03
        'ED6_DT07/CH01530 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH02440P._CP',             # 02
        'ED6_DT07/CH01550P._CP',             # 03
        'ED6_DT07/CH01530P._CP',             # 04
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1520,
        Z                   = 0,
        Y                   = 9460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3010,
        Z                   = 0,
        Y                   = 400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2520,
        Z                   = 0,
        Y                   = 9450,
        Direction           = 270,
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
        X                   = 6550,
        Z                   = 0,
        Y                   = 11890,
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


    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 7890,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 7890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 10640,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 10640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1720,
        TriggerZ            = 0,
        TriggerY            = 540,
        TriggerRange        = 600,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 540,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_20B",          # 01, 1
        "Function_2_274",          # 02, 2
        "Function_3_3F1",          # 03, 3
        "Function_4_3F6",          # 04, 4
        "Function_5_FFA",          # 05, 5
        "Function_6_105C",         # 06, 6
        "Function_7_1168",         # 07, 7
        "Function_8_125F",         # 08, 8
        "Function_9_13D4",         # 09, 9
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F9")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_20A")

    label("loc_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_20A")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_20A")

    Return()

    # Function_0_1DE end

    def Function_1_20B(): pass

    label("Function_1_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    OP_B1("t4402_y")
    Jump("loc_234")

    label("loc_22B")

    OP_B1("t4402_n")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jump("loc_273")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_273")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)

    label("loc_273")

    Return()

    # Function_1_20B end

    def Function_2_274(): pass

    label("Function_2_274")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DB")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DB")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DB")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DB")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DB")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DB")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DB")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DB")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DB")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DB")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DB")

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DB")

    label("loc_3AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DB")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DB")

    label("loc_3F0")

    Return()

    # Function_2_274 end

    def Function_3_3F1(): pass

    label("Function_3_3F1")

    Call(0, 4)
    Return()

    # Function_3_3F1 end

    def Function_4_3F6(): pass

    label("Function_4_3F6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_409")
    OP_A2(0x0)
    Jump("loc_41F")

    label("loc_409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x80)"), scpexpr(EXPR_END)), "loc_419")
    OP_A2(0x1)
    Jump("loc_41F")

    label("loc_419")

    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇QST104成功】\x01",      # 0
            "【◇QST104失败】\x01",      # 1
            "【◇QST104过期】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_492"),
        (1, "loc_498"),
        (2, "loc_49E"),
        (SWITCH_DEFAULT, "loc_4A7"),
    )


    label("loc_492")

    OP_A2(0x0)
    Jump("loc_4A7")

    label("loc_498")

    OP_A2(0x1)
    Jump("loc_4A7")

    label("loc_49E")

    OP_A3(0x0)
    OP_A3(0x1)
    Jump("loc_4A7")

    label("loc_4A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_508")

    ChrTalk(    #0
        0x8,
        (
            "我已不再玩了\x01",
            "和妻子约好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "说起来，飞船\x01",
            "也还是不能动啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_606")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(    #2
        0x8,
        (
            "……卢安的游戏吧\x01",
            "好像没用导力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "反正也不能工作，\x01",
            "再去游戏吧玩玩也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "唔，我这蠢材蠢材蠢材！\x01",
            "约定不再玩了啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_606")

    label("loc_596")


    ChrTalk(    #5
        0x8,
        (
            "因为这个异常现象\x01",
            "和卢安联络不上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "船何时到达\x01",
            "完全都不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "……既然导力停了\x01",
            "难道船也停了？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_606")

    Jump("loc_FF6")

    label("loc_609")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_81E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 5)), scpexpr(EXPR_END)), "loc_67E")

    ChrTalk(    #8
        0x8,
        (
            "今后要请求王国军合作\x01",
            "来保护引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "为了保证不被夺走\x01",
            "好好管理到签字仪式当日。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B")

    label("loc_67E")


    ChrTalk(    #10
        0x8,
        (
            "你，你们……\x01",
            "那天晚上的游击士吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1000F嗯！在协会\x01",
            "是来看看情况的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "多亏你们\x01",
            "新型引擎的样品\x01",
            "也平安返回了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "真是给大家添麻烦了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_73D")

    ChrTalk(    #14
        0x106,
        "#050F警备方面没问题吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_75A")

    label("loc_73D")


    ChrTalk(    #15
        0x103,
        "#020F警备方面没问题吗？\x02",
    )

    CloseMessageWindow()

    label("loc_75A")


    ChrTalk(    #16
        0x8,
        (
            "那个事件以来，似乎\x01",
            "王国军也愿意合作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "不管怎么，这可是缔结互不侵犯条约\x01",
            "不可或缺的重要之物嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "你们如果也有\x01",
            "要存在仓库的东西，\x01",
            "请尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000F啊哈哈，有机会的话。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1655)

    label("loc_81B")

    Jump("loc_FF6")

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_8AD")

    ChrTalk(    #20
        0x8,
        (
            "新型引擎的样品\x01",
            "签字仪式的那天前都保管在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "这个事务所本身，\x01",
            "原本也是出租仓库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "这里经常有人待着，\x01",
            "警备也相当严格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF6")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_98E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #23
        0x8,
        "妻子给我送了便当。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "今后夜班会增加，\x01",
            "可得加油才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_8FD")


    ChrTalk(    #25
        0x8,
        "妻子给我送了便当。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "这样的我\x01",
            "也会想到啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "……今天预定有\x01",
            "非常重要的东西存到仓库来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "今后夜班会增加，\x01",
            "可得加油才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_98B")

    Jump("loc_FF6")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A27")

    ChrTalk(    #29
        0x8,
        (
            "想起来，我可是\x01",
            "尽给妻子添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "没有钱还搬来王都，\x01",
            "沉沦这个又输光光……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "这样果然是不行啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9D")

    label("loc_A27")


    ChrTalk(    #32
        0x8,
        (
            "呼，妻子简直\x01",
            "变得像外人一样严厉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "早上不知不觉睡过头了\x01",
            "穿着睡衣就跑出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "呼呼，看来睡狮\x01",
            "觉醒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A9D")

    Jump("loc_BF1")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #35
        0x8,
        (
            "去游戏吧旅行\x01",
            "也让妻子够受的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "……不过让她吃苦\x01",
            "也不是这次才开始的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "想起来，结婚以后我一直\x01",
            "给妻子添麻烦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF1")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B88")

    ChrTalk(    #38
        0x8,
        (
            "这里是管理港湾区\x01",
            "工作的事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "接受货轮的搬运\x01",
            "和使用出租仓库的请求哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF1")

    label("loc_B88")


    ChrTalk(    #40
        0x8,
        "哎呀，客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "这里是管理港湾区\x01",
            "工作的事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "接受货轮的搬运\x01",
            "和使用出租仓库的要求哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_BF1")

    Jump("loc_C46")

    label("loc_BF4")


    ChrTalk(    #43
        0x8,
        (
            "这里是管理港湾区\x01",
            "工作的事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "接受货轮的搬运\x01",
            "和使用出租仓库的要求哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C46")

    Jump("loc_FF6")

    label("loc_C49")


    ChrTalk(    #45
        0x8,
        (
            "哎呀？没有预约\x01",
            "的客人真新奇啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DAA")

    ChrTalk(    #46
        0x8,
        "你，你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "这不是以前，在卢安的游戏吧\x01",
            "打败了我的人吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004F啊……\x02\x03",

            "#1001F啊哈哈，那时候\x01",
            "承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "哎～听我说啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "虽然那之后为了赢回输掉的钱\x01",
            "挑战了各种各样的游戏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "但跟你们的\x01",
            "胜负是命运的转折点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "等到发现时之前\x01",
            "赢的钱都输光了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EC8")

    ChrTalk(    #53
        0x8,
        "你，你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "这不是以前，在卢安的游戏吧\x01",
            "不是挑战我输了的人吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1004F啊……\x02\x03",

            "#1008F啊哈哈，那时候\x01",
            "承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        "呀～听我说啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "那之后我来了劲，和店里的\x01",
            "女孩子比扑克牌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "结果，看来跟你们比\x01",
            "把最后的运气都用光了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "等到发现时之前\x01",
            "赢的钱都输光了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC8")


    ChrTalk(    #60
        0x101,
        (
            "#1004F是、是这样吗？\x01",
            "好像很难受啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2C")

    ChrTalk(    #61
        0x104,
        (
            "#035F呼，到最后\x01",
            "就像一夜幻梦一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7E")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F56")

    ChrTalk(    #62
        0x106,
        (
            "#051F不过，这就是\x01",
            "这个了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7E")

    label("loc_F56")


    ChrTalk(    #63
        0x103,
        (
            "#021F嗯，所谓这个\x01",
            "往往就是那样啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7E")


    ChrTalk(    #64
        0x8,
        "……真是吃到苦头了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "做任何事情都是\x01",
            "适可而止最重要啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "也让妻子担心了，\x01",
            "于是决定在这里认真工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1654)
    OP_A2(0x2)

    label("loc_FF6")

    TalkEnd(0x8)
    Return()

    # Function_4_3F6 end

    def Function_5_FFA(): pass

    label("Function_5_FFA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1058")

    ChrTalk(    #67
        0xFE,
        (
            "希德中校指示引擎\x01",
            "由我们来戒备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "若再次被偷，影响签字仪式\x01",
            "那可就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1058")

    TalkEnd(0x9)
    Return()

    # Function_5_FFA end

    def Function_6_105C(): pass

    label("Function_6_105C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_1164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10B6")

    ChrTalk(    #69
        0xFE,
        (
            "#691F我们去找这里的哥们\x01",
            "盖个受领的章就回去。\x02\x03",

            "你们工作也要加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1164")

    label("loc_10B6")


    ChrTalk(    #70
        0xFE,
        (
            "#692F哦，艾丝蒂尔你们啊。\x02\x03",

            "#691F刚才样本已经\x01",
            "平安运送完毕了。\x02\x03",

            "之后到签字仪式当天\x01",
            "只需保管在这里就行了。\x02\x03",

            "我们去找这里的哥们\x01",
            "盖个受领的章就回去。\x02\x03",

            "你们工作也要加油。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1164")

    TalkEnd(0xA)
    Return()

    # Function_6_105C end

    def Function_7_1168(): pass

    label("Function_7_1168")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_125B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #71
        0xFE,
        (
            "这个引擎集中了\x01",
            "技术人员种种构想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "虽然我说不好……\x01",
            "不想被背叛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125B")

    label("loc_11C8")


    ChrTalk(    #73
        0xFE,
        (
            "嗯～没想到\x01",
            "会这么白白让出啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "虽然也不是\x01",
            "想要什么抵押……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "这个引擎集中了\x01",
            "技术人员种种构想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "虽然我说不好……\x01",
            "不想被背叛吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_125B")

    TalkEnd(0xB)
    Return()

    # Function_7_1168 end

    def Function_8_125F(): pass

    label("Function_8_125F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1294")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1291")

    ChrTalk(    #77
        0xFE,
        "呼，工作又堆积起来了。\x02",
    )

    CloseMessageWindow()

    label("loc_1291")

    Jump("loc_13D0")

    label("loc_1294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12AA")
    Jump("loc_13D0")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_12F7")

    ChrTalk(    #78
        0xFE,
        "新型引擎啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "这东西看起来\x01",
            "就很让人期待其高输出能力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_133A")

    ChrTalk(    #80
        0xFE,
        (
            "菲利奥吃爱妻便当啊……\x01",
            "呼，真令人打从心底里羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136D")

    ChrTalk(    #81
        0xFE,
        (
            "嗯……\x01",
            "今天也扎实工作了一天啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_13A4")

    ChrTalk(    #82
        0xFE,
        (
            "负责接待的菲利奥虽是新人\x01",
            "却非常努力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_13D0")

    ChrTalk(    #83
        0xFE,
        (
            "如果有工作的事，\x01",
            "麻烦去柜台啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D0")

    TalkEnd(0xFE)
    Return()

    # Function_8_125F end

    def Function_9_13D4(): pass

    label("Function_9_13D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x05有埃尔赛尤用的新型引擎。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_13D4 end

    SaveToFile()

Try(main)
