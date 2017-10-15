from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4143   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4143.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Dalmore',                              # 9
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
        'ED6_DT07/CH02410 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
    )

    DeclNpc(
        X                   = -270,
        Z                   = 0,
        Y                   = 2120,
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


    DeclActor(
        TriggerX            = -440,
        TriggerZ            = 0,
        TriggerY            = 680,
        TriggerRange        = 400,
        ActorX              = -270,
        ActorZ              = 1500,
        ActorY              = 2120,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_11A",          # 01, 1
        "Function_2_11B",          # 02, 2
        "Function_3_120",          # 03, 3
        "Function_4_673",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_119")

    Return()

    # Function_0_F6 end

    def Function_1_11A(): pass

    label("Function_1_11A")

    Return()

    # Function_1_11A end

    def Function_2_11B(): pass

    label("Function_2_11B")

    Call(0, 3)
    Return()

    # Function_2_11B end

    def Function_3_120(): pass

    label("Function_3_120")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C")
    FadeToBright(300, 0)

    ChrTalk(    #0
        0x8,
        (
            "#660FEven the punishments of hell can\x01",
            "be bought off... Welcome to the\x01",
            "Dalmore Firm.\x02\x03",

            "Heh... If you want sepith, we can\x01",
            "provide as much as you might wish.\x02\x03",

            "Of course, we will require you to pay\x01",
            "appropriately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666")

    label("loc_24C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")

    label("loc_259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        65,
        1,
        (
            "Earth Sepith x100 - 3000 mira\x01",       # 0
            "Water Sepith x100 - 3000 mira\x01",       # 1
            "Fire Sepith x100 - 3000 mira\x01",        # 2
            "Wind Sepith x100 - 3000 mira\x01",        # 3
            "Time Sepith x100 - 3000 mira\x01",        # 4
            "Space Sepith x100 - 9000 mira\x01",       # 5
            "Mirage Sepith x100 - 6000 mira\x01",      # 6
            "Stop\x01",                                # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_393"),
        (1, "loc_3F2"),
        (2, "loc_451"),
        (3, "loc_4AF"),
        (4, "loc_50D"),
        (5, "loc_56B"),
        (6, "loc_5CA"),
        (SWITCH_DEFAULT, "loc_62A"),
    )


    label("loc_393")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B9")

    AnonymousTalk(    #1
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_3EC")

    label("loc_3B9")

    SubMira(3000)
    AddSepith(0x0, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "Bought #5C#56I Earth Sepith#0C x100.\x02",
    )


    label("loc_3EC")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_3F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_418")

    AnonymousTalk(    #3
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_44B")

    label("loc_418")

    SubMira(3000)
    AddSepith(0x1, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "Bought #5C#57I Water Sepith#0C x100.\x02",
    )


    label("loc_44B")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_451")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_477")

    AnonymousTalk(    #5
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_4A9")

    label("loc_477")

    SubMira(3000)
    AddSepith(0x2, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #6
        "Bought #5C#58I Fire Sepith#0C x100.\x02",
    )


    label("loc_4A9")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_4AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D5")

    AnonymousTalk(    #7
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_507")

    label("loc_4D5")

    SubMira(3000)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #8
        "Bought #5C#59I Wind Sepith#0C x100.\x02",
    )


    label("loc_507")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_50D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_533")

    AnonymousTalk(    #9
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_565")

    label("loc_533")

    SubMira(3000)
    AddSepith(0x4, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "Bought #5C#62I Time Sepith#0C x100.\x02",
    )


    label("loc_565")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_56B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_591")

    AnonymousTalk(    #11
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_5C4")

    label("loc_591")

    SubMira(9000)
    AddSepith(0x5, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "Bought #5C#60I Space Sepith#0C x100.\x02",
    )


    label("loc_5C4")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_5CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F0")

    AnonymousTalk(    #13
        "\x07\x00Insufficient mira.\x02",
    )

    Jump("loc_624")

    label("loc_5F0")

    SubMira(6000)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "Bought #5C#61I Mirage Sepith#0C x100.\x02",
    )


    label("loc_624")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_637")

    label("loc_62A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_637")

    label("loc_637")

    Jump("loc_259")

    label("loc_63A")

    FadeToBright(300, 0)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_666")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_666")

    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_120 end

    def Function_4_673(): pass

    label("Function_4_673")

    EventBegin(0x0)
    OP_6D(1170, -250, -1690, 0)
    OP_67(0, 5380, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -570, -250, -2430, 0)
    SetChrPos(0x102, 470, -250, -2600, 0)
    SetChrPos(0xF8, -570, -250, -3710, 0)
    SetChrPos(0xF9, 520, -250, -3790, 0)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729")
    SetChrPos(0xF9, -570, -250, -3710, 0)
    SetChrPos(0xF8, 520, -250, -3790, 0)

    label("loc_729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    SetChrPos(0xF9, -570, -250, -3710, 0)
    SetChrPos(0xF8, 520, -250, -3790, 0)

    label("loc_758")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x101,
        "#1015F#2PHuh, was there a store here?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x8,
        "Clerk",
        "Welcome...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)
    Sleep(500)

    def lambda_7D6():
        OP_8E(0xFE, 0xFFFFFC54, 0x0, 0xF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D6)
    Sleep(50)

    def lambda_7F6():
        OP_8E(0xFE, 0xDC, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F6)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860")

    def lambda_823():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_823)
    Sleep(70)

    def lambda_843():
        OP_8E(0xFE, 0xFA, 0x0, 0xFFFFFBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_843)
    Sleep(50)
    Jump("loc_8F0")

    label("loc_860")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")

    def lambda_873():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_873)
    Sleep(70)

    def lambda_893():
        OP_8E(0xFE, 0xFA, 0x0, 0xFFFFFBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_893)
    Sleep(50)
    Jump("loc_8F0")

    label("loc_8B0")


    def lambda_8B6():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8B6)
    Sleep(70)

    def lambda_8D6():
        OP_8E(0xFE, 0xFA, 0x0, 0xFFFFFBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8D6)
    Sleep(50)

    label("loc_8F0")


    def lambda_8F6():
        OP_6D(530, 0, 1970, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F6)

    def lambda_90E():
        OP_67(0, 4900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_90E)

    def lambda_926():
        OP_6B(2830, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_926)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x3)
    Sleep(300)

    ChrTalk(    #17
        0x101,
        "#1000F#6PExcuse me, sir. What kind of store is this?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(    #18
        0x8,
        "Clerk",
        "#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000F#6PUm--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1042FI didn't expect to meet you here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #21
        0x101,
        "#1004F#6POh, do you know him, Joshua?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #22
        0x102,
        (
            "#1043F#4PEstelle, you know this person as\x01",
            "well as I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1005FI do?! Is he with the society?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#1035F#4PNo, not quite.\x02\x03",

            "#1042FSo, if you don't mind, I'd like to hear\x01",
            "the details...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    OP_21()

    ChrTalk(    #25
        0x102,
        "#1042F#4PFormer mayor of Ruan...Mister Dalmore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1004F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #27
        0x8,
        "Clerk",
        "#3PTch...\x02",
    )

    CloseMessageWindow()
    OP_1D(0x57)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #28
        0x101,
        "#1005FWh-Why are you here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1042FI believe you are supposed to be\x01",
            "in holding at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#666F#3PThat's true, but do not misunderstand.\x02\x03",

            "#664FI am here with ALL proper permissions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1009F#6PProper permissions? Yeah, THAT'S not\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "#666F#3PH-How rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1005F#6PConsidering what happened in Ruan,\x01",
            "asking me to believe you would insane!\x02\x03",

            "After what you did to innocent children!\x01",
            "ORPHANS, I MIGHT ADD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#663F#3PErm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        (
            "#1035FEstelle, let's hear him out first.\x02\x03",

            "#1042FWe can decide if he's worth trusting\x01",
            "after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1009FUgh. Fine.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #37
        0x8,
        (
            "#666F#3PYou must understand that I, too,\x01",
            "am a victim of that case.\x02\x03",

            "After all, my memories of that period\x01",
            "are quite vague, as if I were controlled\x01",
            "by someone.\x02\x03",

            "On top of that, I had to pay an enormous\x01",
            "bail from what little fortune I had left to\x01",
            "my name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#1044FI see, that's why...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #39
        0x101,
        "#1015F#6PBail? What's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1035F#4PIt means that by paying a certain\x01",
            "amount of money, you can be set free\x01",
            "until your guilt has been proven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1004F#6PSo what, any bad deed can be\x01",
            "forgiven with money?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#1042F#4PNothing is forgiven.\x02\x03",

            "Liberl's justice system works on a\x01",
            "principle of innocent until proven guilty.\x02\x03",

            "Until your guilt is established, you are granted\x01",
            "personal freedom by paying a heavy amount of\x01",
            "mira to act as assurance against your fleeing.\x02\x03",

            "#1035FOf course, you're not permitted to leave the\x01",
            "area or hide during that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "#664F#3PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1019F#6PHmmm. I'm still not digging it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1042F#4PBasically, it means that it's not that\x01",
            "impossible for Dalmore to be here.\x02\x03",

            "It is true that there were also\x01",
            "extenuating circumstances...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #46
        0x101,
        "#1015F#6PBut what are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#662F#3PAs you see.\x02\x03",

            "To rebuild the Dalmore family,\x01",
            "I intend to make a new start.\x02\x03",

            "First, I am starting a business here\x01",
            "to save money towards rebuilding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1019F#6PA business?\x02\x03",

            "#1015FSo what kind of store is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#664F#3PSepith.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1004F#6PSepith?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#662F#3PYes, there is no store anywhere in\x01",
            "Liberl that trades in sepith.\x02\x03",

            "Quite the genius venture, if I do say\x01",
            "so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1044FYou're right...\x02\x03",

            "#1042FStill, wouldn't it be difficult to get enough\x01",
            "sepith to actually run a business on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#663F#3PA-Ahem!\x02\x03",

            "#664FI have my own secret channels to\x01",
            "procure stock through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1019F#6PAaaand there he goes with the\x01",
            "suspicious stuff again...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x1A)
    OP_A2(0x20EE)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_4_673 end

    SaveToFile()

Try(main)
