from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5314   ._SN',
        MapName             = 'Other',
        Location            = 'C5314.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60065",
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
        '升降梯',                               # 9
        '坏了的德尔基昂',                       # 10
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


    DeclActor(
        TriggerX            = 29120,
        TriggerZ            = 0,
        TriggerY            = 5080,
        TriggerRange        = 1200,
        ActorX              = 29120,
        ActorZ              = 0,
        ActorY              = 5080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_11D",          # 01, 1
        "Function_2_274",          # 02, 2
        "Function_3_B33",          # 03, 3
        "Function_4_BBA",          # 04, 4
        "Function_5_C4D",          # 05, 5
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_11C")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_11C")

    Return()

    # Function_0_10E end

    def Function_1_11D(): pass

    label("Function_1_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 5)), scpexpr(EXPR_END)), "loc_135")
    OP_72(0x0, 0x8)
    OP_6F(0x0, 300)
    OP_72(0x0, 0x20)

    label("loc_135")

    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xFA)
    Jump("loc_1AF")

    label("loc_1A3")

    OP_72(0x1, 0x20)
    OP_6F(0x1, 250)

    label("loc_1AF")

    SetChrPos(0x9, 4500, -9000, 24000, 260)
    OP_A1(0x9, 0x2)
    OP_72(0x2, 0x4)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 1150)
    LoadEffect(0x2, "map\\\\mpsmk0.eff")
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x2, 0xFF, 0x9, 4500, 3200, -3200, 0, 0, 0, 800, 1000, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x9, 11500, 2000, -200, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    SetMapFlags(0x2000000)
    Return()

    # Function_1_11D end

    def Function_2_274(): pass

    label("Function_2_274")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    Call(0, 3)
    Call(0, 4)
    RemoveParty(0x1, 0xFF)

    label("loc_28E")

    OP_6D(12460, 4000, 12240, 0)
    OP_67(0, 12140, -10000, 0)
    OP_6B(10700, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x14A)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, 880, 40000, 130, 90)
    OP_89(0xF8, -410, 40000, -520, 90)
    OP_89(0xF9, -330, 40000, 620, 90)
    OP_22(0xEB, 0x1, 0x64)
    ClearMapFlags(0x100000)
    FadeToBright(2000, 0)

    def lambda_33A():
        OP_6D(1960, 10, 2380, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33A)

    def lambda_352():
        OP_67(0, 6930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_352)
    OP_C8(0x200, 0x46, "C_PLAC28._CH", 0x0, 0x5DC)
    OP_73(0x0)
    OP_23(0xEB)
    OP_22(0xC8, 0x0, 0x64)

    def lambda_38A():
        OP_7C(0x0, 0x64, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_38A)
    OP_6F(0x0, 330)
    OP_70(0x0, 0x12C)
    OP_73(0x0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(220, 710, 270, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#1007F#5P总、总算……\x01",
            "来到了终点。\x02\x03",

            "#1002F这里……\x01",
            "就是『根源区域』吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A1")

    ChrTalk(    #1
        0x104,
        (
            "#032F#6P啊……一种压倒性的\x01",
            "力量从里面涌出来……\x02\x03",

            "看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_4A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_500")

    ChrTalk(    #2
        0x109,
        (
            "#1065F#6P啊……一种可怕的\x01",
            "力量从里面涌出来……\x02\x03",

            "#1063F看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55D")

    ChrTalk(    #3
        0x103,
        (
            "#026F#6P……一种压倒性的\x01",
            "力量从里面涌出来……\x02\x03",

            "#022F看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BC")

    ChrTalk(    #4
        0x105,
        (
            "#1167F#6P……一种压倒性的\x01",
            "力量从里面涌出来……\x02\x03",

            "#1162F看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_619")

    ChrTalk(    #5
        0x106,
        (
            "#053F#6P……一种压倒性的\x01",
            "力量从里面涌出来……\x02\x03",

            "#057F看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_676")

    ChrTalk(    #6
        0x108,
        (
            "#074F#6P……一种压倒性的\x01",
            "力量从里面涌出来……\x02\x03",

            "#072F看样子是没错了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8")

    ChrTalk(    #7
        0x10B,
        (
            "#216F#6P……从里面有\x01",
            "一股很厉害的力量涌出来……\x02\x03",

            "#212F……看样子是没错了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_729")

    ChrTalk(    #8
        0x107,
        (
            "#062F#6P那，那就是说…\x01",
            "约修亚哥哥\x01",
            "和『辉之环』就在前面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_775")

    ChrTalk(    #9
        0x10B,
        (
            "#212F#6P那、那就是说约修亚和\x01",
            "『辉之环』就在前面……  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_775")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #10
        0x108,
        (
            "#072F#6P『辉之环』\x01",
            "就在前面吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_7AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E5")

    ChrTalk(    #11
        0x106,
        (
            "#057F#6P『辉之环』\x01",
            "就在前面吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_7E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E")

    ChrTalk(    #12
        0x105,
        (
            "#1162F#6P那么……约修亚和\x01",
            "和『辉之环』就在前面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_866")

    ChrTalk(    #13
        0x103,
        (
            "#022F#6P『辉之环』\x01",
            "就在前面吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C")

    label("loc_866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #14
        0x109,
        (
            "#1063F#6P『辉之环』\x01",
            "就在前面吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C")


    ChrTalk(    #15
        0x101,
        (
            "#1002F#5P……………………………\x02\x03",

            "#1003F……这应该是\x01",
            "最后的战斗了吧。\x02\x03",

            "#1010F不管是为了阻止异变\x01",
            "而对付辉之环也好……\x02\x03",

            "为了从那个『白面』那里\x01",
            "救回约修亚也好……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #16
        0x101,
        (
            "#1005F#2P二位……\x01",
            "请将最后的力量借给我吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B3")

    ChrTalk(    #17
        0x108,
        "#070F#6P……明白！\x02",
    )

    CloseMessageWindow()

    label("loc_9B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DF")

    ChrTalk(    #18
        0x106,
        "#051F#6P不用你说我也会！\x02",
    )

    CloseMessageWindow()

    label("loc_9DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(    #19
        0x105,
        "#1168F#6P嗯……你不嫌弃的话！\x02",
    )

    CloseMessageWindow()

    label("loc_A10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3C")

    ChrTalk(    #20
        0x103,
        "#027F#6P呵呵……当然了！\x02",
    )

    CloseMessageWindow()

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A69")

    ChrTalk(    #21
        0x109,
        "#1061F#6P嘿嘿，交给我吧！\x02",
    )

    CloseMessageWindow()

    label("loc_A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A97")

    ChrTalk(    #22
        0x107,
        "#061F#6P嗯……我会努力的！\x02",
    )

    CloseMessageWindow()

    label("loc_A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC9")

    ChrTalk(    #23
        0x10B,
        "#210F#6P嘿嘿……真拿你没办法！\x02",
    )

    CloseMessageWindow()

    label("loc_AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(    #24
        0x104,
        (
            "#031F#6P哼哼……\x01",
            "我会奉献我全部的爱和力量！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B08")

    OP_A2(0x223D)
    OP_28(0x9F, 0x1, 0x2000)
    OP_28(0xA0, 0x4, 0x2)
    OP_28(0xA0, 0x4, 0x8)
    OP_28(0xA0, 0x1, 0x1)
    Sleep(100)
    Fade(1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_274 end

    def Function_3_B33(): pass

    label("Function_3_B33")

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
        (0, "loc_BAD"),
        (1, "loc_BB3"),
        (SWITCH_DEFAULT, "loc_BB9"),
    )


    label("loc_BAD")

    OP_A2(0x1200)
    Jump("loc_BB9")

    label("loc_BB3")

    OP_A2(0x1201)
    Jump("loc_BB9")

    label("loc_BB9")

    Return()

    # Function_3_B33 end

    def Function_4_BBA(): pass

    label("Function_4_BBA")

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

    # Function_4_BBA end

    def Function_5_C4D(): pass

    label("Function_5_C4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_E43")

    label("loc_C9E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E28")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_73(0x1)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x2BC)
    OP_71(0x1, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E42")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_E42")

    Return()

    label("loc_E43")

    Return()

    # Function_5_C4D end

    SaveToFile()

Try(main)
