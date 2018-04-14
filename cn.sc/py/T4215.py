from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4215   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4215.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '吉尔维厨师长',                         # 9
        '福鲁克',                               # 10
        '里吉斯',                               # 11
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
        'ED6_DT07/CH01280 ._CH',             # 00
        'ED6_DT07/CH01520 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01280P._CP',             # 00
        'ED6_DT07/CH01520P._CP',             # 01
    )

    DeclNpc(
        X                   = -68800,
        Z                   = 0,
        Y                   = 73020,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -70370,
        Z                   = 0,
        Y                   = 69400,
        Direction           = 356,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -70550,
        Z                   = 0,
        Y                   = 74650,
        Direction           = 173,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_182",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_303",          # 03, 3
        "Function_4_479",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_133")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_181")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13D")
    Jump("loc_181")

    label("loc_13D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_147")
    Jump("loc_181")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_181")
    SetChrPos(0x8, -61660, 0, 68030, 87)
    SetChrPos(0x9, -70230, 0, 65550, 181)
    SetChrPos(0xA, -69850, 0, 77540, 273)

    label("loc_181")

    Return()

    # Function_0_11A end

    def Function_1_182(): pass

    label("Function_1_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E")
    OP_B1("t4215_y")
    Jump("loc_1A7")

    label("loc_19E")

    OP_B1("t4215_n")

    label("loc_1A7")

    Return()

    # Function_1_182 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22E")

    ChrTalk(    #0
        0xFE,
        (
            "用炭火和暖炉烹调也\x01",
            "别有风味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "无法解决的问题恐怕\x01",
            "就是费时这一点了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "看来暂时是没法做出\x01",
            "像样的饭菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF")

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2C3")

    ChrTalk(    #3
        0xFE,
        (
            "在离宫进行的签字仪式上\x01",
            "将会举办宴会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "我正在搭配\x01",
            "餐室的菜单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "为了使条约的签字顺利进行，\x01",
            "我会竭尽自己的的力量认真工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2FF")

    ChrTalk(    #6
        0xFE,
        (
            "祝科洛蒂娅殿下\x01",
            "心情愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "您来这里有事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2FF")

    TalkEnd(0xFE)
    Return()

    # Function_2_1A8 end

    def Function_3_303(): pass

    label("Function_3_303")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_36E")

    ChrTalk(    #8
        0xFE,
        (
            "签字仪式的宴会\x01",
            "获得了相当的好评哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "每个国家的代表都很高兴地\x01",
            "品尝了厨师长做的菜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_475")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_425")

    ChrTalk(    #10
        0xFE,
        (
            "在签字仪式当日的前一天他\x01",
            "就去离宫进行烹调了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "因为有很多大人物要来，\x01",
            "必须好好地管理食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "要是出现食物中毒那就是国际问题了，\x01",
            "最重要的是这关系到厨师的名声……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_475")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_475")

    ChrTalk(    #13
        0xFE,
        (
            "厨师长会做上千种菜，\x01",
            "确实是个了不起的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "我必须好好跟着学……\x02",
    )

    CloseMessageWindow()

    label("loc_475")

    TalkEnd(0xFE)
    Return()

    # Function_3_303 end

    def Function_4_479(): pass

    label("Function_4_479")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4DC")

    ChrTalk(    #15
        0xFE,
        (
            "如果仅仅是烫和煮的话\x01",
            "用火也没有问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "火候的掌握果然\x01",
            "不像用导力器那么方便。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58F")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_515")

    ChrTalk(    #17
        0xFE,
        (
            "嗯……不能\x01",
            "漏买东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "接下来要忙了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_58F")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_58F")

    ChrTalk(    #19
        0xFE,
        (
            "下水道的门关上了之后\x01",
            "储藏室的老鼠总算少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "真是的，真受不了\x01",
            "那些咬坏别人辛辛苦苦\x01",
            "搬运进去的食品的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F")

    TalkEnd(0xFE)
    Return()

    # Function_4_479 end

    SaveToFile()

Try(main)
