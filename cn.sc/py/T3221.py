from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3221_1 ._SN',
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
        '毛婆婆',                               # 9
        '艾缇',                                 # 10
        '赫雷思老人',                           # 11
        '赫雷思老人',                           # 12
        '艾德',                                 # 13
        '莉西亚',                               # 14
        '法尔茨',                               # 15
        '蔡尔德',                               # 16
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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

    DeclNpc(
        X                   = 8490,
        Z                   = 0,
        Y                   = 340,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 14140,
        Z                   = 200,
        Y                   = 2029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2490,
        Z                   = 0,
        Y                   = 40320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -31490,
        Z                   = -250,
        Y                   = 8530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7590,
        Z                   = 0,
        Y                   = 73170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 11190,
        Z                   = 0,
        Y                   = 2440,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 8780,
        Z                   = 200,
        Y                   = 6560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2F8",          # 01, 1
        "Function_2_2F9",          # 02, 2
        "Function_3_2FE",          # 03, 3
        "Function_4_16C4",         # 04, 4
        "Function_5_16C9",         # 05, 5
        "Function_6_1CDF",         # 06, 6
        "Function_7_1EC8",         # 07, 7
        "Function_8_2342",         # 08, 8
        "Function_9_28B1",         # 09, 9
        "Function_10_297B",        # 0A, 10
        "Function_11_2B68",        # 0B, 11
        "Function_12_35EB",        # 0C, 12
        "Function_13_3D9C",        # 0D, 13
        "Function_14_3E26",        # 0E, 14
        "Function_15_3E7F",        # 0F, 15
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28B")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    SetChrPos(0xD, -1150, 0, 40780, 0)
    Jump("loc_288")

    label("loc_283")

    SetChrFlags(0xD, 0x80)

    label("loc_288")

    Jump("loc_2D3")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_29A")
    SetChrFlags(0xD, 0x80)
    Jump("loc_2D3")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2B8")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2D3")

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2CC")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_2D3")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2D3")

    label("loc_2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E9")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_2F7")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2F7")
    OP_A3(0x10F1)
    Event(0, 12)

    label("loc_2F7")

    Return()

    # Function_0_256 end

    def Function_1_2F8(): pass

    label("Function_1_2F8")

    Return()

    # Function_1_2F8 end

    def Function_2_2F9(): pass

    label("Function_2_2F9")

    Call(0, 3)
    Return()

    # Function_2_2F9 end

    def Function_3_2FE(): pass

    label("Function_3_2FE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_335")
    Call(1, 1)
    Jump("loc_339")

    label("loc_335")

    Call(1, 0)

    label("loc_339")

    Jump("loc_16C0")

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_388")
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377")
    OP_A9(0xA1)
    TalkEnd(0x8)
    Return()

    label("loc_377")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_388")
    TalkEnd(0x8)
    Return()

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(2590, 250, 4210, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2200, 250, 3530, 0)
    SetChrPos(0xF8, 3750, 250, 2330, 0)
    SetChrPos(0xF9, 2210, 250, 2420, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#1000F好久不见，毛婆婆。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(    #1
        0x107,
        "#061F你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#680F哟，艾丝蒂尔，还有提妲。\x01",
            "欢迎来我这儿。\x02\x03",

            "#683F哟，这位是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE")

    label("loc_4B3")


    ChrTalk(    #3
        0x8,
        (
            "#680F哟，艾丝蒂尔，还有你们几个。\x01",
            "欢迎来我这儿。\x02\x03",

            "#683F哟，这位是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE")


    ChrTalk(    #4
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#681F我想怎么这么面熟呢，\x01",
            "果然是约修亚啊。\x02\x03",

            "好久没见到你们\x01",
            "一起来了。\x02\x03",

            "#680F不巧，澡堂不能用，\x01",
            "不过还是请你们好好放松一下。\x02\x03",

            "饭菜什么的\x01",
            "还是和平常一样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2083)
    EventEnd(0x0)
    Jump("loc_837")

    label("loc_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B")

    ChrTalk(    #6
        0x8,
        (
            "#680F不巧，因为导力器停了，\x01",
            "澡堂也不能用。\x02\x03",

            "不过饭菜什么的\x01",
            "还是和平常一样的。\x02\x03",

            "知道你们很忙，可还是\x01",
            "希望你们能好好放松一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_837")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_74D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ED")

    ChrTalk(    #7
        0x8,
        (
            "#680F哟，你们几个。\x01",
            "这次真是辛苦了。\x02\x03",

            "在你们的帮助下旅馆\x01",
            "也恢复往常的营业了。\x02\x03",

            "虽然客人可能还要\x01",
            "过一阵子才会回来，\x01",
            "总之我会耐心地等的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_74A")

    label("loc_6ED")


    ChrTalk(    #8
        0x8,
        (
            "#680F在你们的帮助下旅馆\x01",
            "也能像往常一样营业了。\x02\x03",

            "接下来就是等客人在\x01",
            "王国的混乱平息回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74A")

    Jump("loc_837")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 7)), scpexpr(EXPR_END)), "loc_832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D8")

    ChrTalk(    #9
        0x8,
        (
            "#680F水泵小屋在村子的广场\x01",
            "北边的高地上哦。\x02\x03",

            "如果那个不能用\x01",
            "这里也就没法做生意了。\x02\x03",

            "有什么好办法\x01",
            "一定要告诉我哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_82F")

    label("loc_7D8")


    ChrTalk(    #10
        0x8,
        (
            "#680F水泵小屋在村子的广场\x01",
            "北边的高地上哦。\x02\x03",

            "如果那个不能用\x01",
            "这里也就没法做生意了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82F")

    Jump("loc_837")

    label("loc_832")

    Call(0, 11)
    Return()

    label("loc_837")

    TalkEnd(0x8)
    Return()

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8D3")

    ChrTalk(    #11
        0x8,
        (
            "#680F反正无论如何，\x01",
            "要是自然造成的也没办法。\x02\x03",

            "如果再出现的话\x01",
            "我就一定会联络协会了。\x02\x03",

            "那么，你们几个，\x01",
            "有事我会再找你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5A")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #12
        0x8,
        (
            "#680F地震看来也停止了，\x01",
            "这样一来事情总算是平息了。\x02\x03",

            "有空的时候\x01",
            "大家一起过来住下休息休息吧。\x02\x03",

            "我这里随时\x01",
            "欢迎你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4")

    label("loc_964")


    ChrTalk(    #13
        0x8,
        (
            "#680F哟，你们几个。\x01",
            "上回真是谢谢了。\x02\x03",

            "在你们的帮助下温泉\x01",
            "也完全复原了。\x02\x03",

            "有空的时候\x01",
            "大家一起过来住下休息休息吧。\x02\x03",

            "我这里随时\x01",
            "欢迎你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9F4")

    Jump("loc_C23")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A54")

    ChrTalk(    #14
        0x8,
        (
            "#680F源泉所在的洞窟\x01",
            "可以从后面的栅门进入。\x02\x03",

            "用刚才的钥匙\x01",
            "应该能打开栅门的锁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C23")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AC4")

    ChrTalk(    #15
        0x8,
        (
            "#680F听说好多地方\x01",
            "都发生了地震啊。\x02\x03",

            "不过我觉得在这片土地上应该\x01",
            "不会如此频繁地发生地震吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_AC4")


    ChrTalk(    #16
        0x8,
        (
            "#680F最近好像在蔡斯\x01",
            "也发生了地震吧。\x02\x03",

            "我几乎不记得在这片\x01",
            "土地上发生过地震。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B18")

    Jump("loc_C23")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B79")

    ChrTalk(    #17
        0x8,
        (
            "#680F互不侵犯条约就是大家\x01",
            "和平共处的约定吧？\x02\x03",

            "为什么不早点\x01",
            "缔结条约呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE5")

    label("loc_B79")


    ChrTalk(    #18
        0x8,
        (
            "#680F那个什么互不侵犯条约\x01",
            "的签字仪式很快就要举行了吧？\x02\x03",

            "据说还有共和国的来宾，\x01",
            "说不定客人会增加呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BE5")

    Jump("loc_C23")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_C23")

    ChrTalk(    #19
        0x8,
        (
            "#680F你们随时可以\x01",
            "去洗澡哦。\x02\x03",

            "总之小心一点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C23")

    Jump("loc_C5A")

    label("loc_C26")


    ChrTalk(    #20
        0x8,
        (
            "#680F你们随时可以\x01",
            "去洗澡哦。\x02\x03",

            "总之小心一点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5A")

    Jump("loc_16C0")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_11EB")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #21
        0x8,
        "#680F哟，你们来了啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #22
        0x8,
        "#680F怎么？提妲也在？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#560F您好，毛婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1006F毛婆婆，好久不见。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #25
        0x8,
        (
            "#680F嗯，艾丝蒂尔，好久不见。\x02\x03",

            "与以前来的时候相比\x01",
            "一下子变得更像大人了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1008F嘿嘿……是吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #27
        0x104,
        "#030F老板娘，上次麻烦你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #28
        0x8,
        (
            "#683F哟，我还说怎么这么脸熟……\x02\x03",

            "这不是奥利维尔先生吗？\x01",
            "怎么连你也来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        "#064F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x104,
        (
            "#035F呵呵，说来话长。\x02\x03",

            "现在我作为协力人员\x01",
            "和他们一起行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004F你、你们认识？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #32
        0x8,
        (
            "#680F嗯，不久前他\x01",
            "在这里住宿过。\x02\x03",

            "#685F我还是第一次看到有客人\x01",
            "在泡澡时还弹琴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EEF")

    ChrTalk(    #33
        0x106,
        (
            "#551F看来这家伙无论到哪里\x01",
            "都会做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F27")

    label("loc_EEF")


    ChrTalk(    #34
        0x103,
        (
            "#025F唉，这个笨蛋好像无论到哪里\x01",
            "都在做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F27")


    ChrTalk(    #35
        0x104,
        (
            "#031F哼哼，这是我们艺术家的宿命。\x02\x03",

            "对为美的女神服务的人来说，\x01",
            "时间和空间根本就是无关紧要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1007F即便如此，在全裸的\x01",
            "状态下弹琴也太那个什么了。\x02\x03",

            "#1013F啊……不好……\x01",
            "在脑中想象了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #37
        0x107,
        "#562F姐、姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#680F算啦，无论如何，\x01",
            "你能喜欢我很高兴。\x02\x03",

            "这样的话大家\x01",
            "一起住下来怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B7")

    label("loc_1070")


    ChrTalk(    #39
        0x8,
        (
            "#680F话虽这么说，难得\x01",
            "大家都来了\x02\x03",

            "既然这样好好歇息\x01",
            "一晚上怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1109")

    ChrTalk(    #40
        0x106,
        (
            "#051F我们倒是想这样，\x01",
            "可不巧的是现在是在工作。\x02\x03",

            "下次有机会再讨教。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_1109")


    ChrTalk(    #41
        0x103,
        (
            "#020F我们倒是想这样，\x01",
            "可不巧的是现在是在工作哦。\x02\x03",

            "下次有机会再讨饶吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1155")

    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #42
        0x8,
        (
            "#680F怎么？又是工作？\x02\x03",

            "那么至少\x01",
            "去泡个澡吧。\x02\x03",

            "我这里你们可以随时\x01",
            "随意用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1001F啊，那可是求之不得啊。\x02\x03",

            "嗯，有时间我们\x01",
            "就去试试。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BA")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_16BA")
    TurnDirection(0x8, 0x101, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #44
        0x8,
        "#680F哟，你们来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1006F你好，毛婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#680F艾丝蒂尔，好久不见。\x02\x03",

            "与以前来的时候相比\x01",
            "一下子变得更像大人了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1008F嘿嘿……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x104,
        "#030F老板娘，上次麻烦你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #49
        0x8,
        (
            "#683F哟，我还说怎么这么脸熟……\x02\x03",

            "这不是奥利维尔先生吗？\x01",
            "怎么连你也来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        (
            "#035F呵呵，说来话长。\x02\x03",

            "现在我作为协力人员\x01",
            "和他们一起行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1004F你、你们认识？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #52
        0x8,
        (
            "#680F嗯，不久前他\x01",
            "在这里住宿过。\x02\x03",

            "#685F我还是第一次看到有客人\x01",
            "在澡堂里弹琴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_140F")

    ChrTalk(    #53
        0x106,
        (
            "#551F就是说他到哪儿\x01",
            "都会做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_140F")


    ChrTalk(    #54
        0x103,
        (
            "#025F唉，就是说他到哪儿\x01",
            "都会做同样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143F")


    ChrTalk(    #55
        0x104,
        (
            "#031F哼哼，这是我们艺术家的宿命。\x02\x03",

            "对为美的女神服务的人来说\x01",
            "时间和空间根本就是无关紧要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1007F即便如此，在全裸的\x01",
            "状态下弹琴也太那个什么了。\x02\x03",

            "#1013F啊……不好……\x01",
            "在脑中想象了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x105,
        "#540F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#680F算啦，无论如何，\x01",
            "只要你们喜欢就好了。\x02\x03",

            "这样的话，不如大家\x01",
            "一起住下来怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_15CB")

    ChrTalk(    #59
        0x106,
        (
            "#051F我们也很想啊，\x01",
            "可惜现在正在调查的途中。\x02\x03",

            "下次有机会再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_15CB")


    ChrTalk(    #60
        0x103,
        (
            "#020F其实我们也很想那样，\x01",
            "不巧的是我们还在调查的途中哦。\x02\x03",

            "下次有机会时再来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161F")

    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #61
        0x8,
        (
            "#680F怎么？又有工作了吗？\x02\x03",

            "那么至少\x01",
            "去泡个澡吧。\x02\x03",

            "我这里随时\x01",
            "可以让你们使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1001F啊，那太好了。\x02\x03",

            "嗯，有时间的话我们\x01",
            "一定会去泡一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    OP_A2(0x1482)
    OP_A2(0x0)

    label("loc_16C0")

    TalkEnd(0x8)
    Return()

    # Function_3_2FE end

    def Function_4_16C4(): pass

    label("Function_4_16C4")

    Call(0, 5)
    Return()

    # Function_4_16C4 end

    def Function_5_16C9(): pass

    label("Function_5_16C9")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西\x01",                                # 1
            "招牌菜『东方火锅·山』　1000米拉\x01",      # 2
            "退出\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174B")
    OP_0D()
    OP_A9(0xA2)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_174B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1824")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #63
        "\x06\x07\x02东方火锅·山\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0xBB8)
    OP_31(0x1, 0xFD, 0xBB8)
    OP_31(0x2, 0xFD, 0xBB8)
    OP_31(0x3, 0xFD, 0xBB8)
    OP_31(0x4, 0xFD, 0xBB8)
    OP_31(0x5, 0xFD, 0xBB8)
    OP_31(0x6, 0xFD, 0xBB8)
    OP_31(0x7, 0xFD, 0xBB8)
    OP_31(0x8, 0xFD, 0xBB8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1816")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_17EA")
    Jump("loc_1816")

    label("loc_17EA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x06\x07\x02东方火锅·山\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_1816")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_184A")

    label("loc_1824")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #65
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_184A")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_185C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186D")
    TalkEnd(0x9)
    Return()

    label("loc_186D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1917")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(    #66
        0x9,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "澡堂终于\x01",
            "可以用了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "请各位客人\x01",
            "你们去泡一个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1914")

    label("loc_18CE")


    ChrTalk(    #69
        0x9,
        (
            "澡堂终于\x01",
            "可以用了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "这样一来我们的旅馆也\x01",
            "也能照常营业了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1914")

    Jump("loc_1CDB")

    label("loc_1917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A5")

    ChrTalk(    #71
        0x9,
        (
            "欢迎。\x01",
            "欢迎来到『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "真是不好意思，\x01",
            "现在澡堂不能用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "导力器竟然全都不行了，\x01",
            "到底是什么原因呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_19E7")

    label("loc_19A5")


    ChrTalk(    #74
        0x9,
        (
            "抱歉，\x01",
            "澡堂不能用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "真的很抱歉。\x01",
            "虽然你们可能很期待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E7")

    Jump("loc_1CDB")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(    #76
        0x9,
        (
            "吃饭前\x01",
            "泡个澡怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "已经能照常\x01",
            "使用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_1A2F")


    ChrTalk(    #78
        0x9,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "吃饭前\x01",
            "泡个澡怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "已经能照常\x01",
            "使用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1A78")

    Jump("loc_1CDB")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1ACF")

    ChrTalk(    #81
        0x9,
        (
            "这样的事情至今为止\x01",
            "一次也没有发生过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "到底发生了什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1ACF")


    ChrTalk(    #83
        0x9,
        (
            "温泉竟然热到\x01",
            "要沸腾的程度了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        "地下到底在发生着什么。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B13")

    Jump("loc_1CDB")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1C37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B96")

    ChrTalk(    #85
        0x9,
        (
            "好像有魔兽\x01",
            "闯进了露天澡堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "莫非偷窥色魔的传言\x01",
            "就是说的那些魔兽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        "真是的，搞得这么沸沸扬扬。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C34")

    label("loc_1B96")


    ChrTalk(    #88
        0x9,
        (
            "最近有传言说我们\x01",
            "澡堂有人在偷窥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "不过又没人看清\x01",
            "罪犯的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "又没有证据，\x01",
            "光有传言传播出去真令人讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "希望你们游击士\x01",
            "能赶紧想想办法……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C34")

    Jump("loc_1CDB")

    label("loc_1C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(    #92
        0x9,
        (
            "我们的东方菜是很有名的哦。\x01",
            "还有新菜单，\x01",
            "请你们一定要试试。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1C88")


    ChrTalk(    #93
        0x9,
        (
            "呀，欢迎。\x01",
            "欢迎来到『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "我们的东方菜是很有名的哦。\x01",
            "请随意吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1CDB")

    TalkEnd(0x9)
    Return()

    # Function_5_16C9 end

    def Function_6_1CDF(): pass

    label("Function_6_1CDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D59")

    ChrTalk(    #95
        0xFE,
        (
            "东方菜的优点在于\x01",
            "灵活发挥材料特色的烹调法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "如果不是味觉敏锐的人\x01",
            "是很难明白这其中的优点的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB2")

    label("loc_1D59")


    ChrTalk(    #97
        0xFE,
        (
            "这儿的东方菜\x01",
            "可是丝毫不输原产地的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "我可是安特洛丝的常客，\x01",
            "听我的准没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1DB2")

    Jump("loc_1EC4")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DDC")

    ChrTalk(    #99
        0xFE,
        "外面怎么这么吵？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_1DDC")


    ChrTalk(    #100
        0xFE,
        "外面怎么这么吵？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "有魔兽\x01",
            "闯进来了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1E0E")

    Jump("loc_1EC4")

    label("loc_1E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1E1B")
    Jump("loc_1EC4")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1EC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(    #102
        0xFE,
        "呵呵～好舒服的热水。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "浴衣也很整洁。\x01",
            "这儿的温泉质量真好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC4")

    label("loc_1E6F")


    ChrTalk(    #104
        0xFE,
        (
            "我是千里迢迢从\x01",
            "柏斯来这儿做温泉疗养的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "因为这儿的温泉\x01",
            "值得我这么做。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1EC4")

    TalkEnd(0xFE)
    Return()

    # Function_6_1CDF end

    def Function_7_1EC8(): pass

    label("Function_7_1EC8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")

    ChrTalk(    #106
        0xFE,
        (
            "哟，你们几个，\x01",
            "听说是你们修好了泵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "嘿嘿，已经是第二次说这话了，\x01",
            "今后也请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1F8E")

    label("loc_1F3C")


    ChrTalk(    #108
        0xFE,
        (
            "今后也要指望你们\x01",
            "这些游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "因为导力器不能用以后\x01",
            "到处都很不容易啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8E")

    Jump("loc_233E")

    label("loc_1F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201F")

    ChrTalk(    #110
        0xFE,
        (
            "我们这里的灶不是导力式的，\x01",
            "所以不影响工作啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "导力虽然也很诱人，\x01",
            "不过一发生这样的事，\x01",
            "就能看到旧工具的好处了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2071")

    label("loc_201F")


    ChrTalk(    #112
        0xFE,
        (
            "我们这里的灶不是导力式的，\x01",
            "所以不影响工作啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "果然工具还是\x01",
            "越简单越好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2071")

    Jump("loc_233E")

    label("loc_2074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20CB")

    ChrTalk(    #114
        0xC,
        (
            "在你们的帮助下\x01",
            "温泉也完全复原了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "下次你们趁休息\x01",
            "过来玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2125")

    label("loc_20CB")


    ChrTalk(    #116
        0xC,
        "哟，是你们啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "哎呀～在你们的帮助下\x01",
            "温泉也完全复原了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        "游击士果然可靠。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2125")

    Jump("loc_233E")

    label("loc_2128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_21DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(    #119
        0xC,
        (
            "不过还真没想到温泉\x01",
            "会被煮得沸沸腾腾的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "不管世间发生什么\x01",
            "接下来会发生什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D9")

    label("loc_2193")


    ChrTalk(    #121
        0xC,
        "源泉的调查就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "这样下去的话，\x01",
            "我们没法营业了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_21D9")

    Jump("loc_233E")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_22AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2243")

    ChrTalk(    #123
        0xC,
        (
            "莉西亚不愧是我的女儿，\x01",
            "味觉相当敏锐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "不过因为太像我，\x01",
            "性格也大大咧咧的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A8")

    label("loc_2243")


    ChrTalk(    #125
        0xC,
        (
            "最近我女儿莉西亚也\x01",
            "来旅馆帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "虽然现在在打扫房间，\x01",
            "不过也希望她将来能做我的帮手哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_22A8")

    Jump("loc_233E")

    label("loc_22AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_233E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2308")

    ChrTalk(    #127
        0xC,
        (
            "都说东方菜的好处\x01",
            "有三个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "第一是味道，接下来是外观，\x01",
            "最后是健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233E")

    label("loc_2308")


    ChrTalk(    #129
        0xC,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xC,
        (
            "请一定尝尝我们\x01",
            "拿手的东方菜。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_233E")

    TalkEnd(0xC)
    Return()

    # Function_7_1EC8 end

    def Function_8_2342(): pass

    label("Function_8_2342")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D9")

    ChrTalk(    #131
        0xFE,
        (
            "导力器都不能用了，\x01",
            "大家怎么好像都不太着急呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "反而是我这个旁观者\x01",
            "都快要着急起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "现在蔡斯那边\x01",
            "一定很混乱吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2437")

    label("loc_23D9")


    ChrTalk(    #134
        0xFE,
        (
            "导力器都不能用了，\x01",
            "大家怎么好像都不太着急呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "反而是我这个旁观者\x01",
            "都快要着急起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2437")

    Jump("loc_28AD")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_24C5")

    ChrTalk(    #136
        0xD,
        (
            "反正也是闲着，就开始\x01",
            "打工了，打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        (
            "不过都是一些上了年纪的客人，\x01",
            "不太有干劲啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2561")

    label("loc_24C5")


    ChrTalk(    #138
        0xD,
        (
            "反正也是闲着，就开始\x01",
            "打工了，打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xD,
        (
            "不过都是一些上了年纪的客人，\x01",
            "不太有干劲啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        (
            "要是多一些像奥利维尔大人\x01",
            "这样的有趣的客人该多好啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2561")

    Jump("loc_25AB")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_25AB")

    ChrTalk(    #141
        0xD,
        (
            "啊～还是\x01",
            "奥利维尔大人优秀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xD,
        (
            "哎呀～请把我\x01",
            "拐去帝都吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AB")

    Jump("loc_25EE")

    label("loc_25AE")


    ChrTalk(    #143
        0xD,
        (
            "啊～还是\x01",
            "奥利维尔大人优秀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "哎呀～请把我\x01",
            "拐去帝都吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25EE")

    Jump("loc_28AD")

    label("loc_25F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(    #145
        0xD,
        (
            "反正也是闲着，就开始\x01",
            "打工了，打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xD,
        (
            "不过都是一些上了年纪的客人，\x01",
            "不太有干劲啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        "……咦？啊、啊？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #148
        0xD,
        "呀～！？　这不是奥利维尔大人么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "我真高兴～！\x01",
            "您又来啦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1004F（奥、奥利维尔大人～？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x104,
        (
            "#031F呵呵，好久不见。\x01",
            "还乖吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2861")

    label("loc_2726")


    ChrTalk(    #152
        0xD,
        (
            "反正也是闲着，就开始\x01",
            "打工了，打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "不过都是一些上了年纪的客人，\x01",
            "不太有干劲啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x104, 500)

    ChrTalk(    #154
        0xD,
        "……咦？啊、啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xD,
        "那、那边是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x104,
        (
            "#031F呵呵，好久不见。\x01",
            "还乖吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #157
        0xD,
        (
            "呀～！？\x01",
            "果然是奥利维尔大人！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        (
            "我真高兴～！\x01",
            "您又来啦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1004F（奥、奥利维尔大人～？）\x02",
    )

    CloseMessageWindow()

    label("loc_2861")


    ChrTalk(    #160
        0xD,
        (
            "奥利维尔先生～\x01",
            "这次要再唱歌给我听哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "您弹琴的样子\x01",
            "最帅了㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1430)
    OP_A2(0x5)

    label("loc_28AD")

    TalkEnd(0xD)
    Return()

    # Function_8_2342 end

    def Function_9_28B1(): pass

    label("Function_9_28B1")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2977")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2903")

    ChrTalk(    #162
        0xFE,
        (
            "今天要采访\x01",
            "东方菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "呼～希望能找到\x01",
            "好的表达方式……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2977")

    label("loc_2903")


    ChrTalk(    #164
        0xFE,
        (
            "要用文章来描写\x01",
            "菜的可口是很难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "越是真正的美味，\x01",
            "越难写成文章。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "因为除了『好吃』以外\x01",
            "无以形容。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2977")

    TalkEnd(0xE)
    Return()

    # Function_9_28B1 end

    def Function_10_297B(): pass

    label("Function_10_297B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DA")

    ChrTalk(    #167
        0xFE,
        "开水好像能出来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "呼，看来是阿尔宾的愿望\x01",
            "传递到了女神那里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2A11")

    label("loc_29DA")


    ChrTalk(    #169
        0xFE,
        "开水好像能出来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "再过一会儿\x01",
            "去浴场看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A11")

    Jump("loc_2B64")

    label("loc_2A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    ChrTalk(    #171
        0xFE,
        (
            "为了治疗登山的疲劳，\x01",
            "我和同伴温泉疗养来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "不过遗憾的是因为泵的问题，\x01",
            "没法去洗温泉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "不过我的同伴不死心，\x01",
            "还是去了浴室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "这种时候就算勉强\x01",
            "对自己也没好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "我还是吃着美味的\x01",
            "东方菜好好休息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2B64")

    label("loc_2B04")


    ChrTalk(    #176
        0xFE,
        (
            "明明知道不能洗，\x01",
            "阿尔宾还是去了澡堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "那家伙是个一旦决定了什么就\x01",
            "死也不会回头的男人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B64")

    TalkEnd(0xFE)
    Return()

    # Function_10_297B end

    def Function_11_2B68(): pass

    label("Function_11_2B68")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B88")
    Call(0, 13)
    Call(0, 14)
    FadeToBright(0, 0)

    label("loc_2B88")

    Fade(500)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2100, 250, 3530, 0)
    SetChrPos(0xF8, 3700, 250, 2250, 0)
    SetChrPos(0xF9, 2250, 250, 2250, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC2, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_302F")

    ChrTalk(    #178
        0x8,
        (
            "#680F#2P温泉的事\x01",
            "你们不必在意。\x02\x03",

            "你们应该有你们\x01",
            "应该做的工作。\x02\x03",

            "要优先顾及那个。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【那我们就不客气了】\x01",      # 0
            "【硬着头皮帮忙】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF0")
    OP_28(0xC2, 0x1, 0x8000)
    EventEnd(0x0)
    Jump("loc_302C")

    label("loc_2CF0")


    ChrTalk(    #179
        0x101,
        (
            "#1006F#6P不过，难得有机会，\x01",
            "能不能交给我们试试？\x02\x03",

            "说不定会得到\x01",
            "游击士才能给出的结果呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #180
        0x102,
        "#1044F#5P艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "#683F#2P哦……？\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1015F#6P嗯，是啊。\x02\x03",

            "#1006F首先希望您能\x01",
            "借给我们水泵小屋的钥匙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "#680F#2P嗯，这倒没问题……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #184
        "\x1F\x0A\x04\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40A, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ED7")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #185
        0x101,
        (
            "#1006F#2P提妲，正好有机会，\x01",
            "要不要去看看泵装置的状况？\x02\x03",

            "可能会发现\x01",
            "一些什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #186
        0x107,
        "#560F#6P啊，……嗯，是啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F34")

    label("loc_2ED7")

    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #187
        0x101,
        (
            "#1006F#2P各位，正好有机会\x01",
            "要不要去看看泵装置的状况？\x02\x03",

            "可能会发现\x01",
            "一些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F34")


    ChrTalk(    #188
        0x102,
        "#1040F#5P原来是这样。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F80")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #189
        0x106,
        "#051F#6P真是没办法……\x02",
    )

    CloseMessageWindow()

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FAD")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #190
        0x103,
        "#021F#6P我没意见。\x02",
    )

    CloseMessageWindow()

    label("loc_2FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE9")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #191
        0x108,
        (
            "#070F#6P总之先去\x01",
            "确认一下情况吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE9")


    ChrTalk(    #192
        0x101,
        (
            "#1001F#2P那就决定了。\x01",
            "去水泵小屋看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0xC2, 0x4, 0x2)
    OP_28(0xC2, 0x4, 0x8)
    OP_28(0xC2, 0x1, 0x1)
    EventEnd(0x0)

    label("loc_302C")

    Jump("loc_35E3")

    label("loc_302F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3077")

    ChrTalk(    #193
        0x107,
        (
            "#063F#6P请问，毛婆婆……\x02\x03",

            "我们有什么\x01",
            "能帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A7")

    label("loc_3077")


    ChrTalk(    #194
        0x101,
        (
            "#1015F#6P毛婆婆。\x02\x03",

            "我们有什么\x01",
            "能帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A7")


    ChrTalk(    #195
        0x8,
        (
            "#680F#2P嗯，这个啊。\x02\x03",

            "士兵已经开始\x01",
            "定期巡逻了，\x01",
            "所以安全方面没什么问题了。\x02\x03",

            "硬要说的话，我希望可以\x01",
            "想办法让温泉能恢复使用……\x02\x03",

            "#685F不过可能跟你们\x01",
            "说了也没什么用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1015F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【到底还是太难了……】\x01",      # 0
            "【硬着头皮帮忙】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A7")

    ChrTalk(    #197
        0x101,
        (
            "#1007F#6P……抱歉，毛婆婆。\x02\x03",

            "#1003F确实对我们来说\x01",
            "太难了点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#680F#2P嗯，没关系。\x02\x03",

            "你们应该有你们\x01",
            "应该做的工作。\x02\x03",

            "要优先顾及那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#1035F#6P……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#1025F#6P嗯……\x01",
            "我们会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC2, 0x1, 0x8000)
    EventEnd(0x0)
    Jump("loc_35E3")

    label("loc_32A7")


    ChrTalk(    #201
        0x101,
        (
            "#1006F#6P不过，难得有机会，\x01",
            "能不能交给我们试试？\x02\x03",

            "说不定会得到\x01",
            "游击士才能给出的结果呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #202
        0x102,
        "#1044F#5P艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x8,
        (
            "#683F#2P哦……？\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1015F#6P嗯，是啊。\x02\x03",

            "#1006F首先希望你能\x01",
            "借给我们水泵小屋的钥匙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x8,
        "#680F#2P嗯，这倒没问题……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #206
        "\x1F\x0A\x04\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40A, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_348E")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #207
        0x101,
        (
            "#1006F#2P提妲，正好有机会，\x01",
            "要不要去看看泵装置的状况？\x02\x03",

            "可能会发现\x01",
            "一些什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #208
        0x107,
        "#560F#6P啊，……嗯，是啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34EB")

    label("loc_348E")

    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #209
        0x101,
        (
            "#1006F#2P各位，正好有机会\x01",
            "要不要去看看泵装置的状况？\x02\x03",

            "可能会发现\x01",
            "一些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")


    ChrTalk(    #210
        0x102,
        "#1040F#5P原来是这样。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3537")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #211
        0x106,
        "#051F#6P真是没办法……\x02",
    )

    CloseMessageWindow()

    label("loc_3537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3564")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #212
        0x103,
        "#021F#6P我没意见。\x02",
    )

    CloseMessageWindow()

    label("loc_3564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A0")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #213
        0x108,
        (
            "#070F#6P总之先去\x01",
            "确认一下情况吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A0")


    ChrTalk(    #214
        0x101,
        (
            "#1001F#2P那就决定了。\x01",
            "去水泵小屋看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0xC2, 0x4, 0x2)
    OP_28(0xC2, 0x4, 0x8)
    OP_28(0xC2, 0x1, 0x1)
    EventEnd(0x0)

    label("loc_35E3")

    OP_43(0x8, 0x0, 0x6, 0x2)
    Return()

    # Function_11_2B68 end

    def Function_12_35EB(): pass

    label("Function_12_35EB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_360B")
    Call(0, 13)
    Call(0, 14)
    FadeToBright(0, 0)

    label("loc_360B")

    OP_4A(0x8, 255)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2100, 250, 3530, 0)
    SetChrPos(0xF8, 3700, 250, 2250, 0)
    SetChrPos(0xF9, 2250, 250, 2250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #215
        0x8,
        (
            "#680F#2P──没想到你们真能\x01",
            "让泵动起来。\x02\x03",

            "#681F谢谢啊。\x01",
            "这样一来就能让\x01",
            "大家尽情地泡澡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#1008F#6P嘿嘿……\x01",
            "能帮上你们真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #217
        0x101,
        (
            "#1006F#2P不过９成是\x01",
            "提妲的功劳。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #218
        0x107,
        (
            "#067F#6P没、没有～\x02\x03",

            "#560F因为姐姐你们找来了\x01",
            "必要的东西，\x01",
            "我才能改造的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D6")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_37DD")

    label("loc_37D6")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_37DD")


    ChrTalk(    #219
        0x106,
        (
            "#551F#6P不过这次还真是\x01",
            "让我们东奔西跑的。\x02\x03",

            "#555F这也是导力停止现象的危害啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3835():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3835)
    Sleep(50)

    def lambda_3848():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3848)
    Sleep(50)
    TurnDirection(0x107, 0x106, 400)
    Jump("loc_39B8")

    label("loc_385F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_390D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3884")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_388B")

    label("loc_3884")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_388B")


    ChrTalk(    #220
        0x103,
        (
            "#025F#6P不过这次还真是\x01",
            "让我们东奔西跑的。\x02\x03",

            "#022F这也是导力停止现象的危害啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38E3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38E3)
    Sleep(50)

    def lambda_38F6():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38F6)
    Sleep(50)
    TurnDirection(0x107, 0x103, 400)
    Jump("loc_39B8")

    label("loc_390D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3932")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_3939")

    label("loc_3932")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_3939")


    ChrTalk(    #221
        0x108,
        (
            "#075F#6P不过这次还真是\x01",
            "让我们东奔西跑的。\x02\x03",

            "#072F这也是导力停止现象的危害啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3991():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3991)
    Sleep(50)

    def lambda_39A4():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39A4)
    Sleep(50)
    TurnDirection(0x107, 0x108, 400)

    label("loc_39B8")

    WaitChrThread(0x102, 0x1)
    Sleep(200)

    ChrTalk(    #222
        0x102,
        (
            "#1043F#5P……是啊。\x02\x03",

            "#1035F技术方面的功能丧失，\x01",
            "对以此为基础的社会\x01",
            "有着严重的影响……\x02\x03",

            "#1042F这样下去的话\x01",
            "事态只会不断恶化。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #223
        0x107,
        "#063F#6P约修亚哥哥……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #224
        0x101,
        (
            "#1006F#4P好了，也没\x01",
            "那么悲观了。\x02\x03",

            "导力虽然停了，\x01",
            "不过泵不也能用了吗。\x02\x03",

            "#1001F人只要有决心\x01",
            "什么都能做到。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #225
        0x102,
        "#1044F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        (
            "#681F#2P哈哈，说得好。\x02\x03",

            "#680F总之这次\x01",
            "真的是累了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B46():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B46)
    Sleep(100)

    def lambda_3B59():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B59)
    Sleep(100)

    def lambda_3B6C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B6C)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B90")
    OP_8C(0xF9, 0, 400)
    Jump("loc_3B97")

    label("loc_3B90")

    OP_8C(0xF8, 0, 400)

    label("loc_3B97")

    Sleep(300)

    ChrTalk(    #227
        0x8,
        (
            "#680F#2P赶快先去泡个澡，\x01",
            "消解旅行的疲劳吧。\x02\x03",

            "#681F对了，我家有祖传的\x01",
            "有效的药草茶哦。\x02\x03",

            "你们可以在洗完澡时喝。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #228
        "\x07\x00得到了４个\x1F\xC9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1C9, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #229
        (
            "\x07\x05此后，泡了温泉的艾丝蒂尔一行\x01",
            "在品尝了毛赖以自豪的东方菜后\x01",
            "离开了『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCD")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_3CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CE0")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_3CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CF3")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_3CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D06")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_3D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D19")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_3D19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D2C")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_3D2C")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #230
        "\x07\x02任务【亚尔摩温泉的修复】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x40A, 1)
    OP_3F(0x40B, 1)
    OP_28(0xC2, 0x4, 0x10)
    OP_28(0xC2, 0x1, 0x2000)
    OP_28(0xC2, 0x1, 0x4000)
    OP_A2(0x2012)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T3200   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_35EB end

    def Function_13_3D9C(): pass

    label("Function_13_3D9C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E19"),
        (1, "loc_3E1F"),
        (SWITCH_DEFAULT, "loc_3E25"),
    )


    label("loc_3E19")

    OP_A2(0x1200)
    Jump("loc_3E25")

    label("loc_3E1F")

    OP_A2(0x1201)
    Jump("loc_3E25")

    label("loc_3E25")

    Return()

    # Function_13_3D9C end

    def Function_14_3E26(): pass

    label("Function_14_3E26")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_14_3E26 end

    def Function_15_3E7F(): pass

    label("Function_15_3E7F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #231
        "\x07\x05露天澡堂在这边 ≡\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_3E7F end

    SaveToFile()

Try(main)
