from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        '士兵安托斯',                           # 9
        '士兵拉科斯',                           # 10
        '士兵斯科特',                           # 11
        '士兵哈罗德',                           # 12
        '王国军士兵',                           # 13
        '王国军士兵',                           # 14
        '米尔西街道方向',                       # 15
        '东柏斯街道方向',                       # 16
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
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3300,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -1980,
        Z                   = -410,
        Y                   = -40440,
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
        X                   = 440,
        Z                   = -510,
        Y                   = 41850,
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


    DeclActor(
        TriggerX            = 5680,
        TriggerZ            = -260,
        TriggerY            = -27360,
        TriggerRange        = 1500,
        ActorX              = 5680,
        ActorZ              = 1700,
        ActorY              = -27360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9630,
        TriggerZ            = -150,
        TriggerY            = 27430,
        TriggerRange        = 1500,
        ActorX              = -9630,
        ActorZ              = 1700,
        ActorY              = 27430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13270,
        TriggerZ            = -30,
        TriggerY            = -5630,
        TriggerRange        = 1000,
        ActorX              = -12930,
        ActorZ              = -800,
        ActorY              = -2830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21E",          # 00, 0
        "Function_1_249",          # 01, 1
        "Function_2_276",          # 02, 2
        "Function_3_3F3",          # 03, 3
        "Function_4_54D",          # 04, 4
        "Function_5_9DF",          # 05, 5
        "Function_6_C9A",          # 06, 6
        "Function_7_1062",         # 07, 7
        "Function_8_12F9",         # 08, 8
        "Function_9_137B",         # 09, 9
        "Function_10_13E1",        # 0A, 10
        "Function_11_157E",        # 0B, 11
        "Function_12_15E6",        # 0C, 12
    )


    def Function_0_21E(): pass

    label("Function_0_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_228")
    Jump("loc_248")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_248")

    Return()

    # Function_0_21E end

    def Function_1_249(): pass

    label("Function_1_249")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFE0FE8, 0x230005)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275")
    OP_6F(0x1, 420)
    OP_6F(0x2, 420)

    label("loc_275")

    Return()

    # Function_1_249 end

    def Function_2_276(): pass

    label("Function_2_276")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DD")

    label("loc_29B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DD")

    label("loc_2B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DD")

    label("loc_2CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DD")

    label("loc_2E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DD")

    label("loc_2FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DD")

    label("loc_318")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DD")

    label("loc_331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DD")

    label("loc_34A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DD")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DD")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DD")

    label("loc_395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DD")

    label("loc_3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DD")

    label("loc_3C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DD")

    label("loc_3F2")

    Return()

    # Function_2_276 end

    def Function_3_3F3(): pass

    label("Function_3_3F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54C")
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x438A, 0xFFFFFFC4, 0xFFFF9E94, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFABBE, 0xFFFFFF88, 0xFFFF9C14, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFAB46, 0xFFFFFEFC, 0xFFFF8DC8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFA, 0xFFFFFEF2, 0xFFFF9034, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1054, 0xFFFFFF10, 0xFFFF89B8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C10, 0xFFFFFE2A, 0xFFFF8A08, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C1A, 0x50, 0xFFFFD79C, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4236, 0xA, 0xFFFFD6E8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4218, 0x78, 0xFFFFE1BA, 0x9C4, 0x0)
    Jump("Function_3_3F3")

    label("loc_54C")

    Return()

    # Function_3_3F3 end

    def Function_4_54D(): pass

    label("Function_4_54D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_611")

    ChrTalk(    #0
        0xFE,
        (
            "刚才阿斯顿队长\x01",
            "来巡视过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "现在这样的状况下\x01",
            "他竟然还那么冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "优秀的人在这种时候\x01",
            "就会体现出其非凡之处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "他是我心中仅次于卡西乌斯准将\x01",
            "的王国军人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_675")

    label("loc_611")


    ChrTalk(    #4
        0xFE,
        (
            "现在这样的时候，\x01",
            "阿斯顿队长却可以保持如此冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "不愧是优秀的人，\x01",
            "在这种时候就体现出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675")

    Jump("loc_9DB")

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D")

    ChrTalk(    #6
        0xFE,
        (
            "呼～在大门恢复正常之前\x01",
            "绝不能放松警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "连导力枪也不能用了，\x01",
            "真是让人绝望啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "这、这种时候\x01",
            "如果那群红衣猎兵来袭的话\x01",
            "可就麻烦了…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_775")

    label("loc_71D")


    ChrTalk(    #9
        0xFE,
        (
            "呼～在大门恢复正常之前\x01",
            "绝不能放松警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "连导力枪也不能用了，\x01",
            "真是让人绝望啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_775")

    Jump("loc_9DB")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_7E8")

    ChrTalk(    #11
        0xFE,
        (
            "解决了龙的事件后，\x01",
            "将军阁下也松了一口气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "超市也重新开张营业了，\x01",
            "和平的日子终于回来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DB")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(    #13
        0xFE,
        (
            "龙的捕获作战\x01",
            "似乎很艰难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "虽然很着急……\x01",
            "但我们什么忙也帮不上啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C9")

    label("loc_847")


    ChrTalk(    #15
        0xFE,
        (
            "龙的捕获作战\x01",
            "似乎很艰难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "虽然很着急……\x01",
            "但我们什么忙也帮不上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "现在这种情况\x01",
            "就只能把一切都交给飞行舰队了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8C9")

    Jump("loc_9DB")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_939")

    ChrTalk(    #18
        0xFE,
        (
            "东侧的阿斯顿队长\x01",
            "真是个了不起的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "在洛连特警备的时候\x01",
            "就发挥了优秀的指挥才能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DB")

    label("loc_939")


    ChrTalk(    #20
        0xFE,
        (
            "东侧的阿斯顿队长\x01",
            "真是个了不起的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "在洛连特警备的时候\x01",
            "就发挥了优秀的指挥才能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "无论发生什么情况他也不会有丝毫动摇，\x01",
            "真是值得我们学习的榜样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9DB")

    TalkEnd(0x8)
    Return()

    # Function_4_54D end

    def Function_5_9DF(): pass

    label("Function_5_9DF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_A4E")

    ChrTalk(    #23
        0xFE,
        (
            "队长他们在百日战争中\x01",
            "都有过实战经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "能在这种时候保持冷静，\x01",
            "大概和那时的经验也有关吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(    #25
        0xFE,
        (
            "定期船停航之后\x01",
            "旅行者也少了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "算了，这种非常时期，\x01",
            "无论去哪里也都没多少人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(    #27
        0xFE,
        (
            "龙的骚乱\x01",
            "似乎已经平息了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "果然最后靠飞行舰队解决的，\x01",
            "但是到底做了些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(    #29
        0xFE,
        "（发抖）……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "但、但愿龙不要再来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E")

    label("loc_B53")


    ChrTalk(    #31
        0xFE,
        (
            "龙、龙会从口中\x01",
            "喷出火焰的吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "希、希望它不要\x01",
            "再来这里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B9E")

    Jump("loc_C96")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C08")

    ChrTalk(    #33
        0xFE,
        (
            "大雾的那天，\x01",
            "大门这边的工作忙死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "那种夸张的大雾……\x01",
            "希望别再有第二次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_C08")


    ChrTalk(    #35
        0xFE,
        (
            "在大雾的那天\x01",
            "大门这边的工作忙死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "不过，负责护卫的游击士\x01",
            "肯定更辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "在那种大雾之下，不管几个人同行\x01",
            "也可能会走丢的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C96")

    TalkEnd(0x9)
    Return()

    # Function_5_9DF end

    def Function_6_C9A(): pass

    label("Function_6_C9A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_D0C")

    ChrTalk(    #38
        0xFE,
        (
            "听说异变出现的时候\x01",
            "所有飞行中的警备艇\x01",
            "全部被迫降落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "（发抖）……\x01",
            "没去坐飞船真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105E")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #40
        0xFE,
        (
            "多亏了那个奇怪的装置\x01",
            "把通信器似乎修好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "但听了各地的报告之后\x01",
            "心情却越来越暗淡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "呜呜，大雾事件刚过去，\x01",
            "最近怎么这么多倒霉事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_E16")

    label("loc_DB6")


    ChrTalk(    #43
        0xFE,
        (
            "但听了各地的报告之后\x01",
            "心情却越来越暗淡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "啊啊，这样下去，利贝尔王国\x01",
            "的未来会怎样呢…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E16")

    Jump("loc_105E")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E9F")

    ChrTalk(    #45
        0xFE,
        (
            "这里的工作很轻松呢。\x01",
            "每天都很悠闲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "在洛连特的任务\x01",
            "虽然也顺利完成了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "不过果然还是这边\x01",
            "最适合我啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F25")

    label("loc_E9F")


    ChrTalk(    #48
        0xFE,
        (
            "洛连特的警备结束了，\x01",
            "我也回归原本的工作岗位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "在那边工作的时候\x01",
            "总是很紧张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "果然还是这里轻松啊。\x01",
            "每天都很悠闲。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F25")

    Jump("loc_105E")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_105E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(    #51
        0xFE,
        (
            "空贼团已经\x01",
            "不足为惧了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "在他们的首领被抓住后，\x01",
            "贼团众们便已经溃不成军了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105E")

    label("loc_F8D")


    ChrTalk(    #53
        0xFE,
        (
            "柏斯的空贼团余党\x01",
            "好像又现身了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "听说他们的手段\x01",
            "相当娴熟呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "算了，我也不用\x01",
            "担心那个啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "毕竟那些家伙\x01",
            "也不会造成太大影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "在他们的首领被抓住后，\x01",
            "现在的空贼团余党已经\x01",
            "群龙无首了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_105E")

    TalkEnd(0xA)
    Return()

    # Function_6_C9A end

    def Function_7_1062(): pass

    label("Function_7_1062")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_111F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CA")

    ChrTalk(    #58
        0xFE,
        (
            "需要用到导力的东西\x01",
            "似乎全部都不能用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "今天连搬运车\x01",
            "也停住不动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_111C")

    label("loc_10CA")


    ChrTalk(    #60
        0xFE,
        (
            "需要用到导力的东西\x01",
            "似乎全部都不能用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "可、可是我的枪也是\x01",
            "导力式的…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111C")

    Jump("loc_12F5")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117C")

    ChrTalk(    #62
        0xFE,
        (
            "啊，你们是\x01",
            "游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "那么可以自由通行。\x01",
            "我们已经收到命令了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_11B9")

    label("loc_117C")


    ChrTalk(    #64
        0xFE,
        (
            "只要是游击士\x01",
            "就可以通行自由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "我们已经收到命令了。\x02",
    )

    CloseMessageWindow()

    label("loc_11B9")

    Jump("loc_12F5")

    label("loc_11BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_128E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1211")

    ChrTalk(    #66
        0xFE,
        (
            "洛连特市的警备\x01",
            "一直惊险不断，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "能平安无事回来\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_1211")


    ChrTalk(    #68
        0xFE,
        (
            "洛连特市的警备\x01",
            "一直惊险不断，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "那里的视线非常差，\x01",
            "几步之外的东西就看不到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "能平安无事回来\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_128B")

    Jump("loc_12F5")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_12F5")

    ChrTalk(    #71
        0xFE,
        (
            "不知为什么，\x01",
            "这里的警备体制还是没有解除。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "无所谓啦，反正对我来说\x01",
            "一直都是相同的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F5")

    TalkEnd(0xB)
    Return()

    # Function_7_1062 end

    def Function_8_12F9(): pass

    label("Function_8_12F9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(    #73
        0xFE,
        (
            "我们是从哈肯大门那边调来的\x01",
            "阿斯顿部队的补充部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "暂时要负责守卫\x01",
            "这个关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "这段时间内请多多指教了！\x02",
    )

    CloseMessageWindow()

    label("loc_1377")

    TalkEnd(0xC)
    Return()

    # Function_8_12F9 end

    def Function_9_137B(): pass

    label("Function_9_137B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_13DD")

    ChrTalk(    #76
        0xFE,
        (
            "我们补充部队的几个伙伴\x01",
            "到洛连特去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "呼～其实我也想到洛连特那里\x01",
            "负责警备啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DD")

    TalkEnd(0xD)
    Return()

    # Function_9_137B end

    def Function_10_13E1(): pass

    label("Function_10_13E1")

    EventBegin(0x1)

    ChrTalk(    #78
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_140D():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_140D)

    def lambda_141D():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_141D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #79
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x2, 0xFFFFCC2A, 0xFFFFFFE2, 0xFFFFEA02, 0x168, 0xFFFFCD7E, 0xFFFFFCE0, 0xFFFFF4F2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_1568")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155F")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x4)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #80
        (
            "\x07\x05在威尔特桥发现钓鱼场的事情\x01",
            "已经记录在游击士手册上记录了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_155F")

    Jump("loc_1568")

    label("loc_1562")

    OP_28(0x73, 0x1, 0x400)

    label("loc_1568")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_157D")

    label("loc_156E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157D")
    EventEnd(0x1)

    label("loc_157D")

    Return()

    # Function_10_13E1 end

    def Function_11_157E(): pass

    label("Function_11_157E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #81
        (
            "\x07\x05东　洛连特市　１７２塞尔矩\x01",
            "西　柏斯市　　４２０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_157E end

    def Function_12_15E6(): pass

    label("Function_12_15E6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #82
        (
            "\x07\x05西　柏斯市　　４２０塞尔矩\x01",
            "东　洛连特市　１７２塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_15E6 end

    SaveToFile()

Try(main)
