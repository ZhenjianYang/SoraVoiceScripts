from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '贝恩',                                 # 9
        '乌尔斯',                               # 10
        '兰达老人',                             # 11
        '米优',                                 # 12
        '',                                     # 13
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
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
    )

    DeclNpc(
        X                   = -2470,
        Z                   = -1000,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = -1000,
        Y                   = 5320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -450,
        Z                   = -650,
        Y                   = 3980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 50,
        Z                   = -1000,
        Y                   = 8500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 660,
        TriggerZ            = -1000,
        TriggerY            = 6600,
        TriggerRange        = 400,
        ActorX              = 50,
        ActorZ              = 500,
        ActorY              = 8500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1B4",          # 02, 2
        "Function_3_1D8",          # 03, 3
        "Function_4_1DD",          # 04, 4
        "Function_5_2CC",          # 05, 5
        "Function_6_3E0",          # 06, 6
        "Function_7_3E5",          # 07, 7
        "Function_8_4F9",          # 08, 8
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_1B2")

    Return()

    # Function_0_192 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    Return()

    # Function_1_1B3 end

    def Function_2_1B4(): pass

    label("Function_2_1B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D7")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 2000)
    Jump("Function_2_1B4")

    label("loc_1D7")

    Return()

    # Function_2_1B4 end

    def Function_3_1D8(): pass

    label("Function_3_1D8")

    Call(0, 4)
    Return()

    # Function_3_1D8 end

    def Function_4_1DD(): pass

    label("Function_4_1DD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_2C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25B")
    OP_8C(0x10, 90, 0)

    ChrTalk(    #0
        0x10,
        (
            "爷爷，\x01",
            "别那么生气嘛。\x02",
        )
    )

    Jump("loc_21A")

    label("loc_21A")

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "别看艾莉卡那家伙那个样子，\x01",
            "该考虑的东西还是会考虑的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C8")

    label("loc_25B")


    ChrTalk(    #2
        0x10,
        "哦、哦哦，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "前台那边\x01",
            "已经交给新人了。\x02",
        )
    )

    Jump("loc_2A5")

    label("loc_2A5")

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "想点菜的话\x01",
            "就去那边吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2C8")

    TalkEnd(0x10)
    Return()

    # Function_4_1DD end

    def Function_5_2CC(): pass

    label("Function_5_2CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_342")

    ChrTalk(    #5
        0xFE,
        (
            "……哦，\x01",
            "忘记去叫醒露依赛了。\x02",
        )
    )

    Jump("loc_30D")

    label("loc_30D")

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "算了，还有乌缇在。\x01",
            "…………大概没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC")

    label("loc_342")


    ChrTalk(    #7
        0xFE,
        (
            "新来的人\x01",
            "好像是兰达爷爷的孙女呢。\x02",
        )
    )

    Jump("loc_376")

    label("loc_376")

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "料理的本事不错，\x01",
            "似乎也很擅长接待客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "托她的福，\x01",
            "老板偷懒的技术也越来越熟练了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3DC")

    TalkEnd(0xFE)
    Return()

    # Function_5_2CC end

    def Function_6_3E0(): pass

    label("Function_6_3E0")

    Call(0, 7)
    Return()

    # Function_6_3E0 end

    def Function_7_3E5(): pass

    label("Function_7_3E5")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_4F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_491")

    ChrTalk(    #10
        0x13,
        (
            "我只有中午\x01",
            "才会到这家店打工哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        (
            "因为待在中央工房\x01",
            "也都只是做杂事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x13,
        (
            "与其在阴暗的工房当接待，\x01",
            "光鲜亮丽的招牌女郎\x01",
            "不是更适合我吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_491")


    ChrTalk(    #13
        0x13,
        "来了，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "现在本店正在提供\x01",
            "中午的限时优惠哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x13,
        "动心的话就来尝尝吧㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4F5")

    TalkEnd(0x13)
    Return()

    # Function_7_3E5 end

    def Function_8_4F9(): pass

    label("Function_8_4F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_56B")

    ChrTalk(    #16
        0xFE,
        (
            "虽然有丹在，\x01",
            "应该不会出什么大事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "不过那两人做共同研究……\x01",
            "……唉，真担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9")

    label("loc_56B")


    ChrTalk(    #18
        0xFE,
        (
            "拉赛尔那家伙\x01",
            "好像又要开始做什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "而且听说\x01",
            "还和艾莉卡那家伙一起。\x02",
        )
    )

    Jump("loc_5C8")

    label("loc_5C8")

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "唉，\x01",
            "要人不担心真是不可能的了。\x02",
        )
    )

    Jump("loc_5F5")

    label("loc_5F5")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5F9")

    TalkEnd(0xFE)
    Return()

    # Function_8_4F9 end

    SaveToFile()

Try(main)
