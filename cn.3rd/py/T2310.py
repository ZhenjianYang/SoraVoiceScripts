from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2310   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '扎古',                                 # 9
        '索雷诺',                               # 10
        '克拉姆',                               # 11
        '达尼艾尔',                             # 12
        '塞尔吉村长',                           # 13
        '阿梅莉娅',                             # 14
        '萨蒂',                                 # 15
        '特蕾莎院长',                           # 16
        '费瑟尔',                               # 17
        '珂蕾妲婆婆',                           # 18
        '目标用照相机',                         # 19
        '',                                     # 20
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
        'ED6_DT07/CH01460 ._CH',             # 01
        'ED6_DT07/CH02590 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01050 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH02570 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01010 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01460P._CP',             # 01
        'ED6_DT07/CH02590P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01050P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH02570P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01010P._CP',             # 09
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = -28110,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 180,
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
        X                   = -29710,
        Z                   = 0,
        Y                   = 42820,
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
        X                   = -28520,
        Z                   = 0,
        Y                   = 41210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -31800,
        Z                   = 0,
        Y                   = 39140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -31960,
        Z                   = 0,
        Y                   = 42210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -29220,
        Z                   = 0,
        Y                   = 38160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_328",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_4AC",          # 03, 3
        "Function_4_724",          # 04, 4
        "Function_5_A02",          # 05, 5
        "Function_6_D2D",          # 06, 6
        "Function_7_F63",          # 07, 7
        "Function_8_1219",         # 08, 8
        "Function_9_12FD",         # 09, 9
        "Function_10_15DB",        # 0A, 10
        "Function_11_16A6",        # 0B, 11
        "Function_12_1FC3",        # 0C, 12
        "Function_13_1FDC",        # 0D, 13
        "Function_14_207E",        # 0E, 14
        "Function_15_2107",        # 0F, 15
        "Function_16_215F",        # 10, 16
        "Function_17_21C3",        # 11, 17
        "Function_18_2222",        # 12, 18
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -27000, 0, 39020, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30800, 0, 44300, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_2CD")
    SetChrPos(0x14, -31740, 0, 40230, 180)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -29710, 0, 42820, 0)
    Jump("loc_303")

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_2D7")
    Jump("loc_303")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_2F2")
    SetChrPos(0x15, -1740, 0, 7940, 0)
    Jump("loc_303")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_2FC")
    Jump("loc_303")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_303")

    label("loc_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    Event(0, 11)

    label("loc_327")

    Return()

    # Function_0_25A end

    def Function_1_328(): pass

    label("Function_1_328")

    OP_71(0x400, 0x0)
    ExitThread()
    Return()

    # Function_1_328 end

    def Function_2_32F(): pass

    label("Function_2_32F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_496")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_496")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_496")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_496")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_496")

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_496")

    label("loc_3EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_496")

    label("loc_403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_496")

    label("loc_41C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_496")

    label("loc_435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_496")

    label("loc_44E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_496")

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_496")

    label("loc_480")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_4AB")

    Return()

    # Function_2_32F end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4E1")

    ChrTalk(    #0
        0x10,
        (
            "我果然适合\x01",
            "做这种工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534")

    label("loc_4E1")


    ChrTalk(    #1
        0x10,
        (
            "义卖会的收入\x01",
            "都会作为孤儿院的运营经费。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "我果然适合\x01",
            "做这种工作啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_534")

    Jump("loc_720")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_60B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_58E")

    ChrTalk(    #3
        0x10,
        "……算了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "反正平时经常\x01",
            "来帮忙的那位小哥\x01",
            "这次也会来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608")

    label("loc_58E")


    ChrTalk(    #5
        0x10,
        (
            "说起来，\x01",
            "虽然向游击士协会提出了\x01",
            "请求协助义卖会的委托……\x02",
        )
    )

    Jump("loc_5D9")

    label("loc_5D9")

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "却没看到他们的人啊。\x01",
            "……还没来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_608")

    Jump("loc_720")

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_70F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_667")

    ChrTalk(    #7
        0x10,
        "这些商品总共２０米拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "既然是孤儿院的孩子\x01",
            "就算１０米拉好啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C")

    label("loc_667")


    ChrTalk(    #9
        0x10,
        (
            "欢迎！\x01",
            "请买些东西吧！\x02",
        )
    )

    Jump("loc_68C")

    label("loc_68C")

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "……啊，这不是孤儿院的孩子吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "没关系，\x01",
            "有什么想要的\x01",
            "就尽管说啊。\x02",
        )
    )

    Jump("loc_6E8")

    label("loc_6E8")

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "会特别给你们算便宜些哦！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_70C")

    Jump("loc_720")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_719")
    Jump("loc_720")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_720")

    label("loc_720")

    TalkEnd(0x10)
    Return()

    # Function_3_4AC end

    def Function_4_724(): pass

    label("Function_4_724")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_81A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #13
        0x11,
        "来来，随便看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "在所谓的义卖会上，\x01",
            "与其说是购物不如说是体会气氛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_817")

    label("loc_78B")


    ChrTalk(    #15
        0x11,
        (
            "最先举办义卖会的人，\x01",
            "好像是杰尼丝学院的学生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "现在已经完全\x01",
            "变成村里的特色活动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "怎么说呢，\x01",
            "就像节日一样开心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_817")

    Jump("loc_9FE")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(    #18
        0x11,
        (
            "顺带一提，义卖会的实行委员\x01",
            "虽然只有我和扎古两人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        "不过也能算得上是个委员会吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FD")

    label("loc_88A")


    ChrTalk(    #20
        0x11,
        (
            "今年的义卖会已经是第三届了。\x01",
            "最近似乎已经有常客了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "我作为从一开始就参加的人\x01",
            "真是再开心不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8FD")

    Jump("loc_9FE")

    label("loc_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_9ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_961")

    ChrTalk(    #22
        0x11,
        (
            "抱歉哦，\x01",
            "那好像是个古老的传说。\x02\x03",

            "我也不知道\x01",
            "详细的情况呢。\x02",
        )
    )

    Jump("loc_95D")

    label("loc_95D")

    CloseMessageWindow()
    Jump("loc_9EA")

    label("loc_961")


    ChrTalk(    #23
        0x11,
        (
            "呀，这不是刚才的孩子吗。\x01",
            "又是来打听事情的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "很遗憾，\x01",
            "我也不知道详细情况。\x02",
        )
    )

    Jump("loc_9C4")

    label("loc_9C4")

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        "因为是从老爸那里听来的嘛。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9EA")

    Jump("loc_9FE")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_9F7")
    Jump("loc_9FE")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_9FE")

    label("loc_9FE")

    TalkEnd(0x11)
    Return()

    # Function_4_724 end

    def Function_5_A02(): pass

    label("Function_5_A02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_AE5")
    OP_8C(0xFE, 180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A6E")

    ChrTalk(    #26
        0xFE,
        "老师，不用那么担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "对于孩子们来说，\x01",
            "老师的笑容就是最好的礼物哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE2")

    label("loc_A6E")


    ChrTalk(    #28
        0xFE,
        "……真是个相当好的孩子哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "小小年纪就那么懂事，\x01",
            "完全不用人操心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "孩子们都会成长的啊，老师。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AE2")

    Jump("loc_D29")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B34")

    ChrTalk(    #31
        0xFE,
        "村里的年轻人也都很起劲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "呵呵，真是令人高兴啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9B")

    label("loc_B34")


    ChrTalk(    #33
        0xFE,
        (
            "今天早上的梅威海道\x01",
            "似乎没什么魔兽出现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "是不是因为要开义卖会，\x01",
            "所以有人去开路了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B9B")

    Jump("loc_D29")

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_BF2")

    ChrTalk(    #35
        0xFE,
        (
            "今年到底会有些\x01",
            "什么好东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "呵呵，真是令人期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_BF2")


    ChrTalk(    #37
        0xFE,
        (
            "我也差不多\x01",
            "该去逛一逛了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "呵呵，今年到底\x01",
            "会有些什么好东西呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_C43")

    Jump("loc_D29")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(    #39
        0xFE,
        "风车小屋在村外的高台上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不介意的话\x01",
            "你们也去玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1F")

    label("loc_C9A")


    ChrTalk(    #41
        0xFE,
        "哦？是孤儿院的孩子们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "呵呵，村里就像过节一样对吧？\x01",
            "风车小屋的义卖会开始了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "不介意的话\x01",
            "你们也去玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_D1F")

    Jump("loc_D29")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_D29")

    label("loc_D29")

    TalkEnd(0xFE)
    Return()

    # Function_5_A02 end

    def Function_6_D2D(): pass

    label("Function_6_D2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D5F")

    ChrTalk(    #44
        0xFE,
        "好了，接下来买什么呢⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_DBB")

    label("loc_D5F")


    ChrTalk(    #45
        0xFE,
        "嘿嘿，我买到锅子了呢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "真不愧是义卖会呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "想要的东西\x01",
            "一下就找到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_DBB")

    Jump("loc_F5F")

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E1F")

    ChrTalk(    #48
        0xFE,
        (
            "……之前的锅子\x01",
            "已经烧焦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "唉，\x01",
            "义卖会上有没有锅子卖呢？\x02",
        )
    )

    Jump("loc_E1B")

    label("loc_E1B")

    CloseMessageWindow()
    Jump("loc_EA3")

    label("loc_E1F")


    ChrTalk(    #50
        0xFE,
        (
            "玛诺利亚村的义卖会，\x01",
            "扎古从一开始就参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "那孩子小时候经常迷路，\x01",
            "总是让人担心得到处找，\x01",
            "不过现在真是可靠多了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_EA3")

    Jump("loc_F5F")

    label("loc_EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EFA")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #52
        0xFE,
        "记得这边有我的旧衣服……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "咦～？　没有了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F55")

    label("loc_EFA")


    ChrTalk(    #54
        0xFE,
        (
            "唔～有没有什么\x01",
            "可以拿去义卖会卖掉的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "扎古的旧衣服，\x01",
            "谁也不会买吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F55")

    Jump("loc_F5F")

    label("loc_F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_F5F")

    label("loc_F5F")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2D end

    def Function_7_F63(): pass

    label("Function_7_F63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #56
        0xFE,
        (
            "……真希望也能开设\x01",
            "面向孩子的垂钓教室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1215")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_1063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #57
        0xFE,
        (
            "据本人推测，\x01",
            "到这周末都会持续晴天的天气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "一流的垂钓人对天气也是很敏感的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1060")

    label("loc_1009")


    ChrTalk(    #59
        0xFE,
        (
            "今天的天气\x01",
            "似乎也很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "一会儿就去灯塔的山麓那边\x01",
            "看看能钓上什么鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1060")

    Jump("loc_1215")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_113F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_10C2")

    ChrTalk(    #61
        0xFE,
        (
            "玛诺利亚村……\x01",
            "真是个不错的村子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "作为垂钓场所\x01",
            "也是无可挑剔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113C")

    label("loc_10C2")


    ChrTalk(    #63
        0xFE,
        (
            "我每年都会\x01",
            "来这个村子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "真是个不错的村子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "等我老了之后，\x01",
            "真想在这样宁静的村子里\x01",
            "安度晚年啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_113C")

    Jump("loc_1215")

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(    #66
        0xFE,
        (
            "……这附近似乎也有\x01",
            "优秀的钓鱼爱好者呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "真希望他也能\x01",
            "加入我们钓公师团。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120B")

    label("loc_11A6")


    ChrTalk(    #68
        0xFE,
        (
            "以前我在这个义卖会上\x01",
            "找到过很好的钓竿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "虽然是手制的但很好用，\x01",
            "是我非常喜欢的钓竿。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_120B")

    Jump("loc_1215")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_1215")

    label("loc_1215")

    TalkEnd(0xFE)
    Return()

    # Function_7_F63 end

    def Function_8_1219(): pass

    label("Function_8_1219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_125A")

    ChrTalk(    #70
        0xFE,
        (
            "我也有拿出东西来卖哦。\x01",
            "请一定去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D1")

    label("loc_125A")


    ChrTalk(    #71
        0xFE,
        "您好，欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "这里全部都是\x01",
            "村里的居民拿出来的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "嘿嘿，我也有拿东西来卖。\x01",
            "请一定去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12D1")

    Jump("loc_12F9")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_12DE")
    Jump("loc_12F9")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_12E8")
    Jump("loc_12F9")

    label("loc_12E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_12F2")
    Jump("loc_12F9")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_12F9")

    label("loc_12F9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1219 end

    def Function_9_12FD(): pass

    label("Function_9_12FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_15B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 2)), scpexpr(EXPR_END)), "loc_13E5")
    OP_8C(0x17, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1350")

    ChrTalk(    #74
        0x17,
        (
            "#754F果然还是不想成为\x01",
            "我的负担吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E2")

    label("loc_1350")


    ChrTalk(    #75
        0x17,
        (
            "#754F是的，\x01",
            "虽然懂事是很好……\x02\x03",

            "#757F但因此却总是被别人依赖，\x01",
            "从来不会向别人撒娇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14E,
        "#1713F（……………………）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_13E2")

    Jump("loc_15AF")

    label("loc_13E5")


    ChrTalk(    #77
        0x17,
        (
            "#753F哎呀，玛丽？\x01",
            "你没跟波利在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x14E,
        (
            "#1713F嗯、嗯……\x02\x03",

            "波利和克拉姆他们\x01",
            "在一块儿玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x17,
        (
            "#750F是吗……\x02\x03",

            "#754F玛丽，\x01",
            "要是有什么事要马上告诉老师哦？\x02\x03",

            "不要一个人放在心里。\x01",
            "……知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x14E,
        (
            "#1714F是、是！\x02\x03",

            "#1712F……………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14E,
        (
            "#1713F（不、不行………………）\x02\x03",

            "（礼物的事情还是秘密，\x01",
            "  而且波利会不见\x01",
            "  也是我的错……）\x02\x03",

            "#1713F（我还是自己\x01",
            "  再去找一下吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3A)

    label("loc_15AF")

    Jump("loc_15D7")

    label("loc_15B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_15BC")
    Jump("loc_15D7")

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_15C6")
    Jump("loc_15D7")

    label("loc_15C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_15D0")
    Jump("loc_15D7")

    label("loc_15D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_15D7")

    label("loc_15D7")

    TalkEnd(0xFE)
    Return()

    # Function_9_12FD end

    def Function_10_15DB(): pass

    label("Function_10_15DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_167D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(    #82
        0xFE,
        "果然有人想要呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "呼，真是松了一口气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_167A")

    label("loc_1623")


    ChrTalk(    #84
        0xFE,
        (
            "哎呀呀，\x01",
            "我的锅已经卖掉了啊。\x02",
        )
    )

    Jump("loc_1653")

    label("loc_1653")

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "呼，\x01",
            "果然有人想要呢。\x02",
        )
    )

    Jump("loc_1676")

    label("loc_1676")

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_167A")

    Jump("loc_16A2")

    label("loc_167D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_1687")
    Jump("loc_16A2")

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_1691")
    Jump("loc_16A2")

    label("loc_1691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_169B")
    Jump("loc_16A2")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_16A2")

    label("loc_16A2")

    TalkEnd(0xFE)
    Return()

    # Function_10_15DB end

    def Function_11_16A6(): pass

    label("Function_11_16A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4A(0x11, 255)
    OP_4A(0x10, 255)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrPos(0x14E, -30500, -500, 34700, 0)
    SetChrPos(0x14F, -29780, -500, 34700, 0)
    OP_9F(0x14E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-29140, 0, 47160, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(55000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)

    def lambda_1752():
        OP_6D(-29140, 0, 39160, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1752)

    def lambda_176A():
        OP_6B(2720, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_176A)

    def lambda_177A():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_177A)
    Sleep(5000)

    def lambda_178F():
        OP_8E(0xFE, 0xFFFF8878, 0x0, 0x8F34, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_178F)

    def lambda_17AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_17AA)
    Sleep(300)

    def lambda_17C1():
        OP_8E(0xFE, 0xFFFF8B48, 0x0, 0x8D40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_17C1)

    def lambda_17DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14F, 2, lambda_17DC)
    OP_0D()
    WaitChrThread(0x1A, 0x1)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x14F, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_43(0x14E, 0x3, 0x0, 0xC)
    OP_8C(0x14F, 45, 400)
    Sleep(500)
    OP_8C(0x14F, 0, 400)
    Sleep(500)
    OP_8C(0x14F, 45, 400)
    Sleep(400)

    ChrTalk(    #86
        0x14F,
        (
            "#1733F哦……\x01",
            "好厉害——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x14E,
        (
            "#1714F#12P哇，有好多商品哦。\x02\x03",

            "#1719F嗯，有没有什么好东西呢……\x02\x03",

            "适合老师的漂亮的东西……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18C7():
        OP_6D(-28370, 0, 39810, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_18C7)
    OP_43(0x14E, 0x2, 0x0, 0xD)
    OP_43(0x14F, 0x2, 0x0, 0xE)
    WaitChrThread(0x14F, 0x2)
    WaitChrThread(0x1A, 0x0)
    SetChrPos(0x12, -30080, -500, 34500, 0)
    SetChrPos(0x13, -30080, -500, 34500, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    OP_43(0x12, 0x3, 0x0, 0xF)
    OP_43(0x13, 0x3, 0x0, 0x10)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x14F)
    OP_8C(0x14F, 180, 400)
    Sleep(200)
    OP_8C(0x10, 225, 400)
    WaitChrThread(0x13, 0x3)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(100)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(500)
    OP_62(0x12, 0x0, 1600, 0x26, 0x27, 0xC8, 0x5)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(500)
    OP_8C(0x13, 0, 400)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(100)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(500)
    OP_62(0x12, 0x0, 1600, 0x26, 0x27, 0xC8, 0x5)
    Sleep(300)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x14F)
    Sleep(1000)
    OP_43(0x12, 0x3, 0x0, 0x11)
    OP_43(0x13, 0x3, 0x0, 0x12)
    WaitChrThread(0x13, 0x3)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x10, 270, 400)
    Sleep(200)
    OP_8C(0x14F, 90, 400)

    def lambda_1AAD():
        OP_6D(-29390, 0, 44230, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1AAD)

    def lambda_1AC5():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1AC5)

    def lambda_1AD5():
        OP_6C(39000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1AD5)
    WaitChrThread(0x1A, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0x14E, 0x2)
    OP_63(0x14E)
    OP_8C(0x14E, 45, 400)
    Sleep(500)

    ChrTalk(    #88
        0x14E,
        (
            "#1900F#12P（义卖会给人的感觉\x01",
            "  像是在卖魔法道具似的……）\x02\x03",

            "#1900F（嗯……\x01",
            "  好像没有幸福之石……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x11,
        "#5P呀，在找什么东西呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x14E, 0, 400)

    ChrTalk(    #90
        0x14E,
        (
            "#1714F#12P嗯、嗯……\x02\x03",

            "#1900F（还、还是\x01",
            "  稍微打听一下吧？？）\x02\x03",

            "#1718F请、请问……\x01",
            "您觉得世界上有幸福之石吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        "#5P…………咦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x14E,
        (
            "#1710F#12P那是能让\x01",
            "拥有它的人\x01",
            "得到幸福的石头……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        "#5P这、这个…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        (
            "#5P哈哈，\x01",
            "我可不太了解……\x02",
        )
    )

    Jump("loc_1CE8")

    label("loc_1CE8")

    CloseMessageWindow()

    ChrTalk(    #95
        0x14E,
        (
            "#1713F#12P也、也是……\x02\x03",

            "#1716F谢谢您，打扰了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 400)
    Sleep(300)

    def lambda_1D3D():
        OP_8E(0xFE, 0xFFFF88FA, 0x0, 0xA0E6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1D3D)

    def lambda_1D58():
        OP_6D(-29590, 0, 43800, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1D58)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #96
        0x11,
        "#5P啊，对了……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x1A, 0x0)

    ChrTalk(    #97
        0x11,
        (
            "#5P这、这么说来，\x01",
            "我倒是听说过古罗尼连峰发生的怪事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x11,
        (
            "#5P是很神秘的事情，\x01",
            "…………你想知道吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 600)
    Sleep(400)

    ChrTalk(    #99
        0x14E,
        "#1718F#12P……想、想！\x02",
    )

    CloseMessageWindow()

    def lambda_1E52():
        OP_6D(-29600, 0, 44770, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1E52)
    OP_8E(0x14E, 0xFFFF8774, 0x0, 0xA604, 0x5DC, 0x0)
    WaitChrThread(0x1A, 0x0)
    Sleep(300)

    ChrTalk(    #100
        0x11,
        (
            "#5P是老爸告诉我的，\x01",
            "那还真是个古老的故事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#5P正好就是现在这个季节吧……\x01",
            "每年的某个时间，\x01",
            "古罗尼的山中就会突然发出金色的光芒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        (
            "#5P碰巧在这个时期去山里的人，\x01",
            "好像都有过不可思议的经历。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        (
            "#5P而在那之后，\x01",
            "似乎都变得非常幸福……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(2000, 0, -1)

    def lambda_1FA6():
        OP_6B(2560, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1FA6)
    OP_0D()
    Sleep(2200)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2300   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_11_16A6 end

    def Function_12_1FC3(): pass

    label("Function_12_1FC3")

    Sleep(500)
    OP_8C(0x14E, 45, 400)
    Sleep(800)
    OP_8C(0x14E, 0, 400)
    Return()

    # Function_12_1FC3 end

    def Function_13_1FDC(): pass

    label("Function_13_1FDC")


    def lambda_1FE2():
        OP_8E(0xFE, 0xFFFF8D3C, 0x0, 0x9920, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1FE2)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 90, 400)
    Sleep(2000)
    OP_8C(0x14E, 45, 400)
    Sleep(2000)
    OP_8C(0x14E, 0, 400)

    def lambda_2021():
        OP_8E(0xFE, 0xFFFF89B8, 0x0, 0xA6A4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2021)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 0, 400)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)

    label("loc_2059")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_207D")
    OP_8C(0x14E, 45, 400)
    Sleep(2500)
    OP_8C(0x14E, 0, 400)
    Sleep(3500)
    Jump("loc_2059")

    label("loc_207D")

    Return()

    # Function_13_1FDC end

    def Function_14_207E(): pass

    label("Function_14_207E")

    Sleep(500)
    OP_8C(0x14F, 0, 400)
    Sleep(400)
    OP_8C(0x14F, 45, 400)
    Sleep(400)

    def lambda_20A1():
        OP_8E(0xFE, 0xFFFF8E04, 0x0, 0x9510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_20A1)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 90, 400)
    Sleep(2500)
    OP_8C(0x14F, 135, 400)
    Sleep(2000)
    OP_8C(0x14F, 0, 400)

    def lambda_20E0():
        OP_8E(0xFE, 0xFFFF8E2C, 0x0, 0x9B00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_20E0)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 90, 400)
    Sleep(3000)
    Return()

    # Function_14_207E end

    def Function_15_2107(): pass

    label("Function_15_2107")


    def lambda_210D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_210D)

    def lambda_211F():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_211F)
    WaitChrThread(0x12, 0x1)

    def lambda_213F():
        OP_8E(0xFE, 0xFFFF8E2C, 0x0, 0x92E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_213F)
    WaitChrThread(0x12, 0x1)
    Sleep(6000)
    Return()

    # Function_15_2107 end

    def Function_16_215F(): pass

    label("Function_16_215F")

    Sleep(500)

    def lambda_216A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_216A)

    def lambda_217C():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_217C)
    WaitChrThread(0x13, 0x1)

    def lambda_219C():
        OP_8E(0xFE, 0xFFFF8F58, 0x0, 0x8F20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_219C)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 45, 400)
    Sleep(500)
    Return()

    # Function_16_215F end

    def Function_17_21C3(): pass

    label("Function_17_21C3")

    OP_8C(0x12, 220, 500)

    def lambda_21D0():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21D0)
    WaitChrThread(0x12, 0x1)

    def lambda_21F0():
        OP_8E(0xFE, 0xFFFF8A80, 0xFFFFFE0C, 0x86C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21F0)
    Sleep(100)

    def lambda_2210():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2210)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_17_21C3 end

    def Function_18_2222(): pass

    label("Function_18_2222")

    Sleep(500)
    OP_8C(0x13, 220, 500)

    def lambda_2234():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2234)
    WaitChrThread(0x13, 0x1)

    def lambda_2254():
        OP_8E(0xFE, 0xFFFF8A80, 0xFFFFFE0C, 0x86C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2254)
    Sleep(100)

    def lambda_2274():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2274)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_18_2222 end

    SaveToFile()

Try(main)
