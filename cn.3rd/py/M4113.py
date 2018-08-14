from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4113   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4113.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 304880,
        TriggerZ            = 0,
        TriggerY            = -9060,
        TriggerRange        = 1000,
        ActorX              = 304880,
        ActorZ              = 2000,
        ActorY              = -9060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_EE",           # 01, 1
        "Function_2_11C",          # 02, 2
        "Function_3_977",          # 03, 3
        "Function_4_C0F",          # 04, 4
        "Function_5_CFE",          # 05, 5
        "Function_6_DBA",          # 06, 6
        "Function_7_ED0",          # 07, 7
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_E6"),
        (SWITCH_DEFAULT, "loc_ED"),
    )


    label("loc_E6")

    Event(0, 4)
    Jump("loc_ED")

    label("loc_ED")

    Return()

    # Function_0_CE end

    def Function_1_EE(): pass

    label("Function_1_EE")

    OP_16(0x2, 0xFA0, 0x2BF20, 0xFFFE1F88, 0x230066)
    OP_22(0x1CC, 0x0, 0x64)
    OP_1B(0x2, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B")
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x89, 0x0)

    label("loc_11B")

    Return()

    # Function_1_EE end

    def Function_2_11C(): pass

    label("Function_2_11C")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 315490, 10, -15990, 270)
    SetChrPos(0xEF, 316230, 10, -15050, 270)
    SetChrPos(0xF0, 316380, 10, -16890, 270)
    SetChrPos(0xF1, 317190, 10, -15900, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(288520, 2460, -10680, 0)
    OP_67(0, 9740, -10000, 0)
    OP_6B(4070, 0)
    OP_6C(140000, 0)
    OP_6E(401, 0)
    FadeToBright(2000, 0)

    def lambda_1E8():
        OP_6D(314160, 2460, -14030, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1E8)

    def lambda_200():
        OP_67(0, 8480, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_200)

    def lambda_218():
        OP_6B(3570, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_218)

    def lambda_228():
        OP_6C(142000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_228)

    def lambda_238():
        OP_6E(352, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_238)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(316540, 10, -16490, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(135000, 0)
    OP_6E(316, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 316320, 10, -16010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_2ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2ED)

    def lambda_2FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2FF)

    def lambda_311():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_311)

    def lambda_323():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_323)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF")

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF")

    label("loc_3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF")

    label("loc_3C8")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3DF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_473")

    label("loc_40C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_473")

    label("loc_434")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_473")

    label("loc_45C")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_473")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_507")

    label("loc_4A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_507")

    label("loc_4C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_507")

    label("loc_4F0")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_507")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E")

    ChrTalk(    #0
        0x105,
        (
            "#1164F#5P这里……\x01",
            "好像是罗马尔池啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_54E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_591")

    ChrTalk(    #1
        0x10E,
        (
            "#173F#5P这里……\x01",
            "好像是罗马尔池对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_591")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3")

    ChrTalk(    #2
        0x101,
        (
            "#1004F#5P这里……\x01",
            "不就是罗马尔池吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_5D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_615")

    ChrTalk(    #3
        0x102,
        (
            "#1504F#5P这里……\x01",
            "就是罗马尔池对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_662")

    ChrTalk(    #4
        0x110,
        (
            "#265F#5P哎呀……\x01",
            "这里好像是艾尔贝周游道的外围。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_662")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A7")

    ChrTalk(    #5
        0x108,
        (
            "#073F#5P这里……\x01",
            "应该就是周游道附近吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_6A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EC")

    ChrTalk(    #6
        0x106,
        (
            "#052F#5P这里……\x01",
            "应该就是周游道附近吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_6EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732")

    ChrTalk(    #7
        0x103,
        (
            "#1523F#5P这里……\x01",
            "好像是周游道的附近吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(    #8
        0x10A,
        (
            "#814F#5P这里……\x01",
            "好像是周游道的附近吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")

    ChrTalk(    #9
        0x10C,
        (
            "#113F#5P这里……\x01",
            "好像是罗马尔池对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_7BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_806")

    ChrTalk(    #10
        0x104,
        (
            "#1543F#5P哦……\x01",
            "好像来到艾尔贝周游道的附近了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(    #11
        0x107,
        (
            "#065F#5P这里……\x01",
            "好像是在王都附近的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_883")

    label("loc_84B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(    #12
        0x10F,
        "#1442F#5P……真漂亮的地方……\x02",
    )

    CloseMessageWindow()

    label("loc_883")


    ChrTalk(    #13
        0x109,
        (
            "#1065F#5P艾尔贝周游道……\x01",
            "利贝尔王家的离宫附近\x01",
            "也被再现了吗。\x02\x03",

            "#1063F既然是那些家伙准备的场景，\x01",
            "一定会有什么机关。\x02\x03",

            "我们先把现在能去的地方\x01",
            "都调查一遍看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B02)
    OP_28(0x37, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_2_11C end

    def Function_3_977(): pass

    label("Function_3_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A46")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(4864)
    Sleep(500)
    Jump("loc_A49")

    label("loc_A46")

    TalkBegin(0xFF)

    label("loc_A49")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_A73")

    label("loc_A73")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDE")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_AD8")

    label("loc_AD8")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AF5"),
        (1, "loc_B70"),
        (2, "loc_B9F"),
        (SWITCH_DEFAULT, "loc_BCE"),
    )


    label("loc_AF5")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xB7)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDB")

    label("loc_B70")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_B9C")

    label("loc_B9C")

    Jump("loc_BDB")

    label("loc_B9F")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_BCB")

    label("loc_BCB")

    Jump("loc_BDB")

    label("loc_BCE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDB")

    label("loc_BDB")

    Jump("loc_A86")

    label("loc_BDE")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0B")
    OP_A2(0x2596)
    EventEnd(0x1)
    Jump("loc_C0E")

    label("loc_C0B")

    TalkEnd(0xFF)

    label("loc_C0E")

    Return()

    # Function_3_977 end

    def Function_4_C0F(): pass

    label("Function_4_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C20")
    Call(0, 2)
    Return()

    label("loc_C20")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3, 317190, 10, -15900, 270)
    SetChrPos(0x2, 316380, 10, -16890, 270)
    SetChrPos(0x1, 316230, 10, -15050, 270)
    SetChrPos(0x0, 315490, 10, -15990, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 316320, 10, -16010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_4_C0F end

    def Function_5_CFE(): pass

    label("Function_5_CFE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, 317190, 10, -15900, 90)
    SetChrPos(0x1, 316380, 10, -16890, 90)
    SetChrPos(0x2, 316230, 10, -15050, 90)
    SetChrPos(0x3, 315490, 10, -15990, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 316320, 10, -16010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    NewScene("ED6_DT21/M7207   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_5_CFE end

    def Function_6_DBA(): pass

    label("Function_6_DBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE3")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DD7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DD7)

    label("loc_DE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0C")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E00)

    label("loc_E0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E35")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E29():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E29)

    label("loc_E35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E52)

    label("loc_E5E")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8A")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E8A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA1")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB8")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECF")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_ECF")

    Return()

    # Function_6_DBA end

    def Function_7_ED0(): pass

    label("Function_7_ED0")


    def lambda_ED6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ED6)

    def lambda_EE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EE8)

    def lambda_EFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EFA)

    def lambda_F0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F0C)
    Sleep(1000)
    Return()

    # Function_7_ED0 end

    SaveToFile()

Try(main)
