from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5315   ._SN',
        MapName             = 'Other',
        Location            = 'C5315.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        '德尔基昂①',                           # 9
        '德尔基昂②',                           # 10
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_EA",           # 00, 0
        "Function_1_F9",           # 01, 1
        "Function_2_11E",          # 02, 2
        "Function_3_127",          # 03, 3
        "Function_4_1F0F",         # 04, 4
        "Function_5_252B",         # 05, 5
        "Function_6_254F",         # 06, 6
        "Function_7_2573",         # 07, 7
        "Function_8_2597",         # 08, 8
        "Function_9_261E",         # 09, 9
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_F8")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_F8")

    Return()

    # Function_0_EA end

    def Function_1_F9(): pass

    label("Function_1_F9")

    OP_22(0xEB, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x450), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_113")

    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    Return()

    # Function_1_F9 end

    def Function_2_11E(): pass

    label("Function_2_11E")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_11E end

    def Function_3_127(): pass

    label("Function_3_127")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141")
    Call(0, 8)
    Call(0, 9)
    RemoveParty(0x1, 0xFF)

    label("loc_141")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270111, 0x270121, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_17E"),
        (5, "loc_195"),
        (3, "loc_1AC"),
        (4, "loc_1C3"),
        (6, "loc_1DA"),
        (7, "loc_1F1"),
        (8, "loc_208"),
        (10, "loc_21F"),
        (SWITCH_DEFAULT, "loc_236"),
    )


    label("loc_17E")

    OP_D2(0x701D0, 0x701DC, 0x2)
    OP_D2(0x701D1, 0x701DD, 0x3)
    Jump("loc_236")

    label("loc_195")

    OP_D2(0x70218, 0x70224, 0x2)
    OP_D2(0x70219, 0x70225, 0x3)
    Jump("loc_236")

    label("loc_1AC")

    OP_D2(0x701E8, 0x701F4, 0x2)
    OP_D2(0x701E9, 0x701F5, 0x3)
    Jump("loc_236")

    label("loc_1C3")

    OP_D2(0x27036E, 0x27037B, 0x2)
    OP_D2(0x27036F, 0x27037C, 0x3)
    Jump("loc_236")

    label("loc_1DA")

    OP_D2(0x70230, 0x7023C, 0x2)
    OP_D2(0x70231, 0x7023D, 0x3)
    Jump("loc_236")

    label("loc_1F1")

    OP_D2(0x70248, 0x70254, 0x2)
    OP_D2(0x70249, 0x70255, 0x3)
    Jump("loc_236")

    label("loc_208")

    OP_D2(0x270176, 0x270183, 0x2)
    OP_D2(0x270177, 0x270184, 0x3)
    Jump("loc_236")

    label("loc_21F")

    OP_D2(0x702B4, 0x702BB, 0x2)
    OP_D2(0x702B5, 0x702BC, 0x3)
    Jump("loc_236")

    label("loc_236")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_25F"),
        (5, "loc_276"),
        (3, "loc_28D"),
        (4, "loc_2A4"),
        (6, "loc_2BB"),
        (7, "loc_2D2"),
        (8, "loc_2E9"),
        (10, "loc_300"),
        (SWITCH_DEFAULT, "loc_317"),
    )


    label("loc_25F")

    OP_D2(0x701D0, 0x701DC, 0x4)
    OP_D2(0x701D1, 0x701DD, 0x5)
    Jump("loc_317")

    label("loc_276")

    OP_D2(0x70218, 0x70224, 0x4)
    OP_D2(0x70219, 0x70225, 0x5)
    Jump("loc_317")

    label("loc_28D")

    OP_D2(0x701E8, 0x701F4, 0x4)
    OP_D2(0x701E9, 0x701F5, 0x5)
    Jump("loc_317")

    label("loc_2A4")

    OP_D2(0x27036E, 0x27037B, 0x4)
    OP_D2(0x27036F, 0x27037C, 0x5)
    Jump("loc_317")

    label("loc_2BB")

    OP_D2(0x70230, 0x7023C, 0x4)
    OP_D2(0x70231, 0x7023D, 0x5)
    Jump("loc_317")

    label("loc_2D2")

    OP_D2(0x70248, 0x70254, 0x4)
    OP_D2(0x70249, 0x70255, 0x5)
    Jump("loc_317")

    label("loc_2E9")

    OP_D2(0x270176, 0x270183, 0x4)
    OP_D2(0x270177, 0x270184, 0x5)
    Jump("loc_317")

    label("loc_300")

    OP_D2(0x702B4, 0x702BB, 0x4)
    OP_D2(0x702B5, 0x702BC, 0x5)
    Jump("loc_317")

    label("loc_317")

    StopSound(0x7530, 0x493E0, 0x0)
    OP_6D(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x10E)
    SetChrPos(0x101, 0, 1350, 1000, 0)
    SetChrPos(0xF8, -1000, 1350, -1000, 225)
    SetChrPos(0xF9, 1000, 1350, -1000, 135)
    FadeToBright(1000, 0)
    StopSound(0x7530, 0x27100, 0x1F40)

    def lambda_3BE():
        OP_6D(300, 1350, -10, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BE)

    def lambda_3D6():
        OP_67(0, 7550, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D6)

    def lambda_3EE():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3EE)

    def lambda_3FE():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3FE)

    def lambda_40E():
        OP_6E(320, 8000)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_40E)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_479")

    ChrTalk(    #0
        0x10B,
        (
            "#212F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_479")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D0")

    ChrTalk(    #1
        0x106,
        (
            "#057F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_527")

    ChrTalk(    #2
        0x103,
        (
            "#022F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_527")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57F")

    ChrTalk(    #3
        0x105,
        (
            "#1163F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_57F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D6")

    ChrTalk(    #4
        0x104,
        (
            "#032F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_5D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E")

    ChrTalk(    #5
        0x109,
        (
            "#1063F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_62E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_682")

    ChrTalk(    #6
        0x108,
        (
            "#072F想不到这原来是\x01",
            "升降梯的传动轴……\x02\x03",

            "到底会下降到什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_682")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EE")

    ChrTalk(    #7
        0x107,
        (
            "#063F……好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害。\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_6EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_756")

    ChrTalk(    #8
        0x108,
        (
            "#072F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_756")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BF")

    ChrTalk(    #9
        0x109,
        (
            "#1063F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_7BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_827")

    ChrTalk(    #10
        0x104,
        (
            "#032F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_827")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_890")

    ChrTalk(    #11
        0x105,
        (
            "#1163F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_890")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F8")

    ChrTalk(    #12
        0x103,
        (
            "#022F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95D")

    label("loc_8F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D")

    ChrTalk(    #13
        0x106,
        (
            "#057F好像这纵坑的深度\x01",
            "比中枢塔的高度还要厉害……\x02\x03",

            "可能会下降到\x01",
            "浮游都市的中心部。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95D")


    ChrTalk(    #14
        0x101,
        "#1003F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_98C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_98C)
    Sleep(100)
    OP_8C(0xF9, 0, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE6")

    ChrTalk(    #15
        0x105,
        (
            "#1162F艾丝蒂尔……没问题的。\x02\x03",

            "你跟约修亚约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "#1168F那样的话……\x01",
            "他一定会恢复原样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #16
        0x101,
        (
            "#1025F#5P科洛丝……谢谢你。\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        "#1161F嗯！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1A")

    ChrTalk(    #18
        0x108,
        "#071F对，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE3")

    label("loc_B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4C")

    ChrTalk(    #19
        0x106,
        "#051F嘿嘿，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE3")

    label("loc_B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7F")

    ChrTalk(    #20
        0x109,
        "#1061F哈哈，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE3")

    label("loc_B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(    #21
        0x103,
        "#021F呵呵，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE3")

    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE3")

    ChrTalk(    #22
        0x107,
        (
            "#061F嘿嘿……\x01",
            "就是要这种精神！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE3")

    Jump("loc_1668")

    label("loc_BE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0F")

    ChrTalk(    #23
        0x10B,
        (
            "#214F真是的……\x01",
            "别一副苦瓜脸啊！\x02\x03",

            "约修亚才不会让\x01",
            "那种眼镜男恣意操纵呢！\x02\x03",

            "肯定会恢复原样的！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        (
            "#1025F#5P乔丝特……\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10B,
        "#211F嗯！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D43")

    ChrTalk(    #26
        0x108,
        "#071F对，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(    #27
        0x106,
        "#051F嘿嘿，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(    #28
        0x109,
        "#1061F哈哈，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDA")

    ChrTalk(    #29
        0x103,
        "#021F呵呵，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(    #30
        0x107,
        (
            "#061F嘿嘿……\x01",
            "就是要这种精神！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0C")

    Jump("loc_1668")

    label("loc_E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9E")

    ChrTalk(    #31
        0x10B,
        (
            "#214F真是的……\x01",
            "别一副苦瓜脸啊！\x02\x03",

            "约修亚才不会让\x01",
            "那种眼镜男恣意操纵呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#1168F而且你和他约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "那么说的话……\x01",
            "他一定会恢复原样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        (
            "#1025F#5P科洛丝、乔丝特……\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#1161F#1K嗯！\x02",
    )


    ChrTalk(    #35
        0x10B,
        "#211F#1K嗯！\x02",
    )

    OP_56(0x1)
    OP_59()
    Jump("loc_1668")

    label("loc_F9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C7")

    ChrTalk(    #36
        0x107,
        (
            "#062F姐姐……你别担心。\x02\x03",

            "你不是和哥哥约好\x01",
            "要一起走到最后的吗？\x02\x03",

            "#560F那就没问题的……\x01",
            "他一定会复原的！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        (
            "#1025F#5P提妲……谢谢。\x02\x03",

            "#1012F是啊……\x01",
            "他可是个言出必行的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_10C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F3")

    ChrTalk(    #38
        0x103,
        (
            "#026F艾丝蒂尔……\x01",
            "别那么担心。\x02\x03",

            "#027F你和那孩子约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "那就没问题了……\x01",
            "他一定会复原的！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        (
            "#1025F#5P雪拉姐……谢谢。\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_11F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131F")

    ChrTalk(    #40
        0x109,
        (
            "#1065F艾丝蒂尔……\x01",
            "不用那么担心。\x02\x03",

            "#1060F你和约修亚约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "那就不要紧了。\x01",
            "他会恢复原样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1025F#5P凯文……谢谢。\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_131F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144D")

    ChrTalk(    #42
        0x106,
        (
            "#053F艾丝蒂尔……\x01",
            "别摆出那副表情。\x02\x03",

            "#556F你和那家伙约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "那就别担心了。\x01",
            "他肯定会复原的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #43
        0x101,
        (
            "#1025F#5P阿加特……谢谢。\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156F")

    label("loc_144D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(    #44
        0x108,
        (
            "#074F艾丝蒂尔……别担心。\x02\x03",

            "#070F你和约修亚约好\x01",
            "要一起走到最后的吧？\x02\x03",

            "那就不要紧了。\x01",
            "那家伙一定会复原的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #45
        0x101,
        (
            "#1025F#5P金……谢谢。\x02\x03",

            "#1012F是啊……\x01",
            "他不是会爽约的人。\x02\x03",

            "#1019F而且我也不会\x01",
            "让那个无视我们的\x01",
            "眼镜男为所欲为的……\x02\x03",

            "#1005F看我用少女的力量夺回他吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159F")

    ChrTalk(    #46
        0x108,
        "#071F对，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1668")

    label("loc_159F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D1")

    ChrTalk(    #47
        0x106,
        "#051F嘿嘿，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1668")

    label("loc_15D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1604")

    ChrTalk(    #48
        0x109,
        "#1061F哈哈，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1668")

    label("loc_1604")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(    #49
        0x103,
        "#021F呵呵，就是要这种精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1668")

    label("loc_1636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1668")

    ChrTalk(    #50
        0x107,
        (
            "#061F嘿嘿……\x01",
            "就是要这种精神！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(    #51
        0x104,
        (
            "#031F呵呵，万一不行的话\x01",
            "就交给我吧！\x02\x03",

            "我一定会用满溢的爱\x01",
            "让约修亚复原的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1016F#5P知道啦知道啦，拜托你了。\x02",
    )

    CloseMessageWindow()

    label("loc_16EC")

    OP_22(0x158, 0x1, 0x64)

    def lambda_16F7():

        label("loc_16F7")

        OP_7C(0xA, 0xA, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_16F7")

    QueueWorkItem2(0x101, 2, lambda_16F7)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174A")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_177E")

    label("loc_174A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176C")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_177E")

    label("loc_176C")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_177E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A5")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_17D9")

    label("loc_17A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C7")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_17D9")

    label("loc_17C7")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_17D9")

    Sleep(1000)

    ChrTalk(    #53
        0x101,
        "#1020F#5P这、这是什么声音……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(    #54
        0x107,
        "#065F……莫非。\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_1827")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184E")

    ChrTalk(    #55
        0x105,
        "#1163F莫非……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_184E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1878")

    ChrTalk(    #56
        0x10B,
        "#216F莫、莫非……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_1878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189E")

    ChrTalk(    #57
        0x103,
        "#023F莫非……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_189E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C5")

    ChrTalk(    #58
        0x109,
        "#1063F莫非……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_18C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EB")

    ChrTalk(    #59
        0x104,
        "#032F……莫非。\x02",
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_18EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_190E")

    ChrTalk(    #60
        0x106,
        "#052F莫非……！\x02",
    )

    CloseMessageWindow()

    label("loc_190E")

    Sleep(200)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x10E)

    def lambda_1977():
        OP_6D(-650, 6000, 5500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1977)

    def lambda_198F():
        OP_67(0, 4600, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_198F)

    def lambda_19A7():
        OP_6B(3880, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19A7)

    def lambda_19B7():
        OP_6C(27000, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_19B7)

    def lambda_19C7():
        OP_6E(449, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_19C7)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 0, 30000, 15980, 180)
    ClearChrFlags(0x8, 0x100)
    OP_D1(8, 0, -45000, 0, 100)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 320)
    OP_70(0x0, 0x154)

    def lambda_1A21():
        OP_8F(0xFE, 0x0, 0x3E8, 0x3E6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A21)

    def lambda_1A3C():
        OP_D1(254, 0, 180000, 0, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A3C)

    def lambda_1A56():
        OP_97(0xFE, 0xFFFFFFA6, 0x118, 0xB2390, 0x61A8, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1A56)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 0)
    Sleep(150)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 2)
    Sleep(100)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 4)

    def lambda_1A9F():

        label("loc_1A9F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1A9F")

    QueueWorkItem2(0x101, 0, lambda_1A9F)

    def lambda_1AB0():

        label("loc_1AB0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1AB0")

    QueueWorkItem2(0xF8, 0, lambda_1AB0)

    def lambda_1AC1():

        label("loc_1AC1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1AC1")

    QueueWorkItem2(0xF9, 0, lambda_1AC1)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)

    def lambda_1AE1():
        OP_8F(0xFE, 0xFFFFFF1A, 0x7D0, 0x17CA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AE1)

    def lambda_1AFC():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1AFC)
    OP_D8(0x0, 0x12C)
    OP_B0(0x0, 0xF)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 25)
    OP_70(0x0, 0x23)
    OP_73(0x0)
    OP_D8(0x0, 0x12C)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x14)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(1320, 2560, 4050, 0)
    OP_67(0, 2000, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(33000, 0)
    OP_6E(423, 0)
    OP_A1(0x9, 0x2)
    SetChrPos(0x9, -230, 2000, 6090, 0)
    ClearChrFlags(0x9, 0x100)
    OP_72(0x2, 0x4)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 300)
    OP_71(0x0, 0x4)
    OP_8C(0x9, 180, 0)

    def lambda_1BDF():
        OP_8F(0xFE, 0xFFFFFEF2, 0x546, 0x1748, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BDF)
    OP_6F(0x2, 300)
    OP_70(0x2, 0x136)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    Sleep(30)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(50)
    OP_43(0x101, 0x0, 0x0, 0x5)
    WaitChrThread(0x9, 0x1)
    OP_23(0x158)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x3E8)
    OP_44(0x101, 0x2)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x14)
    Sleep(1000)

    ChrTalk(    #61
        0x101,
        (
            "#1020F#6P竟、竟然还有一架……\x02\x03",

            "#1002F这……\x01",
            "看来只有正面应战了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDC")

    ChrTalk(    #62
        0x108,
        (
            "#076F#6P嗯……\x01",
            "拿出斗志来上吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D10")

    ChrTalk(    #63
        0x106,
        (
            "#054F#6P嗯……\x01",
            "拿出斗志上吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #64
        0x104,
        (
            "#035F#6P呼……\x01",
            "拿出斗志上吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7D")

    ChrTalk(    #65
        0x109,
        (
            "#1069F#6P嗯……\x01",
            "只有拿出斗志上了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB3")

    ChrTalk(    #66
        0x103,
        (
            "#024F#6P嗯……\x01",
            "拿出斗志上吧！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE7")

    ChrTalk(    #67
        0x10B,
        (
            "#214F#6P嗯……\x01",
            "拿出斗志上吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1DE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1B")

    ChrTalk(    #68
        0x105,
        (
            "#1162F#6P嗯……\x01",
            "拿出斗志来上了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1B")

    OP_22(0xF3, 0x0, 0x64)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 340)
    OP_70(0x2, 0x15E)

    def lambda_1E4F():
        OP_6D(810, 1350, 5810, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E4F)

    def lambda_1E67():
        OP_67(0, 4710, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E67)

    def lambda_1E7F():
        OP_6B(2440, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E7F)

    def lambda_1E8F():
        OP_8F(0xFE, 0xFFFFFEFC, 0x546, 0x92E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E8F)

    def lambda_1EAA():
        OP_8F(0xFE, 0xFFFFF8DA, 0x546, 0x5A0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1EAA)

    def lambda_1EC5():
        OP_8F(0xFE, 0x230, 0x546, 0x50A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1EC5)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_23(0x1C3)
    OP_23(0xEB)
    OP_23(0x79)
    OP_23(0x158)
    Battle(0x450, 0x0, 0x0, 0x80, 0xFF)
    Return()

    # Function_3_127 end

    def Function_4_1F0F(): pass

    label("Function_4_1F0F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    OP_D2(0x270110, 0x270120, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1F5A"),
        (5, "loc_1F67"),
        (3, "loc_1F74"),
        (4, "loc_1F81"),
        (6, "loc_1F8E"),
        (7, "loc_1F9B"),
        (8, "loc_1FA8"),
        (10, "loc_1FB5"),
        (SWITCH_DEFAULT, "loc_1FC2"),
    )


    label("loc_1F5A")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_1FC2")

    label("loc_1F67")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_1FC2")

    label("loc_1F74")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_1FC2")

    label("loc_1F81")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_1FC2")

    label("loc_1F8E")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_1FC2")

    label("loc_1F9B")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_1FC2")

    label("loc_1FA8")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_1FC2")

    label("loc_1FB5")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_1FC2")

    label("loc_1FC2")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1FEB"),
        (5, "loc_1FF8"),
        (3, "loc_2005"),
        (4, "loc_2012"),
        (6, "loc_201F"),
        (7, "loc_202C"),
        (8, "loc_2039"),
        (10, "loc_2046"),
        (SWITCH_DEFAULT, "loc_2053"),
    )


    label("loc_1FEB")

    OP_D2(0x701D0, 0x701DC, 0x4)
    Jump("loc_2053")

    label("loc_1FF8")

    OP_D2(0x70218, 0x70224, 0x4)
    Jump("loc_2053")

    label("loc_2005")

    OP_D2(0x701E8, 0x701F4, 0x4)
    Jump("loc_2053")

    label("loc_2012")

    OP_D2(0x27036E, 0x27037B, 0x4)
    Jump("loc_2053")

    label("loc_201F")

    OP_D2(0x70230, 0x7023C, 0x4)
    Jump("loc_2053")

    label("loc_202C")

    OP_D2(0x70248, 0x70254, 0x4)
    Jump("loc_2053")

    label("loc_2039")

    OP_D2(0x270176, 0x270183, 0x4)
    Jump("loc_2053")

    label("loc_2046")

    OP_D2(0x702B4, 0x702BB, 0x4)
    Jump("loc_2053")

    label("loc_2053")

    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 0, 1350, 2430, 0)
    OP_8C(0x8, 180, 0)
    ClearChrFlags(0x8, 0x100)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 260)
    OP_70(0x0, 0x104)
    OP_71(0x2, 0x4)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0xF8, 2)
    SetChrChipByIndex(0xF9, 4)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrPos(0x101, 0, 1350, -2880, 0)
    SetChrPos(0xF8, -820, 1350, -4370, 0)
    SetChrPos(0xF9, 820, 1350, -4370, 0)
    LoadEffect(0x1, "battle\\\\btbomb00.eff")
    LoadEffect(0x2, "monster\\\\ms30109a.eff")
    LoadEffect(0x3, "monster\\\\ms30109b.eff")
    OP_6D(-170, 3000, 3490, 0)
    OP_67(0, 2590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(308, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)

    def lambda_2184():
        OP_6D(-170, 4019, 12490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2184)

    def lambda_219C():
        OP_6B(4300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219C)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 260)
    OP_70(0x0, 0x136)
    PlayEffect(0x2, 0x0, 0x8, 180, 3800, 500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 180, 2560, 1060, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x0, 0x8, 180, 2300, 1400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 460, 3000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x8, 1000, 3500, 2500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x0, 0x8, 300, 3500, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x0, 0x8, 400, 1600, 4000, 0, 0, 0, 1300, 1067869798, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xFF, -750, 3000, 4150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x8, -1000, 3000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_23B4():
        OP_6D(-60, 1350, 12530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23B4)

    def lambda_23CC():
        OP_67(0, 22350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23CC)

    def lambda_23E4():
        OP_6B(500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23E4)

    def lambda_23F4():
        OP_6E(513, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_23F4)
    Sleep(900)
    PlayEffect(0x1, 0xFF, 0xFF, 840, 4500, 8400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_B0(0x0, 0x5)
    PlayEffect(0x1, 0xFF, 0xFF, -900, 2560, 10090, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, 0, 1350, 1000, 0)
    SetChrPos(0xF8, -1000, 1350, -1000, 0)
    SetChrPos(0xF9, 1000, 1350, -1000, 0)

    def lambda_24C7():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x2710, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_24C7)

    def lambda_24E2():
        OP_67(0, 23350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E2)

    def lambda_24FA():
        OP_6B(2600, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24FA)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetMapFlags(0x100000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5314   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1F0F end

    def Function_5_252B(): pass

    label("Function_5_252B")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xFFFFFEB6, 0x546, 0xFFFFF344, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_5_252B end

    def Function_6_254F(): pass

    label("Function_6_254F")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xFFFFF90C, 0x546, 0xFFFFECBE, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_6_254F end

    def Function_7_2573(): pass

    label("Function_7_2573")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xE6, 0x546, 0xFFFFEBA6, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_7_2573 end

    def Function_8_2597(): pass

    label("Function_8_2597")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_2611"),
        (1, "loc_2617"),
        (SWITCH_DEFAULT, "loc_261D"),
    )


    label("loc_2611")

    OP_A2(0x1200)
    Jump("loc_261D")

    label("loc_2617")

    OP_A2(0x1201)
    Jump("loc_261D")

    label("loc_261D")

    Return()

    # Function_8_2597 end

    def Function_9_261E(): pass

    label("Function_9_261E")

    FadeToDark(0, 0, -1)
    OP_6D(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_261E end

    SaveToFile()

Try(main)
