from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0113   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0113.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60084",
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
        '拉欧老人',                             # 9
        '亚尔丽 ',                              # 10
        '胡里奥',                               # 11
        '菲特 ',                                # 12
        '尤妮',                                 # 13
        '芙莉莎',                               # 14
        '阿妮娅',                               # 15
        '加通老大',                             # 16
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
        'ED6_DT26/CH20330 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 37070,
        Z                   = 0,
        Y                   = 33560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 38800,
        Z                   = 0,
        Y                   = 30060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4550,
        Z                   = 0,
        Y                   = 37480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3140,
        Z                   = 0,
        Y                   = 32100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3570,
        Z                   = 0,
        Y                   = 33000,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_259",          # 01, 1
        "Function_2_268",          # 02, 2
        "Function_3_3E5",          # 03, 3
        "Function_4_409",          # 04, 4
        "Function_5_461",          # 05, 5
        "Function_6_4BC",          # 06, 6
        "Function_7_5C3",          # 07, 7
        "Function_8_6C5",          # 08, 8
        "Function_9_934",          # 09, 9
        "Function_10_A30",         # 0A, 10
        "Function_11_ACA",         # 0B, 11
        "Function_12_BBB",         # 0C, 12
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_241")
    OP_4A(0x8, 255)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    SetChrPos(0xA, -41280, 0, 35500, 0)
    SetChrPos(0x9, -42700, 0, 37200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 6)

    label("loc_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_258")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)

    label("loc_258")

    Return()

    # Function_0_1EA end

    def Function_1_259(): pass

    label("Function_1_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_267")
    OP_6F(0x2, 15)

    label("loc_267")

    Return()

    # Function_1_259 end

    def Function_2_268(): pass

    label("Function_2_268")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3CF")

    label("loc_28D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3CF")

    label("loc_2A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3CF")

    label("loc_2BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3CF")

    label("loc_2D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3CF")

    label("loc_2F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3CF")

    label("loc_30A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3CF")

    label("loc_323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3CF")

    label("loc_33C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3CF")

    label("loc_355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3CF")

    label("loc_36E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3CF")

    label("loc_387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3CF")

    label("loc_3A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3CF")

    label("loc_3B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3CF")

    label("loc_3E4")

    Return()

    # Function_2_268 end

    def Function_3_3E5(): pass

    label("Function_3_3E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_3E5")

    label("loc_408")

    Return()

    # Function_3_3E5 end

    def Function_4_409(): pass

    label("Function_4_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    Call(0, 12)
    Jump("loc_460")

    label("loc_418")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "那时的铃声……\x01",
            "音色真的很美。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "从未听过\x01",
            "如此清澈的铃音。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_460")

    Return()

    # Function_4_409 end

    def Function_5_461(): pass

    label("Function_5_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470")
    Call(0, 12)
    Jump("loc_4BB")

    label("loc_470")

    TalkBegin(0xA)

    ChrTalk(    #2
        0xFE,
        "你们今天巡逻辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "那如果想起什么的话\x01",
            "我会和协会联络的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_4BB")

    Return()

    # Function_5_461 end

    def Function_6_4BC(): pass

    label("Function_6_4BC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_5BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_528")

    ChrTalk(    #4
        0xFE,
        (
            "总之在雾散之前\x01",
            "我不会让尤妮离开家门半步的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "因为只有我\x01",
            "这个父亲才能保护女儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BF")

    label("loc_528")


    ChrTalk(    #6
        0xFE,
        (
            "听说有好几个人\x01",
            "都沉睡不醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "虽然还不知道\x01",
            "是不是和这场雾有关……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "总、总之暂时不能\x01",
            "让尤妮外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "现在只能用这种办法\x01",
            "来保护自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5BF")

    TalkEnd(0xB)
    Return()

    # Function_6_4BC end

    def Function_7_5C3(): pass

    label("Function_7_5C3")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_6C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_63D")

    ChrTalk(    #10
        0xFE,
        (
            "尤妮虽然也喜欢待在家里，\x01",
            "不过完全不让出门我也不喜欢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "明天要和鲁克他们\x01",
            "在外面尽情的玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C1")

    label("loc_63D")


    ChrTalk(    #12
        0xFE,
        (
            "今天听了爸爸的话，\x01",
            "一整天都待在家里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "唔～不知道鲁克和帕特\x01",
            "有没有在外面玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "他们真好啊……\x01",
            "尤妮也想在外面玩啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_6C1")

    TalkEnd(0xC)
    Return()

    # Function_7_5C3 end

    def Function_8_6C5(): pass

    label("Function_8_6C5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_739")

    ChrTalk(    #15
        0xF,
        (
            "不巧，手上还有很多工作呢，\x01",
            "明天也是一早就要开始工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "嗯，家里的事\x01",
            "就拜托空之女神吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_930")

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_896")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #17
        0xF,
        "啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "你是以前帮助过我们的\x01",
            "游击士小姑娘吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1011F啊，是玛鲁加矿山的老大啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "多亏了你们，\x01",
            "新矿脉的开采很顺利哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        (
            "那时候魔兽跑出来了的洞穴\x01",
            "最后用炸药堵上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1016F真、真…啊哈哈…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "反正过几天也要施工，\x01",
            "就把它完全堵住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "但是，多亏这个\x01",
            "现在的玛鲁加矿山景气多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1032)
    Jump("loc_8D9")

    label("loc_896")


    ChrTalk(    #25
        0xF,
        "哟，游击士小姑娘？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xF,
        (
            "我们的玛鲁加矿山\x01",
            "仍像以往一样地景气，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D9")


    ChrTalk(    #27
        0xF,
        (
            "所以我很忙啊，\x01",
            "得过４、５天才能回家一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        (
            "而且很快又得上山，\x01",
            "真是不容易。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_930")

    TalkEnd(0xF)
    Return()

    # Function_8_6C5 end

    def Function_9_934(): pass

    label("Function_9_934")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9A0")

    ChrTalk(    #29
        0xFE,
        (
            "我丈夫明天又得\x01",
            "一早去矿山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "其实我不想让他去……\x01",
            "但默默地送别也是妻子的义务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2C")

    label("loc_9A0")


    ChrTalk(    #31
        0xFE,
        (
            "今天难得全家\x01",
            "聚在一起吃晚饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "城里虽是这种状况，\x01",
            "我们家里却是很幸福的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "……虽然我丈夫明天要工作，\x01",
            "也算是一瞬间的幸福吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A2C")

    TalkEnd(0xD)
    Return()

    # Function_9_934 end

    def Function_10_A30(): pass

    label("Function_10_A30")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A86")

    ChrTalk(    #34
        0xFE,
        (
            "阿妮娅喂爸爸吃了\x01",
            "一口饭，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "然后爸爸很开心地\x01",
            "说很好吃哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC6")

    label("loc_A86")


    ChrTalk(    #36
        0xFE,
        "今天是三个人的晚饭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "嘿嘿，阿妮娅\x01",
            "要喂爸爸吃饭～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_AC6")

    TalkEnd(0xE)
    Return()

    # Function_10_A30 end

    def Function_11_ACA(): pass

    label("Function_11_ACA")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x2, 15)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    SetChrPos(0xA, -41280, 0, 35500, 0)
    SetChrPos(0x9, -42700, 0, 37200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 6)
    OP_6D(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-41180, 0, 38910, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0134   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_11_ACA end

    def Function_12_BBB(): pass

    label("Function_12_BBB")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -42370, 0, 34440, 0)
    SetChrPos(0x103, -41320, 0, 34290, 0)
    SetChrPos(0xF8, -42850, 0, 33200, 0)
    SetChrPos(0xF9, -41450, 0, 33100, 0)
    OP_8C(0xA, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_6D(-41270, 0, 36170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #38
        0xA,
        "#5P哎呀，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#5P艾丝蒂尔和……\x01",
            "雪拉扎德小姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#020F#4P嗯，晚上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1015F#6P我们受市长先生的委托\x01",
            "来调查此次的事件……\x02\x03",

            "拉欧爷爷的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "#5P嗯……还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#5P看上去睡得很香，\x01",
            "可怎么也叫不醒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "#5P是不是只能等到\x01",
            "明天早上再说了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        (
            "#026F#4P嗯……\x01",
            "现在可能这样比较好。\x02\x03",

            "#022F那么，我们有几个问题想\x01",
            "问一下，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#5P嗯，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#5P只要我们能回答的，\x01",
            "请尽管问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020F#4P感谢你们的合作。\x02\x03",

            "首先是拉欧爷爷是\x01",
            "在何时何地昏倒的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#5P时间……\x01",
            "5点半左右。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "#5P地点……\x02",
    )

    CloseMessageWindow()

    def lambda_E86():
        OP_6D(-42950, 0, 34680, 1200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E86)
    OP_8C(0xA, 230, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #51
        0xA,
        "#5P是在那扇门朝外的那一面。\x02",
    )

    CloseMessageWindow()

    def lambda_ECB():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECB)
    Sleep(50)

    def lambda_EDE():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EDE)
    Sleep(50)

    def lambda_EF1():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_EF1)
    Sleep(50)

    def lambda_F04():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F04)
    Sleep(400)

    ChrTalk(    #52
        0x101,
        (
            "#1015F#5P门朝外的那一面……\x01",
            "也就是在走廊里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#5P嗯，一边敲门一边说\x01",
            "『我回来了』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#5P我打开门出去接他时\x01",
            "我岳父就已经倒在地上了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA7():
        OP_6D(-41270, 0, 36170, 1200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FA7)
    OP_8C(0xA, 180, 400)

    def lambda_FC6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC6)
    Sleep(50)

    def lambda_FD9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FD9)
    Sleep(50)

    def lambda_FEC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_FEC)
    Sleep(50)

    def lambda_FFF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_FFF)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #55
        0x9,
        (
            "#5P我以为爸爸是因为去了\x01",
            "酒馆而醉倒的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#5P可他身上一点酒气也没有，\x01",
            "今天看来是没喝过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#5P但他还是不醒，\x01",
            "实在是让人觉得古怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "#5P我就去找教区长先生了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#026F#4P是这样啊……\x01",
            "大致状况我已经明白了。\x02\x03",

            "#022F最后一个问题……\x02\x03",

            "在拉欧爷爷昏倒前\x01",
            "有没有发生什么怪事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#5P怪事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#5P你是说这雾吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x103,
        (
            "#020F#4P不，这倒不是。\x02\x03",

            "比如见到陌生人或者\x01",
            "听到怪异的声音？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)
    Sleep(500)

    ChrTalk(    #63
        0xA,
        (
            "#2P经你这么一说……\x01",
            "我抬父亲进来的时候……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)
    Sleep(500)

    ChrTalk(    #64
        0x9,
        (
            "#5P嗯……\x01",
            "你也注意到了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#5P那时候一阵慌乱，\x01",
            "到现在才想起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1004F#6P请问……是什么事？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #67
        0xA,
        (
            "#5P我正准备扶昏倒的\x01",
            "岳父到床上时……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#5P听到了微弱的铃声。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1365")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没听到过铃声的说法（没从米蕾奴夫人那里听说）】\x01",      # 0
            "【◇听到过铃声的说法（已从米蕾奴夫人那里听说）】\x01",        # 1
            "【◇不变更】\x01",                                            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1359"),
        (1, "loc_135F"),
        (SWITCH_DEFAULT, "loc_1365"),
    )


    label("loc_1359")

    OP_A3(0x1813)
    Jump("loc_1365")

    label("loc_135F")

    OP_A2(0x1813)
    Jump("loc_1365")

    label("loc_1365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(    #69
        0x103,
        "#023F#4P铃声……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1004F#6P难道是……\x01",
            "我们也听到过的那个？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FB")

    label("loc_13B4")


    ChrTalk(    #71
        0x103,
        "#022F#4P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1002F#6P在这里也能听到铃声……\x02",
    )

    CloseMessageWindow()

    label("loc_13FB")


    ChrTalk(    #73
        0x9,
        "#5P音色非常美啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "#5P大概是有人在\x01",
            "外面摇响的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        (
            "#026F#4P……谢谢。\x01",
            "你们给了我们很多参考。\x02\x03",

            "#020F要是还想起来什么的话\x01",
            "请联系协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#5P嗯……我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F#6P那我们就先告辞了。\x02\x03",

            "明天我们还会来看看情况的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "#5P嗯……\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1505():
        OP_8C(0xA, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1505)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x1815)
    OP_28(0x90, 0x2, 0x80)
    OP_28(0x90, 0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1547")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_1547")

    label("loc_1547")

    EventEnd(0x0)
    Return()

    # Function_12_BBB end

    SaveToFile()

Try(main)
