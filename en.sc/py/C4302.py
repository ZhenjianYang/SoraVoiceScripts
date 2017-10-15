from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Kevin',                                # 9
        'Julia',                                # 10
        'Elevator',                             # 11
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
        "Function_3_90F",          # 03, 3
        "Function_4_A3C",          # 04, 4
        "Function_5_A91",          # 05, 5
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
    SetChrName("テキスト（ポートレイト表示）")
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

    def lambda_2BE():
        OP_6D(250, -4000, -61740, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2BE)

    def lambda_2D6():
        OP_67(0, 9500, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D6)

    def lambda_2EE():
        OP_6B(3200, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EE)

    def lambda_2FE():
        OP_6E(262, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FE)

    def lambda_30E():
        OP_6C(45000, 11000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_30E)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_332():
        OP_8E(0x9, 0xFFFFFCE0, 0xFFFFF060, 0xFFFF141A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_332)

    def lambda_34D():
        OP_6D(300, -4000, -58390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34D)

    def lambda_365():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_365)
    Sleep(500)

    def lambda_382():
        OP_8E(0x8, 0x320, 0xFFFFF060, 0xFFFF13CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_382)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 260, 500)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#1068F#4PAi-diiiios, that was one heck of a trip!\x02\x03",

            "If it's much further I think\x01",
            "my legs are gonna pop off...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(500)

    ChrTalk(    #1
        0x9,
        (
            "#170F#1PWell, you can relax now.\x02\x03",

            "This is the lowest floor of\x01",
            "the Sealed Area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#1062F#4PWait, really?!\x02\x03",

            "#1061FAhhhh, thank the Goddess! If you told me\x01",
            "we were only halfway down, I think I'd be\x01",
            "floatin' off to meet Her right about now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#176F#1PReally, Father Kevin, you're\x01",
            "being a little too humble.\x02\x03",

            "#170FI can tell you're extremely\x01",
            "well-trained for a...'priest.'\x02\x03",

            "If you were not, I doubt you\x01",
            "could do the job you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#1068F#4PAhh, ka-zing. Read like a book!\x01",
            "A children's book, at that!\x02\x03",

            "#1062FWell, it's no big if you figured it out. We're\x01",
            "close to the von Auslese family anyway.\x02\x03",

            "#1060FOh, speaking of my job.\x01",
            "That thing the mayor of Ruan had...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#170F#1PAh, the 'Chronos Rod.'\x02\x03",

            "In accordance with our pact, it's\x01",
            "being kept safely secured using\x01",
            "the prescribed methods.\x02\x03",

            "We can hand it off to you\x01",
            "whenever you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#1061F#4PPerfect, perfect. Thanks!\x02\x03",

            "#1060FSo anyway, the thing we discussed earlier.\x01",
            "Mind showing it to me? It's down here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        "#178F#1PYes. Follow me...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 500)
    SetChrFlags(0x9, 0x40)

    def lambda_83A():
        OP_8E(0x9, 0xFFFFFFC4, 0xFFFFF060, 0xFFFF1AFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_83A)
    Sleep(500)
    OP_8C(0x8, 0, 500)
    SetChrFlags(0x8, 0x40)

    def lambda_866():
        OP_8E(0x8, 0xFFFFFFC4, 0xFFFFF060, 0xFFFF1AFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_866)
    WaitChrThread(0x9, 0x0)

    def lambda_886():
        OP_8E(0x9, 0x46, 0xFFFFF060, 0xFFFF5B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_886)

    def lambda_8A1():
        OP_6D(100, -4000, -48210, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A1)

    def lambda_8B9():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B9)
    WaitChrThread(0x8, 0x0)

    def lambda_8D6():
        OP_8E(0x8, 0x46, 0xFFFFF060, 0xFFFF5B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8D6)
    Sleep(2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    NewScene("ED6_DT21/C4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1AD end

    def Function_3_90F(): pass

    label("Function_3_90F")


    def lambda_915():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_915)
    Sleep(8500)

    def lambda_935():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_935)
    Sleep(500)

    def lambda_955():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_955)
    Sleep(500)

    def lambda_975():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_975)
    OP_43(0xA, 0x2, 0x0, 0x4)
    Sleep(300)

    def lambda_99C():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_99C)
    Sleep(200)

    def lambda_9BC():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9BC)
    Sleep(200)

    def lambda_9DC():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9DC)
    Sleep(100)

    def lambda_9FC():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9FC)
    Sleep(100)

    def lambda_A1C():
        OP_8F(0xFE, 0x0, 0xFFFFEA84, 0xFFFF0DF8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_A1C)
    Sleep(100)
    WaitChrThread(0xA, 0x0)
    Return()

    # Function_3_90F end

    def Function_4_A3C(): pass

    label("Function_4_A3C")

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

    # Function_4_A3C end

    def Function_5_A91(): pass

    label("Function_5_A91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF7")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_C99")

    label("loc_AF7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7E")
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

    label("loc_C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C98")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_C98")

    Return()

    label("loc_C99")

    Return()

    # Function_5_A91 end

    SaveToFile()

Try(main)
