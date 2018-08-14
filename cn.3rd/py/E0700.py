from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0700   ._SN',
        MapName             = 'Event',
        Location            = 'E0700.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '朵洛希',                               # 9
        '海鸥',                                 # 10
        '海鸥',                                 # 11
        '海鸥',                                 # 12
        '海鸥',                                 # 13
        '海鸥',                                 # 14
        '阿鲁姆',                               # 15
        '艾娅莉',                               # 16
        '乘客',                                 # 17
        '小孩',                                 # 18
        '',                                     # 19
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
        'ED6_DT06/CH20063 ._CH',             # 00
        'ED6_DT06/CH20064 ._CH',             # 01
        'ED6_DT07/CH01740 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT06/CH20063P._CP',             # 00
        'ED6_DT06/CH20064P._CP',             # 01
        'ED6_DT07/CH01740P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
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
        NpcIndex            = 0x1C4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2850,
        Z                   = 5000,
        Y                   = -3440,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2910,
        Z                   = 5000,
        Y                   = -4850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -20,
        Z                   = 5000,
        Y                   = -8840,
        Direction           = 180,
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
        X                   = -20,
        Z                   = 5000,
        Y                   = -10140,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_241",          # 01, 1
        "Function_2_253",          # 02, 2
        "Function_3_3D0",          # 03, 3
        "Function_4_3F4",          # 04, 4
        "Function_5_482",          # 05, 5
        "Function_6_59D",          # 06, 6
        "Function_7_6E8",          # 07, 7
        "Function_8_7CB",          # 08, 8
        "Function_9_8A2",          # 09, 9
        "Function_10_1414",        # 0A, 10
        "Function_11_1450",        # 0B, 11
        "Function_12_149C",        # 0C, 12
        "Function_13_15E9",        # 0D, 13
        "Function_14_1661",        # 0E, 14
        "Function_15_16ED",        # 0F, 15
        "Function_16_1779",        # 10, 16
        "Function_17_17F1",        # 11, 17
        "Function_18_1890",        # 12, 18
        "Function_19_18B3",        # 13, 19
        "Function_20_18D6",        # 14, 20
        "Function_21_18F9",        # 15, 21
        "Function_22_191C",        # 16, 22
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_239")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    Event(0, 9)

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 6)), scpexpr(EXPR_END)), "loc_240")

    label("loc_240")

    Return()

    # Function_0_222 end

    def Function_1_241(): pass

    label("Function_1_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 6)), scpexpr(EXPR_END)), "loc_252")
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x1, 0x64)

    label("loc_252")

    Return()

    # Function_1_241 end

    def Function_2_253(): pass

    label("Function_2_253")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3BA")

    label("loc_278")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3BA")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3BA")

    label("loc_2AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3BA")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3BA")

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3BA")

    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3BA")

    label("loc_30E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3BA")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3BA")

    label("loc_340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3BA")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3BA")

    label("loc_372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3BA")

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3BA")

    label("loc_3A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3BA")

    label("loc_3CF")

    Return()

    # Function_2_253 end

    def Function_3_3D0(): pass

    label("Function_3_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_8D(0xFE, 1100, -9840, -1100, -10840, 2000)
    Jump("Function_3_3D0")

    label("loc_3F3")

    Return()

    # Function_3_3D0 end

    def Function_4_3F4(): pass

    label("Function_4_3F4")

    TalkBegin(0xFE)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    ChrTalk(    #0
        0x10,
        (
            "#150F◆东方地区的葱料理\x01",
            "真的是相当的美味呢～！\x02\x03",

            "◆呵呵，\x01",
            "真是想像一下都口水直流呢。\x02",
        )
    )

    Jump("loc_473")

    label("loc_473")

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_3F4 end

    def Function_5_482(): pass

    label("Function_5_482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #1
        0xFE,
        (
            "宁可小一些也要有温暖的感觉，\x01",
            "这才是家的理想状态啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "对了，就在靠近森林的山丘上\x01",
            "建一间独门独户的房子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_599")

    label("loc_50F")


    ChrTalk(    #3
        0xFE,
        (
            "好～\x01",
            "终于要回到利贝尔了！\x02",
        )
    )

    Jump("loc_53A")

    label("loc_53A")

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "咳咳，接下来就要找新居了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "我说，艾娅莉，你喜欢什么样的房子？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x25B9)

    label("loc_599")

    TalkEnd(0xFE)
    Return()

    # Function_5_482 end

    def Function_6_59D(): pass

    label("Function_6_59D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_63B")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #6
        0xFE,
        (
            "呵呵，阿鲁姆真是的，\x01",
            "现在就说什么新居……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "但是，如果住在那样的房子里面的话，\x01",
            "说不定可以组建一个幸福的家庭哦……㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E4")

    label("loc_63B")


    ChrTalk(    #8
        0xFE,
        (
            "我和他花了半年时间，\x01",
            "一起游历了大陆各国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "真是一次美妙的新婚旅行啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0xFE,
        (
            "果然还是和他\x01",
            "在一起好啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x25BA)

    label("loc_6E4")

    TalkEnd(0xFE)
    Return()

    # Function_6_59D end

    def Function_7_6E8(): pass

    label("Function_7_6E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_719")

    ChrTalk(    #11
        0xFE,
        "唉，小孩子还真是天真无邪……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C7")

    label("loc_719")


    ChrTalk(    #12
        0xFE,
        "妻、妻子她……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "竟然回娘家去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "确实，最近因为工作太忙了，\x01",
            "所以见面的机会变少了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "唉，早知道会变成这样，\x01",
            "应该要早点沟通一下才好啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x25BB)

    label("loc_7C7")

    TalkEnd(0xFE)
    Return()

    # Function_7_6E8 end

    def Function_8_7CB(): pass

    label("Function_8_7CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_86A")

    ChrTalk(    #16
        0xFE,
        (
            "嘿嘿……\x01",
            "我正要去看望妈妈呢～！\x02",
        )
    )

    Jump("loc_807")

    label("loc_807")

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "大叔也要一起去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1068F哈哈……\x01",
            "不是大叔，是大哥吧。\x02\x03",

            "#1066F这个给我记好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E")

    label("loc_86A")


    ChrTalk(    #19
        0xFE,
        "啊哈哈，哇～～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "真是舒服啊～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_A2(0x25BC)

    label("loc_89E")

    TalkEnd(0xFE)
    Return()

    # Function_8_7CB end

    def Function_9_8A2(): pass

    label("Function_9_8A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS537._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(3000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0xFFEC, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS538._CH")
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(5000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C4(0x0, 0x4000)
    SetChrPos(0x109, 150, 5100, -360, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3000, 5000, -3240, 90)
    OP_4A(0x10, 255)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, 15000, 8200, -12100, 0)
    SetChrPos(0x12, 16100, 7900, -11100, 0)
    SetChrPos(0x13, 18100, 8200, -10000, 0)
    SetChrPos(0x14, 19800, 8100, -11000, 0)
    SetChrPos(0x15, 22000, 8300, -11800, 0)
    OP_43(0x11, 0x2, 0x0, 0xD)
    OP_43(0x12, 0x2, 0x0, 0xE)
    OP_43(0x13, 0x2, 0x0, 0xF)
    OP_43(0x14, 0x2, 0x0, 0x10)
    OP_43(0x15, 0x2, 0x0, 0x11)
    OP_6D(5330, 5100, 38370, 0)
    OP_67(0, 14100, -10000, 0)
    OP_6B(5120, 0)
    OP_6C(225000, 0)
    OP_6E(457, 0)
    LoadEffect(0x0, "map\\mp032_00.eff")
    OP_43(0x10, 0x0, 0x0, 0xC)

    def lambda_AB7():

        label("loc_AB7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_AB7")

    QueueWorkItem2(0x10, 1, lambda_AB7)

    def lambda_AC8():
        OP_6D(6370, 3250, -2770, 13000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC8)

    def lambda_AE0():
        OP_67(0, 6310, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AE0)

    def lambda_AF8():
        OP_6B(5720, 11000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF8)

    def lambda_B08():
        OP_6C(225000, 11000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B08)

    def lambda_B18():
        OP_6E(490, 11000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_B18)
    OP_1D(0x1)
    OP_22(0x1C3, 0x1, 0x64)
    OP_43(0x16, 0x1, 0x0, 0xA)
    FadeToBright(3000, 0)
    Sleep(5000)
    OP_C8(0x80, 0x172, "C_PLAC30._CH", 0x1, 0x3E8)
    WaitChrThread(0x109, 0x0)

    def lambda_B5E():
        OP_6D(8630, 4000, -6870, 12000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B5E)

    def lambda_B76():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B76)

    def lambda_B8E():
        OP_6B(4500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B8E)

    def lambda_B9E():
        OP_6C(327000, 13000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B9E)

    def lambda_BAE():
        OP_6E(490, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_BAE)
    Sleep(3500)
    OP_A2(0x1)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    WaitChrThread(0x13, 0x2)
    WaitChrThread(0x14, 0x2)
    WaitChrThread(0x15, 0x2)
    OP_43(0x11, 0x2, 0x0, 0x12)
    OP_43(0x12, 0x2, 0x0, 0x13)
    OP_43(0x13, 0x2, 0x0, 0x14)
    OP_43(0x14, 0x2, 0x0, 0x15)
    OP_43(0x15, 0x2, 0x0, 0x16)
    Sleep(2000)

    def lambda_C07():
        OP_6D(8630, 4000, -2870, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C07)
    OP_44(0x10, 0x1)
    OP_8C(0x10, 180, 400)
    OP_8F(0x10, 0xBF4, 0x1388, 0xFFFFEF52, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_23(0x155)
    Fade(1000)
    OP_24(0x79, 0x46)
    OP_6D(2320, 5000, -4880, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(224000, 0)
    OP_6E(239, 0)
    OP_0D()
    Sleep(100)
    OP_44(0x10, 0x0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #21
        0x10,
        (
            "#150F#5P啊～看不见了。\x02\x03",

            "是一群候鸟吧？\x01",
            "果然和基库不一样，\x01",
            "看来追不上飞艇呢。\x02\x03",

            "#151F可是可是，\x01",
            "大家都好可爱啊㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(600)

    NpcTalk(    #22
        0x109,
        "青年的声音",
        (
            "#1P那个……\x01",
            "小姐，你不就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-220, 5100, -960, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(315000, 0)
    OP_6E(207, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_43(0x109, 0x0, 0x0, 0xB)

    def lambda_DF6():
        OP_6D(1230, 5000, -3040, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DF6)

    def lambda_E0E():
        OP_67(0, 4820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E0E)

    def lambda_E26():
        OP_6B(3850, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E26)

    def lambda_E36():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_E36)

    def lambda_E46():
        OP_6E(207, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E46)

    def lambda_E56():

        label("loc_E56")

        TurnDirection(0x10, 0x109, 400)
        OP_48()
        Jump("loc_E56")

    QueueWorkItem2(0x109, 3, lambda_E56)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #23
        0x10,
        "#153F啊～是你～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1061F#5P朵洛希，好久不见！\x02\x03",

            "#1062F真没想到这么碰巧，\x01",
            "能乘坐同一架航班啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#151F#6P呵呵，我也吃了一惊呢～！\x02\x03",

            "好久不见了。\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #26
        0x10,
        "#153F#6P…………那个………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1064F#5P………………………………\x02\x03",

            "#1068F……难道。\x01",
            "你忘了我的名字吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#151F#6P真、真讨厌～\x01",
            "才没有那样的事呢～\x02\x03",

            "#155F唔，那个，唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #29
        0x10,
        (
            "#151F#6P#3S对了！\x01",
            "是葱头·格拉汉姆～对吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1062F#5P没错没错，水煮或者红烧都好吃，\x01",
            "用来入药也不错哦～\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #31
        0x109,
        "#1068F#5P#3S……才不对吧！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #32
        0x109,
        (
            "#1063F#5P再说了，\x01",
            "怎么想『葱头』都不是人的名字吧！\x02\x03",

            "而且你明明记得格拉汉姆这个姓，\x01",
            "为什么偏偏名字想不起来呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#151F#6P呵呵，开玩笑啦。\x02\x03",

            "#150F其实，\x01",
            "昨天我在东方人街\x01",
            "吃了葱料理呢～～～\x02\x03",

            "那个真的是相当美味哦！\x01",
            "虽然锅里只放了葱，\x01",
            "不过咕噜咕噜的一煮，哇～～好甜！\x02\x03",

            "#151F所以呢，\x01",
            "不知不觉就把你的名字搞错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x109,
        (
            "#1068F#5P唉……\x01",
            "算了。\x02\x03",

            "#1066F对了，朵洛希。\x01",
            "那我的名字到底是……\x02",
        )
    )

    Jump("loc_12FD")

    label("loc_12FD")

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#150F#6P嘿嘿～看我的吧～\x02\x03",

            "#151F#3S陶壶先生。\x01",
            "真是好久不见啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1061F#5P没错没错，将应时的食材放进去焖煮，\x01",
            "就可以做出鲜美的清汤来～\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #37
        0x109,
        (
            "#1069F#3S#5P……喂，\x01",
            "那个怎么说也不可能吧！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0710   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_9_8A2 end

    def Function_10_1414(): pass

    label("Function_10_1414")

    OP_22(0x79, 0x1, 0x0)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Return()

    # Function_10_1414 end

    def Function_11_1450(): pass

    label("Function_11_1450")

    OP_8E(0xFE, 0xF0, 0x1388, 0xFFFFF7F4, 0x7D0, 0x0)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0x5FA, 0x1388, 0xFFFFF038, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_1450 end

    def Function_12_149C(): pass

    label("Function_12_149C")

    Sleep(5000)

    label("loc_14A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15E8")
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_14A1")

    label("loc_15E8")

    Return()

    # Function_12_149C end

    def Function_13_15E9(): pass

    label("Function_13_15E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1660")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(6300)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x3A98, 0x2328, 0xFFFFC75C, 0x320, 0x0)

    def lambda_162B():

        label("loc_162B")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_162B")

    QueueWorkItem2(0xFE, 3, lambda_162B)
    OP_8F(0xFE, 0x3A98, 0x2008, 0xFFFFD0BC, 0x320, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_165D")
    Jump("loc_1660")

    label("loc_165D")

    Jump("Function_13_15E9")

    label("loc_1660")

    Return()

    # Function_13_15E9 end

    def Function_14_1661(): pass

    label("Function_14_1661")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16EC")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(3000)

    def lambda_1686():

        label("loc_1686")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1686")

    QueueWorkItem2(0xFE, 3, lambda_1686)
    OP_8F(0xFE, 0x3E80, 0x1CE8, 0xFFFFDAE4, 0x3E8, 0x0)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x3EE4, 0x206C, 0xFFFFD88C, 0x1F4, 0x0)
    OP_8F(0xFE, 0x3EE4, 0x1EDC, 0xFFFFD4A4, 0x1F4, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16E9")
    Jump("loc_16EC")

    label("loc_16E9")

    Jump("Function_14_1661")

    label("loc_16EC")

    Return()

    # Function_14_1661 end

    def Function_15_16ED(): pass

    label("Function_15_16ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1778")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(2400)
    OP_8F(0xFE, 0x46B4, 0x2328, 0xFFFFDE68, 0x320, 0x0)

    def lambda_1726():

        label("loc_1726")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1726")

    QueueWorkItem2(0xFE, 3, lambda_1726)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x46B4, 0x2134, 0xFFFFDCD8, 0x384, 0x0)
    OP_8F(0xFE, 0x46B4, 0x2008, 0xFFFFD8F0, 0x384, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1775")
    Jump("loc_1778")

    label("loc_1775")

    Jump("Function_15_16ED")

    label("loc_1778")

    Return()

    # Function_15_16ED end

    def Function_16_1779(): pass

    label("Function_16_1779")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17F0")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(3000)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x4D58, 0x1BBC, 0xFFFFD120, 0x320, 0x0)

    def lambda_17BB():

        label("loc_17BB")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_17BB")

    QueueWorkItem2(0xFE, 3, lambda_17BB)
    OP_8F(0xFE, 0x4D58, 0x1FA4, 0xFFFFD508, 0x384, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17ED")
    Jump("loc_17F0")

    label("loc_17ED")

    Jump("Function_16_1779")

    label("loc_17F0")

    Return()

    # Function_16_1779 end

    def Function_17_17F1(): pass

    label("Function_17_17F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_188F")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(2200)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x55F0, 0x2328, 0xFFFFCE00, 0x320, 0x0)

    def lambda_1833():

        label("loc_1833")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1833")

    QueueWorkItem2(0xFE, 3, lambda_1833)
    OP_8F(0xFE, 0x55F0, 0x1F40, 0xFFFFCE00, 0x320, 0x0)

    def lambda_185A():

        label("loc_185A")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_185A")

    QueueWorkItem2(0xFE, 3, lambda_185A)
    OP_8F(0xFE, 0x55F0, 0x206C, 0xFFFFD1E8, 0x44C, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_188C")
    Jump("loc_188F")

    label("loc_188C")

    Jump("Function_17_17F1")

    label("loc_188F")

    Return()

    # Function_17_17F1 end

    def Function_18_1890(): pass

    label("Function_18_1890")

    Sleep(300)
    OP_8F(0xFE, 0x3A98, 0x2008, 0xFFFF8A6C, 0x9C4, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_1890 end

    def Function_19_18B3(): pass

    label("Function_19_18B3")

    Sleep(400)
    OP_8F(0xFE, 0x3EE4, 0x1EDC, 0xFFFF8A6C, 0x8FC, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_18B3 end

    def Function_20_18D6(): pass

    label("Function_20_18D6")

    Sleep(500)
    OP_8F(0xFE, 0x46B4, 0x2008, 0xFFFF8AD0, 0x898, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_18D6 end

    def Function_21_18F9(): pass

    label("Function_21_18F9")

    Sleep(450)
    OP_8F(0xFE, 0x4D58, 0x1FA4, 0xFFFF8AD0, 0x8CA, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_18F9 end

    def Function_22_191C(): pass

    label("Function_22_191C")

    Sleep(350)
    OP_8F(0xFE, 0x55F0, 0x206C, 0xFFFF87B0, 0x992, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_191C end

    SaveToFile()

Try(main)
