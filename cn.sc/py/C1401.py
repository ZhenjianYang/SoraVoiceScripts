from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        '',                                     # 9
        '士兵拉凯尔',                           # 10
        '士兵古特',                             # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH11170 ._CH',             # 00
        'ED6_DT09/CH11171 ._CH',             # 01
        'ED6_DT09/CH11180 ._CH',             # 02
        'ED6_DT09/CH11181 ._CH',             # 03
        'ED6_DT09/CH11190 ._CH',             # 04
        'ED6_DT09/CH11191 ._CH',             # 05
        'ED6_DT09/CH10170 ._CH',             # 06
        'ED6_DT09/CH10171 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT09/CH11170P._CP',             # 00
        'ED6_DT09/CH11171P._CP',             # 01
        'ED6_DT09/CH11180P._CP',             # 02
        'ED6_DT09/CH11181P._CP',             # 03
        'ED6_DT09/CH11190P._CP',             # 04
        'ED6_DT09/CH11191P._CP',             # 05
        'ED6_DT09/CH10170P._CP',             # 06
        'ED6_DT09/CH10171P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
    )

    DeclNpc(
        X                   = 19810,
        Z                   = 0,
        Y                   = 166800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 860,
        Z                   = -1910,
        Y                   = 188180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4130,
        Z                   = -1910,
        Y                   = 188050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclMonster(
        X                   = -31230,
        Z                   = -30,
        Y                   = 76720,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21980,
        Z                   = -30,
        Y                   = 47990,
        Unknown_0C          = 38,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2600,
        Z                   = 10,
        Y                   = 79910,
        Unknown_0C          = 219,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7230,
        Z                   = -1190,
        Y                   = 93200,
        Unknown_0C          = 285,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = -1960,
        Y                   = 58080,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = -1990,
        Y                   = 103160,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4790,
        Z                   = -1950,
        Y                   = 141270,
        Unknown_0C          = 252,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10740,
        Z                   = -2009,
        Y                   = 162000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8460,
        Z                   = -2020,
        Y                   = 79300,
        Unknown_0C          = 280,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21780,
        Z                   = -2050,
        Y                   = 78280,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 920,
        Y                   = -3000,
        Z                   = 189170,
        Range               = 4030,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2E180,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 19360,
        TriggerZ            = -1990,
        TriggerY            = 166110,
        TriggerRange        = 1000,
        ActorX              = 19810,
        ActorZ              = -490,
        ActorY              = 166800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BE",          # 00, 0
        "Function_1_2BF",          # 01, 1
        "Function_2_2F9",          # 02, 2
        "Function_3_476",          # 03, 3
        "Function_4_772",          # 04, 4
        "Function_5_B58",          # 05, 5
        "Function_6_D28",          # 06, 6
    )


    def Function_0_2BE(): pass

    label("Function_0_2BE")

    Return()

    # Function_0_2BE end

    def Function_1_2BF(): pass

    label("Function_1_2BF")

    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x2, 0)
    Jump("loc_2F3")

    label("loc_2EC")

    OP_6F(0x2, 60)

    label("loc_2F3")

    OP_71(0x1, 0x4)
    Return()

    # Function_1_2BF end

    def Function_2_2F9(): pass

    label("Function_2_2F9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_460")

    label("loc_31E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_460")

    label("loc_337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_460")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_460")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_460")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_460")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_460")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_460")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_460")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_460")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_460")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_460")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_460")

    label("loc_44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_460")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_460")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_460")

    label("loc_475")

    Return()

    # Function_2_2F9 end

    def Function_3_476(): pass

    label("Function_3_476")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_572")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515")

    ChrTalk(    #0
        0xFE,
        (
            "听说哈肯大门那边\x01",
            "现在的情况非常紧张。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "好像是国境的大门一直开着，\x01",
            "没有办法关上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "国、国境师团的士兵们\x01",
            "这下可不得了了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_56F")

    label("loc_515")


    ChrTalk(    #3
        0xFE,
        (
            "听说哈肯大门那边\x01",
            "现在的情况非常紧张。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "好像是国境的大门一直开着，\x01",
            "没有办法关上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F")

    Jump("loc_76E")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C2")

    ChrTalk(    #5
        0xFE,
        (
            "啊，不好意思，这里\x01",
            "现在还是禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "请回去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5E1")

    label("loc_5C2")


    ChrTalk(    #7
        0xFE,
        (
            "这里禁止入内。\x01",
            "请回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E1")

    Jump("loc_76E")

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_655")

    ChrTalk(    #8
        0xFE,
        (
            "结果最后好像还是无法将\x01",
            "那条龙捕获呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "居然要倾尽王国军\x01",
            "的全部力量来围剿，\x01",
            "真是可怕的生物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_69D")

    ChrTalk(    #10
        0xFE,
        (
            "总觉得龙还潜藏在\x01",
            "附近呢，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "拜、拜托了\x01",
            "不要来这里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_76E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6D9")

    ChrTalk(    #12
        0xFE,
        (
            "这里禁止入内的。\x01",
            "请老老实实地回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E")

    label("loc_6D9")


    ChrTalk(    #13
        0xFE,
        "啊，你们是旅行者吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "不好意思，这里\x01",
            "现在禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "自从空贼艇被抢走之后，\x01",
            "这里的警备就\x01",
            "更加森严了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "不要给我们\x01",
            "添太多麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_76E")

    TalkEnd(0x9)
    Return()

    # Function_3_476 end

    def Function_4_772(): pass

    label("Function_4_772")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_88A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")

    ChrTalk(    #17
        0xFE,
        (
            "哈肯大门那边的情况\x01",
            "好像也不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "毕竟才刚签署完互不侵犯条约，\x01",
            "我想帝国应该不会乱来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "话虽然是这么说，\x01",
            "但是战争这种事情谁也说不准的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_887")

    label("loc_823")


    ChrTalk(    #20
        0xFE,
        (
            "哈肯大门那边的情况\x01",
            "好像也不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "毕竟才刚签署完互不侵犯条约，\x01",
            "我想帝国应该不会乱来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_887")

    Jump("loc_B54")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(    #22
        0xFE,
        (
            "再往前就是王国军的训练设施，\x01",
            "禁止民间人士入内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "不好意思，\x01",
            "还是请你们离开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_922")

    label("loc_8F7")


    ChrTalk(    #24
        0xFE,
        (
            "禁止民间人士入内。\x01",
            "还是请你们离开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_922")

    Jump("loc_B54")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_990")

    ChrTalk(    #25
        0xFE,
        (
            "这里几乎没有人\x01",
            "会来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "所以最主要的工作\x01",
            "就是别让自己睡着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A09")

    label("loc_990")


    ChrTalk(    #28
        0xFE,
        (
            "哎呀呀，龙的骚乱事件\x01",
            "似乎也已经平息了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "恢复和平固然是很好，\x01",
            "但日子又开始变得无聊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A09")

    Jump("loc_B54")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A72")

    ChrTalk(    #31
        0xFE,
        (
            "迷雾峡谷的西部\x01",
            "在地图中也都没有标识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "误闯进去的话非常危险，\x01",
            "所以平时都把桥撤掉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_ABC")

    ChrTalk(    #33
        0xFE,
        (
            "前面禁止民间人士\x01",
            "进入了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "不好意思，请回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_ABC")


    ChrTalk(    #35
        0xFE,
        (
            "自从遭到空贼团的入侵之后，\x01",
            "这里的警备就更加森严了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "所以说，\x01",
            "现在这里禁止民间人士入内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "连猫也不能放进去一只，\x01",
            "这是队长下达的死命令。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B54")

    TalkEnd(0xA)
    Return()

    # Function_4_772 end

    def Function_5_B58(): pass

    label("Function_5_B58")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_BAA():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BAA)

    def lambda_BC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BC5)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #38
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xBA, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C12"),
        (2, "loc_C24"),
        (1, "loc_C34"),
        (SWITCH_DEFAULT, "loc_C37"),
    )


    label("loc_C12")

    OP_A2(0x1B17)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_C37")

    label("loc_C24")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C34")

    OP_B4(0x0)
    Return()

    label("loc_C37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A2, 1)"), scpexpr(EXPR_END)), "loc_C86")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #39
        "\x07\x00得到了\x1F\xA2\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B16)
    Jump("loc_CE8")

    label("loc_C86")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
        (
            "宝箱里装有\x1F\xA2\x02\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xA2\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_CE8")

    Jump("loc_D1A")

    label("loc_CEB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #41
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D1A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B58 end

    def Function_6_D28(): pass

    label("Function_6_D28")

    EventBegin(0x1)
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #42
        0xA,
        (
            "这里禁止\x01",
            "民间人士进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "不好意思，请回去吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8C(0xA, 180, 400)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_D28 end

    SaveToFile()

Try(main)
