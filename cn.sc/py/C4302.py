from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C4302   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4302.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60033",
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
        '凯文神父',                             # 9
        '尤莉亚上尉',                           # 10
        '升降机用',                             # 11
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 7320,
        TriggerZ            = 0,
        TriggerY            = 38820,
        TriggerRange        = 1000,
        ActorX              = 7320,
        ActorZ              = 1000,
        ActorY              = 38820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13E",          # 00, 0
        "Function_1_148",          # 01, 1
        "Function_2_1AD",          # 02, 2
        "Function_3_73C",          # 03, 3
        "Function_4_869",          # 04, 4
        "Function_5_8BE",          # 05, 5
    )


    def Function_0_13E(): pass

    label("Function_0_13E")

    SetMapFlags(0x10000000)
    Event(0, 2)
    Return()

    # Function_0_13E end

    def Function_1_148(): pass

    label("Function_1_148")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A0")
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_72(0x7, 0x20)
    OP_6F(0x7, 250)

    label("loc_1AC")

    Return()

    # Function_1_148 end

    def Function_2_1AD(): pass

    label("Function_2_1AD")

    ClearMapFlags(0x1)
    ClearMapFlags(0x80)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x10A, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    OP_6D(250, 34000, -61740, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(20000, 0)
    OP_6E(389, 0)
    SetChrName("正文（肖像表示）")
    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 0, 50000, -61960, 0)
    OP_72(0x0, 0x4)
    OP_48()
    OP_89(0x8, 800, 70000, -62000, 0)
    OP_89(0x9, -800, 70000, -62000, 0)
    OP_43(0xA, 0x1, 0x0, 0x3)
    OP_C8(0x200, 0x46, "C_PLAC03._CH", 0x1, 0x5DC)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1500, 0)

    def lambda_2B2():
        OP_6D(250, -4000, -61740, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B2)

    def lambda_2CA():
        OP_67(0, 9500, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CA)

    def lambda_2E2():
        OP_6B(3200, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E2)

    def lambda_2F2():
        OP_6E(262, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F2)

    def lambda_302():
        OP_6C(45000, 11000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_302)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_326():
        OP_8E(0x9, 0xFFFFFCE0, 0xFFFFF060, 0xFFFF141A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_326)

    def lambda_341():
        OP_6D(300, -4000, -58390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_341)

    def lambda_359():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_359)
    Sleep(500)

    def lambda_376():
        OP_8E(0x8, 0x320, 0xFFFFF060, 0xFFFF13CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_376)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 260, 500)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#2P#1068F呼～话说回来\x01",
            "还真是相当棘手呢。\x02\x03",

            "两条腿快要酸死了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(500)

    ChrTalk(    #1
        0x9,
        (
            "#170F#6P呵呵，安心吧。\x02\x03",

            "这里是『封印区域』的最下层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#2P#1062F哇，真的吗！？\x02\x03",

            "#1061F哈哈～我还在想，如果你要是说\x01",
            "“刚走了一半”的话该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#176F#6P呵呵，您谦虚了。\x02\x03",

            "#170F神父你作为圣职者，\x01",
            "看来却经过相当的锻炼。\x02\x03",

            "否则可无法胜任\x01",
            "你的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#2P#1068F真是服了你了。\x02\x03",

            "#1062F不过……也好。\x01",
            "利贝尔王家似乎和我们\x01",
            "从以前开始就渊源颇深。\x02\x03",

            "#1060F对了，上尉，\x01",
            "关于市长的那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#170F#6P啊啊，『封印宝杖』吧。\x02\x03",

            "我们遵从盟约，以指定的方法\x01",
            "正在严加保管中。\x02\x03",

            "随时都可以交给你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#2P#1061F感激不尽，真是帮大忙了。\x02\x03",

            "#1060F那么……\x01",
            "能把那个东西给我看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        "#178F#6P啊──在这里。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 500)
    SetChrFlags(0x9, 0x40)

    def lambda_667():
        OP_8E(0x9, 0xFFFFFFC4, 0xFFFFF060, 0xFFFF1AFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_667)
    Sleep(500)
    OP_8C(0x8, 0, 500)
    SetChrFlags(0x8, 0x40)

    def lambda_693():
        OP_8E(0x8, 0xFFFFFFC4, 0xFFFFF060, 0xFFFF1AFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_693)
    WaitChrThread(0x9, 0x0)

    def lambda_6B3():
        OP_8E(0x9, 0x46, 0xFFFFF060, 0xFFFF5B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6B3)

    def lambda_6CE():
        OP_6D(100, -4000, -48210, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CE)

    def lambda_6E6():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E6)
    WaitChrThread(0x8, 0x0)

    def lambda_703():
        OP_8E(0x8, 0x46, 0xFFFFF060, 0xFFFF5B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_703)
    Sleep(2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    NewScene("ED6_DT21/C4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1AD end

    def Function_3_73C(): pass

    label("Function_3_73C")


    def lambda_742():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_742)
    Sleep(8500)

    def lambda_762():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_762)
    Sleep(500)

    def lambda_782():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_782)
    Sleep(500)

    def lambda_7A2():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_7A2)
    OP_43(0xA, 0x2, 0x0, 0x4)
    Sleep(300)

    def lambda_7C9():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_7C9)
    Sleep(200)

    def lambda_7E9():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_7E9)
    Sleep(200)

    def lambda_809():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_809)
    Sleep(100)

    def lambda_829():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_829)
    Sleep(100)

    def lambda_849():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_849)
    Sleep(100)
    WaitChrThread(0xA, 0x0)
    Return()

    # Function_3_73C end

    def Function_4_869(): pass

    label("Function_4_869")

    OP_24(0xEB, 0x5A)
    Sleep(300)
    OP_24(0xEB, 0x50)
    Sleep(300)
    OP_24(0xEB, 0x46)
    Sleep(300)
    OP_24(0xEB, 0x3C)
    Sleep(200)
    OP_24(0xEB, 0x32)
    Sleep(200)
    OP_24(0xEB, 0x28)
    Sleep(200)
    OP_24(0xEB, 0x1E)
    Sleep(100)
    OP_24(0xEB, 0x14)
    Sleep(100)
    OP_24(0xEB, 0xA)
    Sleep(100)
    OP_23(0xEB)
    Return()

    # Function_4_869 end

    def Function_5_8BE(): pass

    label("Function_5_8BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_AB4")

    label("loc_90F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A99")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 300)
    OP_70(0x7, 0x1F4)
    OP_73(0x7)
    OP_6F(0x7, 500)
    OP_70(0x7, 0x2BC)
    OP_71(0x7, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x5, 0x6, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_AB3")

    Return()

    label("loc_AB4")

    Return()

    # Function_5_8BE end

    SaveToFile()

Try(main)
