from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4140   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4140.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '夏伊',                                 # 9
        '史帕德',                               # 10
        '塞森',                                 # 11
        '多姆',                                 # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_23A",          # 03, 3
        "Function_4_23F",          # 04, 4
        "Function_5_318",          # 05, 5
        "Function_6_31D",          # 06, 6
        "Function_7_476",          # 07, 7
        "Function_8_47B",          # 08, 8
        "Function_9_521",          # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)

    label("loc_1F3")

    Return()

    # Function_0_1BE end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    OP_64(0x2, 0x1)

    label("loc_215")

    Return()

    # Function_1_1F4 end

    def Function_2_216(): pass

    label("Function_2_216")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_239")
    OP_8D(0x9, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_216")

    label("loc_239")

    Return()

    # Function_2_216 end

    def Function_3_23A(): pass

    label("Function_3_23A")

    Call(0, 4)
    Return()

    # Function_3_23A end

    def Function_4_23F(): pass

    label("Function_4_23F")

    TalkBegin(0xA)
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    OP_A9(0xC8)
    TalkEnd(0xA)
    Return()

    label("loc_25C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D")
    TalkEnd(0xA)
    Return()

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2C1")

    ChrTalk(    #0
        0xA,
        (
            "这是怎么了？\x01",
            "这么惊惶失措的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "我们的店可不会逃避。\x01",
            "好好看着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_314")

    ChrTalk(    #2
        0xA,
        (
            "最近在晚上\x01",
            "南街区的店也在营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        (
            "也是，只要能赚钱，\x01",
            "多辛苦都正常。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_314")

    TalkEnd(0xA)
    Return()

    # Function_4_23F end

    def Function_5_318(): pass

    label("Function_5_318")

    Call(0, 6)
    Return()

    # Function_5_318 end

    def Function_6_31D(): pass

    label("Function_6_31D")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_342")
    OP_A9(0xDA)
    Jump("loc_344")

    label("loc_342")

    OP_A9(0xC9)

    label("loc_344")

    TalkEnd(0x8)
    Return()

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C")
    TalkEnd(0x8)
    Return()

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_3C6")

    ChrTalk(    #4
        0x8,
        (
            "哼，受不了了。\x01",
            "还是要离家出走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "啊……对、对不起。\x01",
            "欢迎！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472")

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451")

    ChrTalk(    #7
        0x8,
        (
            "哈……\x01",
            "我和丈夫大吵了一架。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "虽然这么说，不过他根本就不说话，\x01",
            "都是我一个人在上窜下跳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "感觉好空虚……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_472")

    label("loc_451")


    ChrTalk(    #10
        0x8,
        (
            "对他来说\x01",
            "我根本就不重要……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472")

    TalkEnd(0x8)
    Return()

    # Function_6_31D end

    def Function_7_476(): pass

    label("Function_7_476")

    Call(0, 8)
    Return()

    # Function_7_476 end

    def Function_8_47B(): pass

    label("Function_8_47B")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_4C9")

    ChrTalk(    #11
        0xB,
        (
            "可能是因为夜晚的\x01",
            "黑暗，可以集中精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xB,
        "好，加油修理吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_51D")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(    #13
        0xB,
        (
            "呼，这可难办了……\x01",
            "结晶回路好像短路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        "把这儿这么弄一下……嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_51D")

    TalkEnd(0xB)
    Return()

    # Function_8_47B end

    def Function_9_521(): pass

    label("Function_9_521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_593")

    ChrTalk(    #15
        0xFE,
        (
            "和妻子吵架了，\x01",
            "她没给我做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "没办法我只能做了\x01",
            "意大利面来吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "可这更加\x01",
            "激怒了她……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_655")

    label("loc_593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_619")

    ChrTalk(    #18
        0xFE,
        (
            "关于店里的事，\x01",
            "我想和妻子谈谈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "可因为一点小事\x01",
            "激怒了她……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "我就默不作声，\x01",
            "所以她以为我不想谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_655")

    label("loc_619")


    ChrTalk(    #21
        0xFE,
        (
            "我绝不是\x01",
            "不关心妻子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "可我不知道\x01",
            "该说什么好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655")

    TalkEnd(0xFE)
    Return()

    # Function_9_521 end

    SaveToFile()

Try(main)
