from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1100   ._SN',
        MapName             = 'Bose',
        Location            = 'T1100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 1,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1100_1 ._SN',
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
        '马尔科',                               # 9
        '蒙提',                                 # 10
        '法娜',                                 # 11
        '阿尔贝尔',                             # 12
        '西蒙',                                 # 13
        '王国军士兵',                           # 14
        '莉咏',                                 # 15
        '莫德娜',                               # 16
        '安赛尔新街方向',                       # 17
        '柏斯市·北街区',                       # 18
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT07/CH01690 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT26/CH20311 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT07/CH01690P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT26/CH20311P._CP',             # 08
    )

    DeclNpc(
        X                   = 50000,
        Z                   = -3000,
        Y                   = 31800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = -3000,
        Y                   = 30480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51870,
        Z                   = -3000,
        Y                   = 30650,
        Direction           = 43,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 52830,
        Z                   = -3000,
        Y                   = 32950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 51780,
        Z                   = -3000,
        Y                   = 32900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 44410,
        Z                   = -3000,
        Y                   = 20760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44380,
        Z                   = -3000,
        Y                   = 29520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 43530,
        Z                   = -3000,
        Y                   = 30940,
        Direction           = 122,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 47970,
        Z                   = -3000,
        Y                   = 4220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48070,
        Z                   = 0,
        Y                   = 48590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 53090,
        Y                   = -3000,
        Z                   = 20940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 55320,
        Y                   = -3000,
        Z                   = 33040,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 65140,
        TriggerZ            = 3000,
        TriggerY            = 36680,
        TriggerRange        = 1000,
        ActorX              = 65280,
        ActorZ              = 5000,
        ActorY              = 36680,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_296",          # 00, 0
        "Function_1_326",          # 01, 1
        "Function_2_390",          # 02, 2
        "Function_3_3F1",          # 03, 3
        "Function_4_47E",          # 04, 4
        "Function_5_559",          # 05, 5
        "Function_6_868",          # 06, 6
        "Function_7_B4B",          # 07, 7
        "Function_8_C27",          # 08, 8
        "Function_9_CDD",          # 09, 9
        "Function_10_DB5",         # 0A, 10
        "Function_11_F2E",         # 0B, 11
        "Function_12_14BC",        # 0C, 12
        "Function_13_14C0",        # 0D, 13
    )


    def Function_0_296(): pass

    label("Function_0_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2BD")
    ClearChrFlags(0xA, 0x80)

    label("loc_2BD")

    Jump("loc_325")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_325")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2ED")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_325")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2FC")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_325")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_325")
    SetChrPos(0x8, 50940, -3000, 31530, 0)
    SetChrPos(0x9, 49760, -3000, 30480, 0)

    label("loc_325")

    Return()

    # Function_0_296 end

    def Function_1_326(): pass

    label("Function_1_326")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFE7960, 0x230040)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_342")
    Jump("loc_35B")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_35B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x1)
    OP_10(0x11, 0x1)

    label("loc_35B")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37E")
    OP_65(0x0, 0x1)

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F")
    OP_1B(0xD, 0x0, 0xB)

    label("loc_38F")

    Return()

    # Function_1_326 end

    def Function_2_390(): pass

    label("Function_2_390")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3ED")

    ChrTalk(    #0
        0xFE,
        (
            "博尔德先生的太太\x01",
            "好像去了超市了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "总算是重新\x01",
            "开始营业了，\x01",
            "去买些东西吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED")

    TalkEnd(0xF)
    Return()

    # Function_2_390 end

    def Function_3_3F1(): pass

    label("Function_3_3F1")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_47A")

    ChrTalk(    #2
        0xFE,
        (
            "平静的日子\x01",
            "终于回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "定期船也恢复航行了，\x01",
            "商业上的竞争现在才要开始！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "买、买东西的时候\x01",
            "本应该忘记那些事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A")

    TalkEnd(0xE)
    Return()

    # Function_3_3F1 end

    def Function_4_47E(): pass

    label("Function_4_47E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4FE")

    ChrTalk(    #5
        0xFE,
        (
            "不过，听说飞行舰队\x01",
            "没有抓到那条龙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "竟然会失败，\x01",
            "真是有点失望啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "警备市街区的我们\x01",
            "也觉得不好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_555")

    ChrTalk(    #8
        0xFE,
        (
            "听说这次龙的骚乱事件\x01",
            "给军队高层带来了很大冲击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "连飞行舰队\x01",
            "都出动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_555")

    TalkEnd(0xFE)
    Return()

    # Function_4_47E end

    def Function_5_559(): pass

    label("Function_5_559")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5C9")

    ChrTalk(    #10
        0xFE,
        (
            "商人对交易要慎重，\x01",
            "到现在也没签署协议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "我也知道在飞船停航的\x01",
            "情况下什么也做不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_5C9")


    ChrTalk(    #12
        0xFE,
        (
            "虽然要\x01",
            "签署协定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "但这种事总要慎重些。\x01",
            "到现在也没签署协议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "我也知道在飞船停航的\x01",
            "情况下什么也做不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "如果商谈不成功的话，\x01",
            "来王国也就没有意义了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_674")

    Jump("loc_864")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #16
        0xFE,
        (
            "超市被袭事件之后，\x01",
            "王国军也开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "但是这一带\x01",
            "距离我们帝国的国境线很近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "希望不要出什么乱子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_729")

    ChrTalk(    #19
        0xFE,
        (
            "北街区的超市似乎\x01",
            "有什么骚动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77E")

    label("loc_729")


    ChrTalk(    #20
        0xFE,
        (
            "北街区的超市似乎\x01",
            "有什么骚动啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "呼，真糟糕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "我才正打算\x01",
            "出去商谈…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_77E")

    Jump("loc_864")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7E2")

    ChrTalk(    #23
        0xFE,
        (
            "第一次来这里的时候\x01",
            "我也迷路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "经过了多次的来往，\x01",
            "也完全熟悉了柏斯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_7E2")


    ChrTalk(    #25
        0xFE,
        (
            "我第一次从帝国来的时候\x01",
            "也迷路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "经过了多次的来往，\x01",
            "也完全熟悉了柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "那么，先在南街区转转，\x01",
            "然后再去超市吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_864")

    TalkEnd(0x8)
    Return()

    # Function_5_559 end

    def Function_6_868(): pass

    label("Function_6_868")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #28
        0xFE,
        (
            "真是的。\x01",
            "商谈还是没有进展。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E8")

    label("loc_89D")


    ChrTalk(    #29
        0xFE,
        (
            "呼，真是的。\x01",
            "商谈还是没有进展。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "来的不是时候，\x01",
            "也只有放弃了…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8E8")

    Jump("loc_B47")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_9D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_956")

    ChrTalk(    #31
        0xFE,
        (
            "帝国军的导力战车\x01",
            "定货量明显减少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "仔细想想，\x01",
            "也许是因为互不侵犯条约的影响吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5")

    label("loc_956")


    ChrTalk(    #33
        0xFE,
        (
            "帝国军的导力战车\x01",
            "定货量明显减少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "仔细想想，\x01",
            "也许是因为互不侵犯条约的影响吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "作为商人，想法还是很复杂的…\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9D5")

    Jump("loc_B47")

    label("loc_9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A23")

    ChrTalk(    #36
        0xFE,
        "超市的被袭事件吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "不管怎么说，\x01",
            "商谈似乎无法继续了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B47")

    label("loc_A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A8C")

    ChrTalk(    #38
        0xFE,
        (
            "即使如此，这里真的是\x01",
            "比我想象中得还发达呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "我们帝国的都市\x01",
            "也未必有这么繁荣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B47")

    label("loc_A8C")


    ChrTalk(    #40
        0xFE,
        (
            "我身为帝国的商人，\x01",
            "也想拓展一下海外的市场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "所以这次才下定决心\x01",
            "来王国进行商谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "多亏前辈马尔科的帮忙，\x01",
            "我才能和这里的商人们联系上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "接下来就希望\x01",
            "商谈能早些达成吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B47")

    TalkEnd(0x9)
    Return()

    # Function_6_868 end

    def Function_7_B4B(): pass

    label("Function_7_B4B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(    #44
        0xFE,
        (
            "这个店一定\x01",
            "希望有个帮手吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "如果和店主商量商量，\x01",
            "一定会被采纳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "……不过，太混乱了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "算了，总之要有\x01",
            "长期作战的准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C23")

    label("loc_BE9")


    ChrTalk(    #48
        0xFE,
        (
            "工房来了\x01",
            "很多客人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "他们应该\x01",
            "人手不足了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C23")

    TalkEnd(0xA)
    Return()

    # Function_7_B4B end

    def Function_8_C27(): pass

    label("Function_8_C27")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40")
    Call(0, 10)
    Jump("loc_C7C")

    label("loc_C40")


    ChrTalk(    #50
        0xFE,
        (
            "前面的客人\x01",
            "是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "进了店以后\x01",
            "这么久也没出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jump("loc_CD9")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9F")
    Call(0, 10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_CD9")

    label("loc_C9F")


    ChrTalk(    #52
        0xFE,
        (
            "昨天晚上我家\x01",
            "非常恐慌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "工房好像也\x01",
            "非常混乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD9")

    TalkEnd(0xB)
    Return()

    # Function_8_C27 end

    def Function_9_CDD(): pass

    label("Function_9_CDD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF6")
    Call(0, 10)
    Jump("loc_D3C")

    label("loc_CF6")


    ChrTalk(    #54
        0xFE,
        (
            "接下来就去看看\x01",
            "店里的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "前边的客人\x01",
            "应该已经办完事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3C")

    Jump("loc_DB1")

    label("loc_D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F")
    Call(0, 10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_DB1")

    label("loc_D5F")


    ChrTalk(    #56
        0xFE,
        (
            "现在一到晚上，\x01",
            "我家里就很麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "特里诺家也在找油灯，\x01",
            "把家里都翻了个遍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB1")

    TalkEnd(0xC)
    Return()

    # Function_9_CDD end

    def Function_10_DB5(): pass

    label("Function_10_DB5")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_E99")

    ChrTalk(    #58
        0xC,
        "对了，阿尔贝尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xC,
        (
            "你好像是准备\x01",
            "考进王立学院吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        (
            "嗯，为了准备考试\x01",
            "一直在拼命学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "就算是现在这种状况，\x01",
            "也只有努力克服了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xC,
        "确实如此呢…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xC,
        (
            "导力器全都瘫痪了，\x01",
            "日常生活也受到很大影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(    #64
        0xB,
        "啊，西蒙…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "你也有事\x01",
            "要到工房吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xC,
        (
            "嗯，是米拉诺\x01",
            "让我来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "我的父亲也吩咐过。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "任何一家\x01",
            "似乎都很头疼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x3)
    OP_A2(0x4)
    Return()

    # Function_10_DB5 end

    def Function_11_F2E(): pass

    label("Function_11_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1071")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F97")

    ChrTalk(    #69
        0x108,
        (
            "#074F现在已经\x01",
            "没空乱逛了啊。\x02\x03",

            "#070F在街上买过东西之后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFD")

    label("loc_F97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAD")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_FB4")

    label("loc_FAD")

    TurnDirection(0x103, 0x0, 400)

    label("loc_FB4")


    ChrTalk(    #70
        0x103,
        (
            "#020F现在已经\x01",
            "没时间闲逛了啊。\x02\x03",

            "在街上买完东西以后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFD")

    Fade(1000)
    OP_59()
    SetChrPos(0x101, 47790, -3000, 17080, 0)
    SetChrPos(0x103, 47790, -3000, 17080, 0)
    SetChrPos(0x108, 47790, -3000, 17080, 0)
    SetChrPos(0x105, 47790, -3000, 17080, 0)
    SetChrPos(0x104, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_14BB")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_128E")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_109F"),
        (2, "loc_10DD"),
        (4, "loc_1123"),
        (3, "loc_1165"),
        (6, "loc_11AB"),
        (7, "loc_11F3"),
        (SWITCH_DEFAULT, "loc_1232"),
    )


    label("loc_109F")


    ChrTalk(    #71
        0x101,
        (
            "#1002F不是这条路啦。\x02\x03",

            "准备完毕之后\x01",
            "马上回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_10DD")


    ChrTalk(    #72
        0x103,
        (
            "#022F现在没时间\x01",
            "绕远路了。\x02\x03",

            "准备结束之后\x01",
            "就赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_1123")


    ChrTalk(    #73
        0x105,
        (
            "#042F现在没空\x01",
            "绕远路了。\x02\x03",

            "准备结束之后\x01",
            "赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_1165")


    ChrTalk(    #74
        0x104,
        (
            "#032F现在不是闲逛\x01",
            "的时候啊。\x02\x03",

            "准备完毕之后\x01",
            "赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_11AB")


    ChrTalk(    #75
        0x107,
        (
            "#062F……别再\x01",
            "磨磨蹭蹭的啦。\x02\x03",

            "准备好之后\x01",
            "赶快追上阿加特哥哥吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_11F3")


    ChrTalk(    #76
        0x108,
        (
            "#072F已经没时间乱逛了。\x02\x03",

            "准备好之后\x01",
            "赶快回拉文努村吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1232")

    label("loc_1232")

    Fade(1000)
    OP_59()
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_14BB")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BB")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_12BC"),
        (2, "loc_12FC"),
        (4, "loc_133D"),
        (3, "loc_137E"),
        (6, "loc_13BB"),
        (7, "loc_1427"),
        (SWITCH_DEFAULT, "loc_1462"),
    )


    label("loc_12BC")


    ChrTalk(    #77
        0x101,
        (
            "#1002F现在必须要\x01",
            "赶快到拉文努村…\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_12FC")


    ChrTalk(    #78
        0x103,
        (
            "#022F要去拉文努村的话，\x01",
            "得从西边的出口出去。\x02\x03",

            "快一点吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_133D")


    ChrTalk(    #79
        0x105,
        (
            "#042F拉文努村\x01",
            "位于柏斯的西北方向。\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_137E")


    ChrTalk(    #80
        0x104,
        (
            "#032F拉文努村\x01",
            "是在西北方向呢。\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_13BB")


    ChrTalk(    #81
        0x107,
        (
            "#065F啊啊……\x01",
            "要去拉文努村的话，\x01",
            "应该从西边的出口出去啊。\x02\x03",

            "#062F我们必须要早点\x01",
            "追上阿加特哥哥……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_1427")


    ChrTalk(    #82
        0x108,
        (
            "#072F去拉文努村的话，\x01",
            "要从西边出去，\x02\x03",

            "赶快行动吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1462")

    label("loc_1462")

    Fade(1000)
    OP_59()
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)

    label("loc_14BB")

    Return()

    # Function_11_F2E end

    def Function_12_14BC(): pass

    label("Function_12_14BC")

    SetPlaceName(0x22)
    Return()

    # Function_12_14BC end

    def Function_13_14C0(): pass

    label("Function_13_14C0")

    SetPlaceName(0x24)
    Return()

    # Function_13_14C0 end

    SaveToFile()

Try(main)
