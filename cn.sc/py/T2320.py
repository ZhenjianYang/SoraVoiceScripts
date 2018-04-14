from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2320   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2320.x',
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
        '珂蕾妲婆婆',                           # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 500,
        Y                   = 8800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -4040,
        TriggerZ            = 500,
        TriggerY            = 7530,
        TriggerRange        = 400,
        ActorX              = -4000,
        ActorZ              = 2000,
        ActorY              = 8800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_F8",           # 02, 2
        "Function_3_FD",           # 03, 3
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Return()

    # Function_1_F7 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    Call(0, 3)
    Return()

    # Function_2_F8 end

    def Function_3_FD(): pass

    label("Function_3_FD")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A")
    OP_A9(0x6E)
    TalkEnd(0x8)
    Return()

    label("loc_11A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B")
    TalkEnd(0x8)
    Return()

    label("loc_12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF")

    ChrTalk(    #0
        0x8,
        (
            "最近有年轻人\x01",
            "来学料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "以前的烹调法\x01",
            "只要有个锅就能解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "只用暖炉的火\x01",
            "就能做简单的料理了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1F1")

    label("loc_1AF")


    ChrTalk(    #3
        0x8,
        (
            "最近有年轻人\x01",
            "来学料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "大家好像\x01",
            "都不知道火的用法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1")

    Jump("loc_51D")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286")

    ChrTalk(    #5
        0x8,
        (
            "没有导力器\x01",
            "我倒不会感到为难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "放点柴火就能取暖，\x01",
            "照明用油灯也足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "为什么大家那么紧张\x01",
            "我真是完全不明白哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2D6")

    label("loc_286")


    ChrTalk(    #8
        0x8,
        (
            "没有导力器\x01",
            "我倒不会感到为难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "为什么大家那么紧张\x01",
            "我真是完全不明白哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6")

    Jump("loc_51D")

    label("loc_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_33E")

    ChrTalk(    #10
        0x8,
        (
            "选举最重要的\x01",
            "就是候选人的人品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "以前就是失败在这里，\x01",
            "这次一定要看清楚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391")

    label("loc_33E")

    OP_A2(0x0)

    ChrTalk(    #12
        0x8,
        (
            "选举最重要的\x01",
            "就是候选人的人品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "这里没出问题的话，\x01",
            "应该就万事顺利了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_391")

    Jump("loc_51D")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_470")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FE")

    ChrTalk(    #14
        0x8,
        (
            "扎古有扎古自己\x01",
            "的考虑吧。\x01",
            "行动比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "动口不如动手。\x01",
            "我就是这么教他的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D")

    label("loc_3FE")

    OP_A2(0x0)

    ChrTalk(    #16
        0x8,
        (
            "选举临近了,\x01",
            "村长似乎很忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "相比之下扎古\x01",
            "在干什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "年轻人不工作，\x01",
            "以前可是想都不敢想哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D")

    Jump("loc_51D")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_4BC")

    ChrTalk(    #19
        0x8,
        (
            "我孙女萨蒂在店前\x01",
            "开花店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "不介意的话\x01",
            "也去那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D")

    label("loc_4BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(    #21
        0x8,
        (
            "刚才在前面\x01",
            "碰到巡回神父了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "好像是新上任的神父，\x01",
            "实在太年轻了，让人大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D")

    TalkEnd(0x8)
    Return()

    # Function_3_FD end

    SaveToFile()

Try(main)
