from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0210   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0210.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0210   ._SN',
            'ED6_DT21/T0210_1 ._SN',
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
        '米蕾奴夫人',                           # 9
        '玲达',                                 # 10
        '克劳斯市长',                           # 11
        '克劳斯市长',                           # 12
        '潘杜老人',                             # 13
        '红茶',                                 # 14
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
        'ED6_DT07/CH01180 ._CH',             # 00
        'ED6_DT26/CH20330 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02350 ._CH',             # 03
        'ED6_DT07/CH01250 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH02353 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01180P._CP',             # 00
        'ED6_DT26/CH20330P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02350P._CP',             # 03
        'ED6_DT07/CH01250P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH02353P._CP',             # 06
    )

    DeclNpc(
        X                   = 5860,
        Z                   = 0,
        Y                   = 64489,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = -1800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 6080,
        Z                   = 0,
        Y                   = -4640,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 5350,
        Z                   = 200,
        Y                   = -6560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3860,
        Z                   = 0,
        Y                   = -5520,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 200400,
        Z                   = 500,
        Y                   = 49090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_354",          # 02, 2
        "Function_3_4D1",          # 03, 3
        "Function_4_A9C",          # 04, 4
        "Function_5_1243",         # 05, 5
        "Function_6_2323",         # 06, 6
        "Function_7_2D56",         # 07, 7
        "Function_8_2E1C",         # 08, 8
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1D2")
    SetChrPos(0x9, 7070, 0, 64599, 0)
    SetChrPos(0x8, 202000, 0, 1390, 82)

    label("loc_1D2")

    Jump("loc_2FD")

    label("loc_1D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1F0")
    SetChrPos(0x9, 6700, 0, 62710, 270)
    Jump("loc_2FD")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_239")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 25)
    Jump("loc_2FD")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_278")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    Jump("loc_2FD")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    SetChrFlags(0xA, 0x80)
    Jump("loc_2FD")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0")
    SetChrFlags(0x8, 0x10)

    label("loc_2D0")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, 6700, 0, 62710, 270)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2FD")

    label("loc_2F3")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_30B")
    OP_A3(0x10F0)
    Event(0, 8)

    label("loc_30B")

    Return()

    # Function_0_1A2 end

    def Function_1_30C(): pass

    label("Function_1_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_353")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_327")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_353")
    Jump("loc_353")

    label("loc_353")

    Return()

    # Function_1_30C end

    def Function_2_354(): pass

    label("Function_2_354")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4BB")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4BB")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4BB")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4BB")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4BB")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4BB")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4BB")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4BB")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4BB")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4BB")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4BB")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4BB")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4BB")

    label("loc_4A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4BB")

    label("loc_4D0")

    Return()

    # Function_2_354 end

    def Function_3_4D1(): pass

    label("Function_3_4D1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_5C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568")

    ChrTalk(    #0
        0xFE,
        (
            "导力炉不能用了，\x01",
            "做饭真是很很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "嗯。晚餐也变得很难处理，\x01",
            "不知该做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "呼，还是去找夫人\x01",
            "商量商量看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5C2")

    label("loc_568")


    ChrTalk(    #3
        0xFE,
        (
            "导力炉不能用了，\x01",
            "做饭真是很很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "嗯。晚餐也变得很难处理，\x01",
            "不知该做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2")

    Jump("loc_A98")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60F")

    ChrTalk(    #5
        0xFE,
        (
            "啊，艾丝蒂尔，\x01",
            "还有雪拉小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_623")

    label("loc_60F")


    ChrTalk(    #6
        0xFE,
        "啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    label("loc_623")


    ChrTalk(    #7
        0xFE,
        (
            "那个那个……起大雾那时多亏\x01",
            "你们的照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "现在已经恢复健康了，\x01",
            "要继续加油啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6CD")

    label("loc_681")


    ChrTalk(    #9
        0xFE,
        (
            "起大雾那时多亏\x01",
            "你们的照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "现在已经恢复健康了，\x01",
            "要继续加油啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD")

    Jump("loc_A98")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_74C")

    ChrTalk(    #11
        0xFE,
        (
            "昏睡的时候\x01",
            "梦见了以前的事呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "夫人泡了很香\x01",
            "的茶给我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "那美味的茶香\x01",
            "让我想起了小时候的事情～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC")

    label("loc_74C")


    ChrTalk(    #14
        0xFE,
        (
            "昏睡的时候\x01",
            "梦见了以前的事呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "还有我刚见到主人和夫人\x01",
            "时的事情…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "夫人泡了很香\x01",
            "的茶给我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "那以来我一直\x01",
            "就很喜欢那种茶……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "在梦中也好像\x01",
            "能闻见香气呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7FC")

    Jump("loc_A98")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_85E")

    ChrTalk(    #19
        0xFE,
        (
            "整理完茶之后\x01",
            "又要扫除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "对了，不能忘了对客人\x01",
            "微笑……嘿嘿☆\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_A3(0x1)
    Jump("loc_981")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(    #21
        0xFE,
        (
            "夫人非常\x01",
            "擅长泡茶呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "她泡的茶可以\x01",
            "香彻心肺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "嗯～能泡这么香，\x01",
            "果然是有秘诀吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "……不行了。\x01",
            "要早点把茶准备好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_981")

    label("loc_8F1")


    ChrTalk(    #25
        0xFE,
        (
            "呼，好忙好忙。\x01",
            "今天的客人很多，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "不但要扫除，\x01",
            "还要准备好茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "又要扫除又要准备茶，\x01",
            "然后还是扫除…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "总是来回来去做这些事啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_981")

    Jump("loc_A98")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9DB")

    ChrTalk(    #29
        0xFE,
        (
            "主人和夫人现在\x01",
            "还在格兰赛尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "现在两个人正在王都\x01",
            "旅行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A98")

    label("loc_9DB")


    ChrTalk(    #31
        0xFE,
        "啊，你是…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "游击士\x01",
            "艾丝蒂尔吧？！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "你回洛连特了啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "……主人现在\x01",
            "还在格兰赛尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "夫人在主人走之后\x01",
            "也出发去格兰赛尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "呜～夫人没能\x01",
            "见到艾丝蒂尔真遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A98")

    TalkEnd(0x9)
    Return()

    # Function_3_4D1 end

    def Function_4_A9C(): pass

    label("Function_4_A9C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2C")
    Jump("loc_B6E")

    label("loc_B2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B48")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6E")

    label("loc_B48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B64")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6E")

    label("loc_B64")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6E")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_END)), "loc_C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFC")

    ChrTalk(    #37
        0xB,
        (
            "#602F定期船停止航行了，\x01",
            "真是非常时期啊。\x02\x03",

            "嗯，推迟前往王都的计划\x01",
            "看来是正确的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C47")

    label("loc_BFC")


    ChrTalk(    #38
        0xB,
        (
            "#602F定期船停止航行了，\x01",
            "真是非常时期啊。\x02\x03",

            "不好意思，\x01",
            "请你们也帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C47")

    Jump("loc_123A")

    label("loc_C4A")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #39
        0xB,
        (
            "#601F噢噢，是艾丝蒂尔啊，\x01",
            "雪拉小姐也在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1006F市长爷爷，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3F")

    ChrTalk(    #41
        0xB,
        (
            "#603F公主殿下……\x01",
            "您还是很有朝气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        "#048F是啊，托您的福……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#021F市长先生也是一样，\x01",
            "看您这么健康我就安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D67")

    label("loc_D3F")


    ChrTalk(    #44
        0x103,
        (
            "#021F看您还是这么\x01",
            "健康我就安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D67")


    ChrTalk(    #45
        0xB,
        (
            "#601F哈哈，你们两个这么争气，\x01",
            "我这个当市长的也感到面上有光啊。\x02\x03",

            "#600F对了，今天\x01",
            "为什么又回洛连特了？\x02\x03",

            "有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1015F嗯……其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05将因大雾而被迫停留在\x01",
            "洛连特的事情告诉市长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #48
        0xB,
        (
            "#602F原来如此，你们\x01",
            "也是这场雾的受害者。\x02\x03",

            "嗯，推迟前往王都的计划\x01",
            "似乎看来是对的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1015F啊？去王都有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#023F去王都，难道是……\x02\x03",

            "互不侵犯条约的签字仪式吗？！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #51
        0x101,
        (
            "#1004F啊啊！\x02\x03",

            "签、签字仪式！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        (
            "#603F嗯……\x02\x03",

            "我作为地区的代表，\x01",
            "自然必须出席…\x02\x03",

            "但看现在这种雾…\x01",
            "出发只能推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F说、说的对啊……\x02\x03",

            "呼，市长爷爷\x01",
            "也遇到麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#602F不管怎样，总之要暂时\x01",
            "观望一下情况的发展了。\x02\x03",

            "如果遇到什么情况的话，\x01",
            "就和协会一起思考对策吧。\x02\x03",

            "那样的话，\x01",
            "也许又要拜托你们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1006F嗯，当然没问题！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(    #56
        0x106,
        (
            "#050F啊，那是应该的。\x02\x03",

            "再次来到这里也算\x01",
            "是缘分吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B1")

    label("loc_10BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110E")

    ChrTalk(    #57
        0x108,
        (
            "#070F嗯，一定帮忙。\x02\x03",

            "再次来到这里也算\x01",
            "一定是女神的召唤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B1")

    label("loc_110E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(    #58
        0x104,
        (
            "#030F呼，交给我们好啦。\x02\x03",

            "再次来到这里也算\x01",
            "这也是一种缘分啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B1")

    label("loc_1161")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B1")

    ChrTalk(    #59
        0x105,
        (
            "#040F是，我们一定会全力帮忙。\x02\x03",

            "能来到这里\x01",
            "也算是一种缘分吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")


    ChrTalk(    #60
        0xB,
        "#603F那就先谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#020F那么，有什么事情的话\x01",
            "请随时和协会联络。\x02\x03",

            "爱娜会马上\x01",
            "联络到我们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#600F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1881)
    OP_A2(0x2)

    label("loc_123A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_A9C end

    def Function_5_1243(): pass

    label("Function_5_1243")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187B")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #63
        0xA,
        (
            "#601F哟，艾丝蒂尔啊。\x01",
            "今天和约修亚一起来了吗？\x02\x03",

            "上次的大雾事件\x01",
            "多谢你的帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1008F您太客气了，市长爷爷。\x01",
            "没做什么的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1044F大雾事件……\x02\x03",

            "#1043F是吗……\x01",
            "果然是结社的『实验』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#602F不过现在的事态\x01",
            "比之前更加严重得多。\x02\x03",

            "很可能已经覆盖到了\x01",
            "整个王国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1026F啊……嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1035F是啊，整个利贝尔\x01",
            "王国都陷入了导力器瘫痪状态。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1454")

    ChrTalk(    #69
        0x103,
        (
            "#522F这样一来，各种运输\x01",
            "通道也全部瘫痪了。\x02\x03",

            "再这么下去的话，市民\x01",
            "的生活会受到很严重的影响。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_154B")

    label("loc_1454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CF")

    ChrTalk(    #70
        0x106,
        (
            "#050F这样一来，各种运输\x01",
            "方式也全部瘫痪了呢。\x02\x03",

            "再这样下去的话，市民\x01",
            "的生活会受到很严重的影响。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_154B")

    label("loc_14CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(    #71
        0x108,
        (
            "#072F各种运输方式\x01",
            "也全都瘫痪了。\x02\x03",

            "这种状态如果不赶快解决的话，\x01",
            "市民们的生活会受到很严重的影响啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)

    label("loc_154B")


    ChrTalk(    #72
        0xA,
        (
            "#603F原来如此……\x01",
            "比想象中的还要严重啊。\x02\x03",

            "看来必须要\x01",
            "赶快思考对策了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015F不过，在这种非常时期，\x01",
            "洛连特城里却很宁静呢。\x02\x03",

            "简直看不出来和\x01",
            "平时有什么区别…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1040F的确……\x02\x03",

            "和柏斯等城市\x01",
            "比有些不同呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #75
        0xA,
        (
            "#600F嗯，洛连特对\x01",
            "导力器的依赖不是太严重。\x02\x03",

            "这里的主要导力装置\x01",
            "也就是钟楼的时钟了…\x02\x03",

            "#601F而且，洛连特的市民\x01",
            "本来就很悠闲懒散。\x02\x03",

            "所以即使是面对这种处境，\x01",
            "也一样能悠然应对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1708")

    ChrTalk(    #76
        0x103,
        "#021F呵呵，原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1759")

    label("loc_1708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1732")

    ChrTalk(    #77
        0x106,
        "#051F嗯，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1759")

    label("loc_1732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1759")

    ChrTalk(    #78
        0x108,
        "#070F嗯，原来如此。\x02",
    )

    CloseMessageWindow()

    label("loc_1759")


    ChrTalk(    #79
        0x101,
        "#1007F嗯、嗯……不愧是乡村城镇。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #80
        0xA,
        (
            "#600F不管怎么说，在遇到困难时\x01",
            "大家要互相帮助。\x02\x03",

            "我也要准备一下对\x01",
            "其它地区的支援工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1040F……那可太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006F如果需要协会帮忙的话，\x01",
            "请随时和支部联络哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#600F嗯，我会的。\x02\x03",

            "那么，各位。\x01",
            "我期待你们再次活跃啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20A8)
    Jump("loc_1DC3")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A4A")

    ChrTalk(    #84
        0xA,
        (
            "#600F对了，艾丝蒂尔。\x02\x03",

            "听说玛鲁加矿山的事情\x01",
            "已经解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1000F啊，您已经知道了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#1040F虽然过程很危险，\x01",
            "不过总算是把矿工们都安全救出了。\x02\x03",

            "真是千钧一发啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "#600F嗯，在这种状况下\x01",
            "难免会发生意外。\x02\x03",

            "也许以后还会在别处\x01",
            "出现这种事件呢。\x02\x03",

            "抱歉，暂时请继续\x01",
            "保持警备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1000F嗯，了解。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E8")

    ChrTalk(    #89
        0x103,
        "#020F嗯，会注意的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A41")

    label("loc_19E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A16")

    ChrTalk(    #90
        0x106,
        "#050F啊，我们会注意的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A41")

    label("loc_1A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A41")

    ChrTalk(    #91
        0x108,
        "#070F嗯，一定会注意的。\x02",
    )

    CloseMessageWindow()

    label("loc_1A41")

    OP_A3(0x3)
    OP_A2(0x2)
    Jump("loc_1BFC")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B86")

    ChrTalk(    #92
        0xA,
        (
            "#600F听说你们已经\x01",
            "把矿山的危机解决了啊。\x02\x03",

            "这也是因异变而引起\x01",
            "的灾难之一吧。\x02\x03",

            "也许以后还会在别处\x01",
            "出现这种事件呢。\x02\x03",

            "抱歉，暂时请继续\x01",
            "保持警备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1000F嗯，了解。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B27")

    ChrTalk(    #94
        0x103,
        "#020F嗯，会注意的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B80")

    label("loc_1B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B55")

    ChrTalk(    #95
        0x106,
        "#050F啊，我们会注意的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B80")

    label("loc_1B55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B80")

    ChrTalk(    #96
        0x108,
        "#070F嗯，一定会注意的。\x02",
    )

    CloseMessageWindow()

    label("loc_1B80")

    OP_A2(0x2)
    Jump("loc_1BFC")

    label("loc_1B86")


    ChrTalk(    #97
        0xA,
        (
            "#600F矿山事件也是因异变而引起\x01",
            "的灾难之一吧。\x02\x03",

            "也许以后还会在别处\x01",
            "出现这种事件呢。\x02\x03",

            "抱歉，暂时请继续\x01",
            "保持警备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFC")

    Jump("loc_1DC3")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C7F")

    ChrTalk(    #98
        0xA,
        (
            "#600F比起其他城市，\x01",
            "洛连特对导力器的依赖性较低。\x01",
            "市民们的性情也比较懒散。\x02\x03",

            "所以在这种时候\x01",
            "也会表现得比较平静吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC3")

    label("loc_1C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5D")

    ChrTalk(    #99
        0xA,
        (
            "#603F流通渠道出问题的话，\x01",
            "确保生活必需品就成了大问题。\x02\x03",

            "所幸洛连特的\x01",
            "近郊有很多农田。\x01",
            "粮食的供给倒是没有问题。\x02\x03",

            "#602F但柏斯、蔡斯，\x01",
            "还有王都格兰赛尔\x01",
            "可就不是这样了。\x02\x03",

            "我们也要想想怎么才能支援\x01",
            "邻近地区。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1DC3")

    label("loc_1D5D")


    ChrTalk(    #100
        0xA,
        (
            "#602F流通渠道出问题的话，\x01",
            "确保生活必需品就成了大问题。\x02\x03",

            "我们也要想想办法\x01",
            "怎么才能支援\x01",
            "邻近地区。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC3")

    Jump("loc_231F")

    label("loc_1DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_20E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 3)), scpexpr(EXPR_END)), "loc_1E30")

    ChrTalk(    #101
        0xA,
        (
            "#600F看样子你们要继续前往下个地区了啊，\x01",
            "路上要小心啊。\x02\x03",

            "你们的敌人可不是\x01",
            "寻常之辈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E0")

    label("loc_1E30")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #102
        0xA,
        (
            "#600F是艾丝蒂尔你们啊。\x02\x03",

            "事情的经过我\x01",
            "已经听爱娜说了。\x02\x03",

            "调查中的事情还有很多，\x01",
            "一时也没办法全部问清…\x02\x03",

            "#603F……嗯，看来想不通\x01",
            "的事情还有很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1007F想不通的事件\x01",
            "我们也遇到过很多。\x02\x03",

            "现在也只能尽力\x01",
            "解决各地发生的事件了。\x02\x03",

            "#1006F只要努力下去的话，\x01",
            "总会找到解决根本问题的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "#602F嗯，我准备将事件的真相\x01",
            "对市民们隐瞒。\x02\x03",

            "昏睡事件已经解决，\x01",
            "所以没必要再增加市民们的不安情绪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x103,
        (
            "#020F……是吗，那最好不过。\x02\x03",

            "说出来的话也只能\x01",
            "引发骚乱而已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#600F你们似乎要继续前往下个地区了啊。\x01",
            "路上要小心啊。\x02\x03",

            "你们的敌人可不是\x01",
            "寻常之辈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1002F嗯！早已有心理准备了。\x02\x03",

            "#1000F那么，市长爷爷也要保重！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        "#601F嗯，我会平平安安得等你们回来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A63)

    label("loc_20E0")

    Jump("loc_231F")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2166")

    ChrTalk(    #109
        0xA,
        (
            "#600F市民的避难引导工作\x01",
            "真是辛苦你们了。\x02\x03",

            "矿工们的家人\x01",
            "也安心了吧。\x02\x03",

            "不好意思，今后也许还会\x01",
            "需要你们的帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_2166")


    ChrTalk(    #110
        0xA,
        (
            "#600F在阿斯顿队长的指挥下，\x01",
            "士兵们秩序井然。\x02\x03",

            "这样的话，引导避难的工作\x01",
            "真是辛苦你们了。\x02\x03",

            "矿工们的家人\x01",
            "也算是放心了。\x02\x03",

            "不好意思，今后也许还会\x01",
            "需要你们的帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_220C")

    Jump("loc_231F")

    label("loc_220F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_231F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2277")

    ChrTalk(    #111
        0xA,
        (
            "#600F刚才阿斯顿队长\x01",
            "来打过招呼。\x02\x03",

            "指挥官是出身于我们地区的人，\x01",
            "实在是令人安心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231F")

    label("loc_2277")


    ChrTalk(    #112
        0xA,
        (
            "#600F刚才阿斯顿队长\x01",
            "来打过招呼。\x02\x03",

            "指挥官是出身于我们地区的人，\x01",
            "实在是令人安心呢。\x02\x03",

            "不但对这里的地理很熟悉，\x01",
            "而且和市民们也都认识。\x02\x03",

            "简直就像卡西乌斯\x01",
            "来了一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_231F")

    TalkEnd(0xA)
    Return()

    # Function_5_1243 end

    def Function_6_2323(): pass

    label("Function_6_2323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_233B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_233B")
    SetChrFlags(0xFE, 0x10)

    label("loc_233B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_242F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D6")

    ChrTalk(    #113
        0xFE,
        "啊，艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "我听老公说过了，\x01",
            "矿山好像出事了是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "你们在这里\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "今后也请继续\x01",
            "帮助我们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_242C")

    label("loc_23D6")


    ChrTalk(    #117
        0xFE,
        (
            "矿山事件\x01",
            "似乎也是因为这次异变的影响啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "这些讨厌的事件也许\x01",
            "还会不断发生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_242C")

    Jump("loc_2D52")

    label("loc_242F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_264D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F0")

    ChrTalk(    #119
        0x101,
        "#1001F您好，米蕾奴阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #121
        0xFE,
        (
            "啊，这不是艾丝蒂尔\x01",
            "和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "上一次一起来我家玩，\x01",
            "好像都是很久以前的事了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        (
            "#1040F是啊……\x01",
            "调查强盗事件以后就再没来过。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(600)

    ChrTalk(    #124
        0x101,
        (
            "#1004F啊，有那么久了啊……\x02\x03",

            "#1016F嗯，好像都是\x01",
            "很久之前的事情了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #125
        0xFE,
        (
            "呵呵，你们已经\x01",
            "成熟了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "虽然工作那么辛苦，\x01",
            "不过难得两个人一起返乡，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "有时间的话\x01",
            "就多休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_264A")

    label("loc_25F0")


    ChrTalk(    #128
        0xFE,
        (
            "大雾散去，刚松了一口气，\x01",
            "导力器就瘫痪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "呼，利贝尔王国最近\x01",
            "还真是多灾多难。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264A")

    Jump("loc_2D52")

    label("loc_264D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 4)), scpexpr(EXPR_END)), "loc_2725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_26BF")

    ChrTalk(    #130
        0xFE,
        (
            "虽然曾经吃过，\x01",
            "但制作方法就不知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "详细的制作方法最好\x01",
            "还是去问上年纪的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2722")

    label("loc_26BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26EA")
    Call(1, 0)
    Jump("loc_2722")

    label("loc_26EA")


    ChrTalk(    #132
        0xFE,
        (
            "难得有空\x01",
            "回洛连特啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "我给你们\x01",
            "准备了些茶点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2722")

    Jump("loc_283F")

    label("loc_2725")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #134
        0xFE,
        "大家辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "我听先生说过了，\x01",
            "事件好像顺利解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "我家的玲达也\x01",
            "醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "这都多亏了艾丝蒂尔和大家\x01",
            "的帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1017F嘿嘿，没什么啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#020F哪里，身为游击士，\x01",
            "这也是我们的义务。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #140
        0xFE,
        (
            "难得有空\x01",
            "回到洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "我给你们\x01",
            "准备了些茶点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A64)

    label("loc_283F")

    Jump("loc_2D52")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_290F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_288C")

    ChrTalk(    #142
        0xFE,
        (
            "玲达，我给你泡了你最喜欢的\x01",
            "柠檬茶哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "很香吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_290C")

    label("loc_288C")


    ChrTalk(    #144
        0xFE,
        (
            "之前就有感觉要\x01",
            "发生什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "我泡了玲达\x01",
            "最喜欢的柠檬茶哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "虽然我也知道\x01",
            "没有效果…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "但也不能什么也不做。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_290C")

    Jump("loc_2D52")

    label("loc_290F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_29F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2966")

    ChrTalk(    #148
        0xFE,
        (
            "阿斯顿的儿子\x01",
            "好像也醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "执行这种任务…\x01",
            "还真是难为他了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EF")

    label("loc_2966")


    ChrTalk(    #150
        0xFE,
        (
            "刚才阿斯顿先生\x01",
            "来打过招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "鲁克\x01",
            "好像也醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "还只是个小孩子，\x01",
            "竟然会遇到这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "阿斯顿先生\x01",
            "还真是难为他了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_29EF")

    Jump("loc_2D52")

    label("loc_29F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A67")

    ChrTalk(    #154
        0xFE,
        (
            "虽然想她早上就会自然醒，\x01",
            "但现实可没有那么美好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "调查的事加油吧，\x01",
            "现在的希望全在你们身上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B16")

    label("loc_2A67")


    ChrTalk(    #156
        0xFE,
        (
            "虽然幻想玲达\x01",
            "到早上就会醒来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "……但果然是自欺欺人啊。\x01",
            "现实毕竟没有那么美好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "玲达让我来\x01",
            "照看就好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "调查的事情就拜托各位了。\x01",
            "现在的希望全在你们身上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2B16")

    Jump("loc_2D52")

    label("loc_2B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B86")

    ChrTalk(    #160
        0xFE,
        (
            "外边的雾很大，\x01",
            "请一定小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "我也从来没见过这种\x01",
            "怪天气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "总觉得心中很不安。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 1)), scpexpr(EXPR_END)), "loc_2C0F")

    ChrTalk(    #163
        0xFE,
        (
            "我也从来没见过这种\x01",
            "怪天气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "市民们似乎也很不安，\x01",
            "今天一大早就来了好多客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "如果只是普通的自然现象\x01",
            "就最好了…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2C0F")


    ChrTalk(    #166
        0x101,
        "#1000F米蕾奴阿姨，你好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x103,
        "#020F好久不见。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #168
        0xFE,
        (
            "啊，这不是艾丝蒂尔\x01",
            "和雪拉扎德吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "真是好久不见了。\x01",
            "在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1006F嗯，正在街道巡逻。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "是啊…\x01",
            "请小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "城里最近不大正常，\x01",
            "外边的雾一定也很厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "我也从来没见过这种\x01",
            "怪天气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "总觉得心中很不安。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x18A1)
    OP_A2(0x4)

    label("loc_2D52")

    TalkEnd(0x8)
    Return()

    # Function_6_2323 end

    def Function_7_2D56(): pass

    label("Function_7_2D56")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2DAA")

    ChrTalk(    #175
        0xFE,
        (
            "钟楼的事和市长\x01",
            "说过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "呼，既然说完了，\x01",
            "也该回去啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E18")

    label("loc_2DAA")


    ChrTalk(    #177
        0xFE,
        (
            "今日的雾也许会让钟楼\x01",
            "的零件生锈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "为此我马上来和市长\x01",
            "商量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "呼呼呼，\x01",
            "有事一定要早点说啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2E18")

    TalkEnd(0xC)
    Return()

    # Function_7_2D56 end

    def Function_8_2E1C(): pass

    label("Function_8_2E1C")

    EventBegin(0x0)
    SetMapFlags(0x2000000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x9, 255)
    OP_6F(0x5, 10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, 200280, 0, 48270, 60)
    ClearChrFlags(0x8, 0x80)
    OP_6D(199670, 0, 45910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_2EDB():
        OP_6D(201780, 0, 48770, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EDB)
    FadeToBright(1000, 0)
    Sleep(3000)
    SetChrSubChip(0x9, 1)
    Sleep(300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2E1C end

    SaveToFile()

Try(main)
