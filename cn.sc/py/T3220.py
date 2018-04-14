from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3220   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3220.x',
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
        '希玛',                                 # 9
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
        'ED6_DT07/CH01020 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
    )

    DeclNpc(
        X                   = 2550,
        Z                   = 250,
        Y                   = 4470,
        Direction           = 192,
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
        TriggerX            = 2440,
        TriggerZ            = 250,
        TriggerY            = 2960,
        TriggerRange        = 400,
        ActorX              = 2550,
        ActorZ              = 1750,
        ActorY              = 4470,
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
    OP_A9(0xA0)
    TalkEnd(0x8)
    Return()

    label("loc_11A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B")
    TalkEnd(0x8)
    Return()

    label("loc_12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF")

    ChrTalk(    #0
        0x8,
        (
            "温泉的泵\x01",
            "好像顺利恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "果然是中央工房的工程师\x01",
            "修好的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "真希望也能顺便修\x01",
            "一下我们的照明啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1F5")

    label("loc_1AF")


    ChrTalk(    #3
        0x8,
        (
            "温泉的泵\x01",
            "好像顺利恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "果然是中央工房的工程师\x01",
            "修好的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5")

    Jump("loc_723")

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9")

    ChrTalk(    #5
        0x8,
        "呀，欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "定期船好像停了，\x01",
            "现在客人很少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "你们可能知道，\x01",
            "我还有个很小的儿子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "靠我这个男人\x01",
            "养活他有多辛苦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "……所以啊，\x01",
            "请你们买点什么吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_32E")

    label("loc_2B9")


    ChrTalk(    #10
        0x8,
        (
            "你们可能知道，\x01",
            "我还有个很小的儿子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "靠我这个男人\x01",
            "养活他有多辛苦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "……所以啊，\x01",
            "请你们买点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E")

    Jump("loc_723")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_43F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_39C")

    ChrTalk(    #13
        0x8,
        (
            "只要有温泉疗养的客人来，\x01",
            "我家就能过得去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "我会尽量细水常流地\x01",
            "努力到库安长大的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C")

    label("loc_39C")


    ChrTalk(    #15
        0x8,
        (
            "呼，真没办法……\x01",
            "听说水温恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "暂且可以放心了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "只要有温泉疗养的客人来，\x01",
            "我家就能过得去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "我会尽量细水常流地\x01",
            "努力到库安长大的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_43C")

    Jump("loc_723")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_52B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4AA")

    ChrTalk(    #19
        0x8,
        (
            "我们的店就好像是靠着\x01",
            "温泉疗养生意过活的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "如果温泉不行了，\x01",
            "那就等着关门打烊吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_528")

    label("loc_4AA")


    ChrTalk(    #21
        0x8,
        (
            "如果温泉不行了，\x01",
            "那就等着关门打烊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "拜托你们了，\x01",
            "赶快想想办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "我们的店就好像是靠着\x01",
            "温泉疗养生意过活的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_528")

    Jump("loc_723")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_59E")

    ChrTalk(    #24
        0x8,
        (
            "据说互不侵犯条约的签字仪式\x01",
            "就要在艾尔贝离宫举行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "反正和我们这些平民\x01",
            "也没什么关系……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_636")

    label("loc_59E")


    ChrTalk(    #26
        0x8,
        (
            "因为最近店里比较闲，\x01",
            "就经常读利贝尔通讯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "据说互不侵犯条约的签字仪式很快\x01",
            "就要在艾尔贝离宫举行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "反正和我们这些平民\x01",
            "也没什么关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_636")

    Jump("loc_723")

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_693")

    ChrTalk(    #29
        0x8,
        (
            "有新商品进来了，\x01",
            "需要的话请看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "很适合当作旅游的纪念品哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_723")

    label("loc_693")


    ChrTalk(    #31
        0x8,
        (
            "啊啊…\x01",
            "欢迎欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "有新商品进来了，\x01",
            "需要的话请看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "不过客人还真少啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "库安那小鬼不知道有没有\x01",
            "好好地在外面招揽顾客。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_723")

    TalkEnd(0x8)
    Return()

    # Function_3_FD end

    SaveToFile()

Try(main)
