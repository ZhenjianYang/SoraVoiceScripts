from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4222   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4222.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '里拉老人',                             # 9
        '艾科尔',                               # 10
        '希尔丹夫人',                           # 11
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
        'ED6_DT06/CH20008 ._CH',             # 00
        'ED6_DT06/CH20107 ._CH',             # 01
        'ED6_DT07/CH00127 ._CH',             # 02
        'ED6_DT07/CH02460 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT06/CH20008P._CP',             # 00
        'ED6_DT06/CH20107P._CP',             # 01
        'ED6_DT07/CH00127P._CP',             # 02
        'ED6_DT07/CH02460P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
    )

    DeclNpc(
        X                   = -138710,
        Z                   = 0,
        Y                   = 7150,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -74270,
        Z                   = 0,
        Y                   = 1530,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_187",          # 01, 1
        "Function_2_1AD",          # 02, 2
        "Function_3_32A",          # 03, 3
        "Function_4_34E",          # 04, 4
        "Function_5_359",          # 05, 5
        "Function_6_4D5",          # 06, 6
        "Function_7_622",          # 07, 7
        "Function_8_EDF",          # 08, 8
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_14B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_14B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -144740, 0, 7150, 0)

    label("loc_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A")
    SetChrFlags(0x9, 0x80)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186")
    Event(0, 7)

    label("loc_186")

    Return()

    # Function_0_13A end

    def Function_1_187(): pass

    label("Function_1_187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3")
    OP_B1("t4222_y")
    Jump("loc_1AC")

    label("loc_1A3")

    OP_B1("t4222_n")

    label("loc_1AC")

    Return()

    # Function_1_187 end

    def Function_2_1AD(): pass

    label("Function_2_1AD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_314")

    label("loc_1D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_314")

    label("loc_1EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_314")

    label("loc_204")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_314")

    label("loc_21D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_314")

    label("loc_236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_314")

    label("loc_24F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_314")

    label("loc_268")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_314")

    label("loc_281")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_314")

    label("loc_29A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_314")

    label("loc_2B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_314")

    label("loc_2CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_314")

    label("loc_2E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_314")

    label("loc_2FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_329")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_314")

    label("loc_329")

    Return()

    # Function_2_1AD end

    def Function_3_32A(): pass

    label("Function_3_32A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34D")
    OP_8D(0xFE, -75980, 4000, -69120, -620, 2000)
    Jump("Function_3_32A")

    label("loc_34D")

    Return()

    # Function_3_32A end

    def Function_4_34E(): pass

    label("Function_4_34E")

    TalkBegin(0xA)
    Call(0, 8)
    TalkEnd(0xA)
    Return()

    # Function_4_34E end

    def Function_5_359(): pass

    label("Function_5_359")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3C2")

    ChrTalk(    #0
        0xFE,
        (
            "在太阳下山之前\x01",
            "必须要做完全部的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "在没有导力器的现在，\x01",
            "天一黑就伸手不见五指。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_444")

    ChrTalk(    #2
        0xFE,
        "情报部的余党都被捕了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "谁让他们搞得王国不得安宁，\x01",
            "真是自作自受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "一定要让他们和理查德上校\x01",
            "一同赎罪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4D1")

    ChrTalk(    #5
        0xFE,
        (
            "《王城设计图》、《七至宝》、\x01",
            "《百日战役全貌》……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "陛下命令我整理出\x01",
            "被情报部带走的书的清单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "陛下到底是想调查什么呢……\x02",
    )

    CloseMessageWindow()

    label("loc_4D1")

    TalkEnd(0xFE)
    Return()

    # Function_5_359 end

    def Function_6_4D5(): pass

    label("Function_6_4D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_52C")

    ChrTalk(    #8
        0xFE,
        (
            "杜南公爵\x01",
            "简直像变了个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "最近甚至还在政务室\x01",
            "接待来投诉的市民。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5CF")

    ChrTalk(    #10
        0xFE,
        (
            "听说在昨天的事件中杜南公爵\x01",
            "被胁持为人质了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "谁让他这么晚还出去晃悠，\x01",
            "真是自讨苦吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "明明被要求在离宫谨慎而居，\x01",
            "可一点都没有在反省的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_61E")

    ChrTalk(    #13
        0xFE,
        (
            "好了，赶紧\x01",
            "打扫完客厅吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "客厅打扫完\x01",
            "还要去里面的资料室帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E")

    TalkEnd(0xFE)
    Return()

    # Function_6_4D5 end

    def Function_7_622(): pass

    label("Function_7_622")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetMapFlags(0x80)
    SetChrPos(0x103, -79000, 0, 9200, 180)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -29660, 350, 60680, 177)
    OP_69(0x101, 0x0)

    ChrTalk(    #15
        0x101,
        "#007F……唔～……好刺眼…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(200)
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    Sleep(1500)

    def lambda_6C7():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C7)

    ChrTalk(    #16 op#5
        0x101,
        "#007F嘿～～～～～……\x05\x02",
    )

    OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)

    def lambda_705():
        OP_99(0xFE, 0xC, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_705)
    Sleep(1000)
    SetChrSubChip(0x101, 14)
    Sleep(200)
    SetChrSubChip(0x101, 17)
    Sleep(200)
    SetChrSubChip(0x101, 18)
    Sleep(200)

    ChrTalk(    #17
        0x101,
        "#007F嗯～～睡得挺好～～！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(400)

    ChrTalk(    #18
        0x101,
        (
            "#004F咦……\x02\x03",

            "…………………………\x02\x03",

            "#000F对了，我们\x01",
            "昨天留宿在王都里面了。\x02\x03",

            "#505F和约修亚一起逛了庆典……\x01",
            "回来途中吃了冰淇淋……\x02\x03",

            "晚上和老爸一起参加晚餐会……\x02\x03",

            "……然后………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_AD(0x240027, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x240028, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x240029, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x24002A, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x101,
        (
            "#580F………………………………\x02\x03",

            "……不………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(500)
    OP_6B(3000, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, -31510, 0, 60590, 176)
    OP_6A(0x101)
    OP_0D()
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        (
            "#004F这是……\x01",
            "约修亚和老爸的房间……\x02\x03",

            "#505F我应该……\x01",
            "是和雪拉姐睡一个房间的……\x02\x03",

            "那个……\x01",
            "……我是什么时候开始做梦的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 5)
    Sleep(1000)

    ChrTalk(    #21
        0x101,
        (
            "#580F啊……\x02\x03",

            "………………………………\x01",
            "………………………………\x02\x03",

            "#005F约修亚！！！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(500)
    OP_8E(0x101, 0xFFFF76EE, 0x0, 0xBEA0, 0x1B58, 0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-67000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -67000, 0, 7200, 180)
    SetChrPos(0x103, -79000, 0, 9200, 180)
    OP_0D()
    OP_8E(0x101, 0xFFFEFB24, 0x0, 0xCDA, 0x1388, 0x0)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    OP_69(0x103, 0x7D0)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_B56():

        label("loc_B56")

        OP_69(0x103, 0x0)
        OP_48()
        Jump("loc_B56")

    QueueWorkItem2(0x103, 3, lambda_B56)
    OP_8E(0x103, 0xFFFECDDE, 0x0, 0xBFE, 0x7D0, 0x0)
    TurnDirection(0x103, 0x101, 1000)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8E(0x103, 0xFFFEEA08, 0x0, 0x8DE, 0x7D0, 0x0)
    OP_44(0x103, 0x3)

    ChrTalk(    #22
        0x103,
        (
            "#021F哎呀，艾丝蒂尔。\x01",
            "你可睡醒了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 1000)

    ChrTalk(    #23
        0x101,
        "#003F雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#025F真是的，昨天那么晚还不回来，\x01",
            "叫人担心死了。\x02\x03",

            "#021F不过看起来，你应该是\x01",
            "和约修亚聊了很多──\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x103, 0x7D0, 0x1388, 0x0)

    ChrTalk(    #25
        0x101,
        "#005F雪拉姐，约修亚在哪儿！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        "#023F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#005F我在找约修亚！\x02\x03",

            "雪拉姐，你见过他么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#023F今早是没见到……\x02\x03",

            "#020F搞什么啊，你不是昨天太累了\x01",
            "就睡在那边的房间了吗？\x02\x03",

            "醒来的时候他不在？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#580F咦……！？\x02\x03",

            "我太累，就睡了……\x01",
            "#005F你、你是听谁说的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#020F老师说的啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#580F老、老爸！？\x02\x03",

            "#005F那么！\x01",
            "你有没有看见老爸！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        (
            "#020F老师他刚才走上楼梯\x01",
            "去了空中庭园啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#002F！！！\x02",
    )

    CloseMessageWindow()

    def lambda_E09():
        OP_8E(0xFE, 0xFFFF23F6, 0x0, 0x58C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E09)
    Sleep(500)

    ChrTalk(    #34
        0x103,
        "#024F啊，等等，艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #35
        0x103,
        "#024F……怎么回事……？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x103, 2)
    OP_99(0x103, 0x0, 0xD, 0x7D0)
    Sleep(1000)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 65535)

    ChrTalk(    #36
        0x103,
        (
            "#022F………………………………\x02\x03",

            "#026F逆位的『恋人』……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1002)
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x2, 0xFF)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_622 end

    def Function_8_EDF(): pass

    label("Function_8_EDF")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, -144700, 0, 5700, 360)
    SetChrPos(0x101, -145560, 0, 5680, 360)
    SetChrPos(0x104, -145320, 0, 4460, 360)
    SetChrPos(0x108, -144920, 0, 3690, 360)
    OP_8C(0xA, 180, 0)
    SetChrSubChip(0xA, 0)
    OP_6D(-144440, 0, 6730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #37
        0xA,
        (
            "#712F#5P科洛蒂娅殿下！？\x01",
            "还有艾丝蒂尔小姐也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x105,
        (
            "#542F#4P希尔丹夫人。\x01",
            "我回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1006F#6P那个，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#711F#5P嗯，是啊……\x02\x03",

            "公主殿下在帮助\x01",
            "艾丝蒂尔的事儿\x01",
            "我也知道。\x02\x03",

            "你们两个……\x01",
            "能平安回来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1025F#6P希尔丹夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#041F#4P呵呵，谢谢。\x02\x03",

            "#040F其实我这次回来，\x01",
            "也同时是为了协会的调查。\x02\x03",

            "有些事想问问\x01",
            "希尔丹夫人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#713F#5P请您随便问吧。\x02\x03",

            "#711F可是，这里似乎\x01",
            "有点不太方便。\x02\x03",

            "我们去会客室吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0xA, -34220, 0, -53190, 270)
    SetChrPos(0x101, -35670, 0, -52660, 90)
    SetChrPos(0x105, -35990, 0, -53890, 90)
    SetChrPos(0x108, -37150, 0, -53340, 90)
    SetChrPos(0x104, -35720, 0, -54910, 45)
    OP_6D(-34480, 0, -52400, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #44
        0xA,
        (
            "#712F#2P原来如此……\x02\x03",

            "你们在调查\x01",
            "那封恐吓信啊。\x02\x03",

            "#710F那么你们想问我的是\x01",
            "对罪犯的身份有没有线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002F#6P是的，一点不错。\x02\x03",

            "总之我们先要遍访\x01",
            "各个收到恐吓信的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "#713F#2P还真是辛苦你们了。\x02\x03",

            "#715F不过我这儿还真\x01",
            "没有什么线索。\x02\x03",

            "我只能说我敢断言\x01",
            "绝不是城堡里的人干的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1007F#6P唔～也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#042F寄到城堡里的恐吓信\x01",
            "寄给谁收的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#714F#2P是女王陛下，\x01",
            "真让人心惊。\x02\x03",

            "因为寄给陛下的\x01",
            "可疑信件都要接受检查，\x01",
            "所以内容我也知道。\x02\x03",

            "#716F还真有这种胆大包天的\x01",
            "不法之徒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x108,
        (
            "#070F#6P我想冒昧问一下……\x02\x03",

            "还有没有什么其他的可疑信件\x01",
            "被寄到城堡里？\x02\x03",

            "比如充满了对王室的\x01",
            "批判的内容的文字之类的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        "#712F#2P这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#043F希尔丹夫人。\x01",
            "我也请求您说出来。\x02\x03",

            "我们需要尽可能多的\x01",
            "判断材料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#713F#2P您既然都这么说了……\x02\x03",

            "#710F我们确实收到过\x01",
            "好几封匿名信。\x02\x03",

            "不过内容并非\x01",
            "批评王室。\x02\x03",

            "多为请求给\x01",
            "理查德上校减刑的。\x02\x03",

            "我想这恐怕是来自\x01",
            "一部分王都的市民……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1004F#6P这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x104,
        (
            "#035F呵呵，不愧是\x01",
            "我过去的竞争对手。\x02\x03",

            "即便被捕，也还是受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        (
            "#542F因为所有人都认可上校\x01",
            "是位有能力的人物……\x02\x03",

            "有人替他惋惜\x01",
            "也是人之常情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x108,
        (
            "#072F#6P不过此类信件看来\x01",
            "和恐吓信没什么关系。\x02\x03",

            "#074F看来恐吓信的目的多半是\x01",
            "企图动摇王室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1015F#6P唔～能了解到这一点\x01",
            "也不错了。\x02\x03",

            "#1004F对了，希尔丹夫人。\x02\x03",

            "还有一件事情\x01",
            "想问您……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05询问了希尔丹夫人关于玲的双亲的事。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #60
        0xA,
        (
            "#712F#2P克洛斯贝尔贸易商，\x01",
            "哈罗德·海瓦斯……\x02\x03",

            "嗯，我知道。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x101,
        "#1005F#6P#3S啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#044F是希尔丹夫人的\x01",
            "相识吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#710F#2P不，只不过他们前几天\x01",
            "申请过城堡内的参观。\x02\x03",

            "因为我正好有空，\x01",
            "就给他们带了路。\x02\x03",

            "我记得他们夫妇\x01",
            "还带着一个女儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1008F#6P是、是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x104,
        (
            "#035F不过这对找寻他们\x01",
            "似乎构不成什么线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "#713F#2P可是……有件事让我比较在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#044F在意的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "#714F#2P他们的女儿虽然参观得\x01",
            "很有兴致……\x02\x03",

            "不过相比之下，\x01",
            "她的父母感觉心不在焉的样子。\x02\x03",

            "虽然和我说话时没什么异样，\x01",
            "可我觉得那恐怕是勉强装出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x108,
        (
            "#074F#6P第一次来这里参观\x01",
            "竟然心不在焉……\x02\x03",

            "#072F很可能是有什么烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        (
            "#043F嗯……\x02\x03",

            "有可能那时候已经\x01",
            "被卷进什么纠纷中去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        (
            "#030F嗯，说不定可以从\x01",
            "这条线查下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006F#6P希尔丹夫人，谢谢您。\x02\x03",

            "您给了我们\x01",
            "很好的提示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#711F#2P那就太好了。\x02\x03",

            "对了，公主殿下，还有各位……\x02\x03",

            "今晚你们应该会住在\x01",
            "格兰赛尔城堡吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        (
            "#040F我在王都的这段时间\x01",
            "是准备住在这里的……\x02\x03",

            "大家呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇已经和帝国大使对话】\x01",      # 0
            "【◇尚未和帝国大使对话】\x01",      # 1
            "【◇什么也没有变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BA9"),
        (1, "loc_1BC1"),
        (SWITCH_DEFAULT, "loc_1BCA"),
    )


    label("loc_1BA9")

    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    Jump("loc_1BCA")

    label("loc_1BC1")

    OP_A3(0x1621)
    OP_A3(0x1622)
    Jump("loc_1BCA")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1C66")

    ChrTalk(    #76
        0x104,
        (
            "#031F我前面也说过了，\x01",
            "我准备住在\x01",
            "埃雷波尼亚大使馆。\x02\x03",

            "所以这份好意我就心领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#070F#6P我也准备留宿在\x01",
            "卡尔瓦德大使馆。\x02\x03",

            "就不劳烦各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF0")

    label("loc_1C66")


    ChrTalk(    #78
        0x104,
        (
            "#031F啊，我今晚\x01",
            "准备住在埃雷波尼亚\x01",
            "大使馆。\x02\x03",

            "所以这份好意我就心领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x108,
        (
            "#070F#6P我也准备留宿在\x01",
            "卡尔瓦德大使馆。\x02\x03",

            "就不劳烦各位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D9C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第１章选了阿加特作为同伴】\x01",        # 0
            "【◇在第１章选了雪拉扎德作为同伴】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D90"),
        (1, "loc_1D96"),
        (SWITCH_DEFAULT, "loc_1D9C"),
    )


    label("loc_1D90")

    OP_A2(0x1201)
    Jump("loc_1D9C")

    label("loc_1D96")

    OP_A3(0x1200)
    Jump("loc_1D9C")

    label("loc_1D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DE4")

    ChrTalk(    #80
        0x101,
        (
            "#1025F#1P唔～我得问问阿加特\x01",
            "和提妲……\x02\x03",

            "再说还有小玲在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1DE4")


    ChrTalk(    #81
        0x101,
        (
            "#1025F#1P唔～我得问问雪拉姐\x01",
            "和提妲……\x02\x03",

            "再说还有小玲在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")


    ChrTalk(    #82
        0x105,
        "#542F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#713F#2P那么我去准备一下房间，\x01",
            "你们随时都可以\x01",
            "过来住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1017F#6P谢谢您，希尔丹夫人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        "#048F那就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "#711F#2P请交给我吧。\x02\x03",

            "我先回女佣室了，\x01",
            "各位\x01",
            "请随意。\x02\x03",

            "那么，告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    def lambda_1F00():
        OP_6D(-34470, 0, -49910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F00)

    def lambda_1F18():

        label("loc_1F18")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1F18")

    QueueWorkItem2(0x101, 2, lambda_1F18)

    def lambda_1F29():

        label("loc_1F29")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1F29")

    QueueWorkItem2(0x105, 2, lambda_1F29)

    def lambda_1F3A():

        label("loc_1F3A")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1F3A")

    QueueWorkItem2(0x104, 2, lambda_1F3A)

    def lambda_1F4B():

        label("loc_1F4B")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1F4B")

    QueueWorkItem2(0x108, 2, lambda_1F4B)
    OP_8E(0xA, 0xFFFF7748, 0x0, 0xFFFF3990, 0x7D0, 0x0)
    Sleep(200)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_8E(0xA, 0xFFFF770C, 0x0, 0xFFFF4156, 0x7D0, 0x0)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x108, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_6D(-35580, 0, -52640, 1600)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2074")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇已经和女王对话】\x01",      # 0
            "【◇尚未和女王对话】\x01",      # 1
            "【◇什么也没有变更】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2068"),
        (1, "loc_206E"),
        (SWITCH_DEFAULT, "loc_2074"),
    )


    label("loc_2068")

    OP_A2(0x1625)
    Jump("loc_2074")

    label("loc_206E")

    OP_A3(0x1625)
    Jump("loc_2074")

    label("loc_2074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2122")
    OP_8C(0x101, 225, 400)

    def lambda_2089():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2089)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #87
        0x101,
        (
            "#1006F#5P好了……\x01",
            "接下来得去见女王陛下。\x02\x03",

            "她应该在女王宫吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x105,
        "#040F嗯，我想是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x104,
        (
            "#035F哼哼，那么\x01",
            "去向她老人家打招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2122")

    OP_8C(0x101, 225, 400)

    def lambda_212F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_212F)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #90
        0x101,
        (
            "#1006F#5P好了……\x02\x03",

            "这样一来从女王陛下和\x01",
            "希尔丹夫人那里都打听过情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x108,
        (
            "#070F#6P我们也该出城堡\x01",
            "回市区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1011F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x2, 0x80)
    OP_28(0x8B, 0x1, 0x100)

    label("loc_21D6")

    Sleep(100)
    OP_A2(0x1626)
    OP_28(0x8B, 0x1, 0x800)
    OP_28(0x8A, 0x1, 0x4)
    OP_28(0x8A, 0x1, 0x8)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_8_EDF end

    SaveToFile()

Try(main)
