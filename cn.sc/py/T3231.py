from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3231   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3231.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '莉西亚',                               # 9
        '阿尔宾',                               # 10
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
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -580,
        Z                   = 0,
        Y                   = -5020,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = 0,
        TriggerY            = 5070,
        TriggerRange        = 800,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = 5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1890,
        TriggerZ            = 0,
        TriggerY            = -4990,
        TriggerRange        = 800,
        ActorX              = -1890,
        ActorZ              = 1000,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_18A",          # 01, 1
        "Function_2_1D1",          # 02, 2
        "Function_3_1F5",          # 03, 3
        "Function_4_744",          # 04, 4
        "Function_5_8F1",          # 05, 5
        "Function_6_AF3",          # 06, 6
        "Function_7_CFB",          # 07, 7
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16E")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_16B")
    SetChrPos(0x9, -1110, 0, -3330, 90)

    label("loc_16B")

    Jump("loc_189")

    label("loc_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17D")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_189")

    label("loc_17D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_189")
    ClearChrFlags(0x8, 0x80)

    label("loc_189")

    Return()

    # Function_0_142 end

    def Function_1_18A(): pass

    label("Function_1_18A")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)

    label("loc_1D0")

    Return()

    # Function_1_18A end

    def Function_2_1D1(): pass

    label("Function_2_1D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F4")
    OP_8D(0xFE, -1080, -1680, 1450, 3260, 2000)
    Jump("Function_2_1D1")

    label("loc_1F4")

    Return()

    # Function_2_1D1 end

    def Function_3_1F5(): pass

    label("Function_3_1F5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_268")

    ChrTalk(    #0
        0x8,
        (
            "我只是在打扫的时候\x01",
            "顺便确认了一下水温哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "我、我可没偷懒。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE")

    label("loc_268")


    ChrTalk(    #2
        0x8,
        (
            "哇～这水不错。\x01",
            "看来温泉已经没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "好，得继续打扫了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2AE")

    Jump("loc_36D")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_36D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30B")

    ChrTalk(    #4
        0x8,
        "我来室内浴场打扫了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "不过这里水蒸气太厉害，\x01",
            "什么也看不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_30B")


    ChrTalk(    #6
        0x8,
        "我来室内浴场打扫了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "不过这里水蒸气太厉害，\x01",
            "什么也看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "这是怎么回事呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_36D")

    Jump("loc_41E")

    label("loc_370")

    TurnDirection(0xFE, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE")

    ChrTalk(    #9
        0x8,
        (
            "对不起，奥利维尔大人～\x01",
            "您难得来却不能泡温泉～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "不知道为什么，\x01",
            "澡堂的水沸腾起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E")

    label("loc_3DE")


    ChrTalk(    #11
        0x8,
        (
            "啊～还是\x01",
            "奥利维尔大人优秀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "哎呀～请把我\x01",
            "拐去帝都吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E")

    Jump("loc_740")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")

    ChrTalk(    #13
        0x8,
        "我来室内浴场打扫了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "进了更衣室就会因为有很厉害的\x01",
            "水蒸气而什么都看不见……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E5")

    label("loc_483")


    ChrTalk(    #15
        0x8,
        (
            "反正也是闲着，就开始\x01",
            "打工了，打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "不过都是一些上了年纪的客人，\x01",
            "不太有干劲啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B8")

    ChrTalk(    #17
        0x8,
        "……咦？啊、啊？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #18
        0x8,
        "呀～！？　这不是奥利维尔大人么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "我真高兴～！\x01",
            "您又来啦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1004F（奥、奥利维尔大人～？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031F呵呵，好久不见。\x01",
            "还乖吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691")

    label("loc_5B8")

    TurnDirection(0x8, 0x104, 500)

    ChrTalk(    #22
        0x8,
        "……咦？啊、啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "那、那边是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x104,
        (
            "#031F呵呵，好久不见。\x01",
            "还乖吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #25
        0x8,
        (
            "呀～！？\x01",
            "果然是奥利维尔大人！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "我真高兴～！\x01",
            "您又来啦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F（奥、奥利维尔大人～？）\x02",
    )

    CloseMessageWindow()

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F4")

    ChrTalk(    #28
        0x8,
        (
            "对不起，奥利维尔大人～\x01",
            "现在还不能洗澡～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "不知道为什么，\x01",
            "澡堂的水沸腾起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_6F4")


    ChrTalk(    #30
        0x8,
        (
            "奥利维尔先生～\x01",
            "这次要再唱歌给我听哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "您弹琴的样子\x01",
            "最帅了㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A")

    OP_A2(0x1430)
    OP_A2(0x0)

    label("loc_740")

    TalkEnd(0x8)
    Return()

    # Function_3_1F5 end

    def Function_4_744(): pass

    label("Function_4_744")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A8")

    ChrTalk(    #32
        0xFE,
        (
            "呀～～结婚仪式\x01",
            "头把澡是特别的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "哈哈，也不枉我在这里\x01",
            "苦苦等待了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_7F6")

    label("loc_7A8")


    ChrTalk(    #34
        0xFE,
        (
            "呀～～结婚仪式\x01",
            "头把澡是特别的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "好了，先休息一下\x01",
            "然后再泡个回头澡！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F6")

    Jump("loc_8ED")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89F")

    ChrTalk(    #36
        0xFE,
        (
            "泵出了故障，\x01",
            "澡堂好像不能用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "不过都到了这里，\x01",
            "我怎么能不泡温泉呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "我会一直在这里\x01",
            "等到能用为止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "……阻止我也是没用的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_8ED")

    label("loc_89F")


    ChrTalk(    #40
        0xFE,
        (
            "都到了亚尔摩了，\x01",
            "我怎么能不泡温泉呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "我会一直在这里\x01",
            "等到能用为止。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    TalkEnd(0xFE)
    Return()

    # Function_4_744 end

    def Function_5_8F1(): pass

    label("Function_5_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_8FF")
    Call(0, 7)
    Jump("loc_AEF")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_970")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05发现门上有块牌子。\x01",
            "『因为泵装置出现故障，\x01",
            "　温泉暂停开放』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_AEF")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A86")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #43
        (
            "\x07\x05发现门上有块牌子。\x01",
            "『因为温泉处于沸腾状态，\x01",
            "　暂时禁止进入』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A39")

    ChrTalk(    #44
        0x103,
        (
            "#020F要泡温泉就得\x01",
            "想办法解决洗澡水的沸腾问题。\x02\x03",

            "赶快去后面的栅门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A83")

    label("loc_A39")


    ChrTalk(    #45
        0x106,
        (
            "#050F要泡温泉就得\x01",
            "想办法解决洗澡水的沸腾问题。\x02\x03",

            "赶快去后面的栅门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A83")

    Jump("loc_AEF")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A98")
    Call(0, 7)
    Jump("loc_AEF")

    label("loc_A98")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #46
        (
            "\x07\x05『女澡堂』\x01",
            "　需要使用时\x01",
            "　请到服务台申请。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_AEF")

    TalkEnd(0xFF)
    Return()

    # Function_5_8F1 end

    def Function_6_AF3(): pass

    label("Function_6_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_B04")
    OP_A2(0x3)
    Call(0, 7)
    Jump("loc_CF7")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B75")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #47
        (
            "\x07\x05发现门上有块牌子。\x01",
            "『因为泵装置出现故障，\x01",
            "　温泉暂停开放』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_CF7")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x05发现门上有块牌子。\x01",
            "『因为温泉处于沸腾状态，\x01",
            "　暂时禁止进入』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #49
        0x103,
        (
            "#020F要泡温泉就得\x01",
            "想办法解决洗澡水的沸腾问题。\x02\x03",

            "赶快去后面的栅门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C88")

    label("loc_C3E")


    ChrTalk(    #50
        0x106,
        (
            "#050F要泡温泉就得\x01",
            "想办法解决洗澡水的沸腾问题。\x02\x03",

            "赶快去后面的栅门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C88")

    Jump("loc_CF7")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CA0")
    OP_A2(0x3)
    Call(0, 7)
    Jump("loc_CF7")

    label("loc_CA0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05『男澡堂』\x01",
            "　需要使用时\x01",
            "　请到服务台申请。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_CF7")

    TalkEnd(0xFF)
    Return()

    # Function_6_AF3 end

    def Function_7_CFB(): pass

    label("Function_7_CFB")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "洗澡\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D56"),
        (1, "loc_F80"),
        (SWITCH_DEFAULT, "loc_F83"),
    )


    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D73")
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1D)
    Sleep(200)
    Jump("loc_D86")

    label("loc_D73")

    OP_6F(0x8, 0)
    OP_70(0x8, 0x1D)
    Sleep(200)

    label("loc_D86")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Sleep(600)
    OP_22(0xA2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xB, 0x0, 0x64)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E4A")
    SetChrPos(0x0, -1000, 0, -5090, 90)
    SetChrPos(0x1, -1000, 0, -5090, 90)
    SetChrPos(0x2, -1000, 0, -5090, 90)
    SetChrPos(0x3, -1000, 0, -5090, 90)
    SetChrPos(0x4, -1000, 0, -5090, 90)
    SetChrPos(0x5, -1000, 0, -5090, 90)
    SetChrPos(0x6, -1000, 0, -5090, 90)
    SetChrPos(0x7, -1000, 0, -5090, 90)
    Jump("loc_ED2")

    label("loc_E4A")

    SetChrPos(0x0, -1000, 0, 4900, 90)
    SetChrPos(0x1, -1000, 0, 4900, 90)
    SetChrPos(0x2, -1000, 0, 4900, 90)
    SetChrPos(0x3, -1000, 0, 4900, 90)
    SetChrPos(0x4, -1000, 0, 4900, 90)
    SetChrPos(0x5, -1000, 0, 4900, 90)
    SetChrPos(0x6, -1000, 0, 4900, 90)
    SetChrPos(0x7, -1000, 0, 4900, 90)

    label("loc_ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE5")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_EE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF8")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0B")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_F0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1E")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F31")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_F31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F44")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_F44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F57")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_F57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6A")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_F6A")

    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_F86")

    label("loc_F80")

    Jump("loc_F86")

    label("loc_F83")

    Jump("loc_F86")

    label("loc_F86")

    OP_A3(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_7_CFB end

    SaveToFile()

Try(main)
