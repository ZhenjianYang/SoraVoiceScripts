from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Nial',                                 # 11
        'Dorothy',                              # 12
        'Target Camera',                        # 13
        'Grancel - North Block',                # 14
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT06/CH20122 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT06/CH20122P._CP',             # 03
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1C6",          # 02, 2
        "Function_3_1CD",          # 03, 3
        "Function_4_1D4",          # 04, 4
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1B2")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1B2")

    Return()

    # Function_0_18A end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    Return()

    # Function_1_1B3 end

    def Function_2_1C6(): pass

    label("Function_2_1C6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_2_1C6 end

    def Function_3_1CD(): pass

    label("Function_3_1CD")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_1CD end

    def Function_4_1D4(): pass

    label("Function_4_1D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00\x18#20W#5S#20ABreaking news!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#20W       #4SLiberl News - Special Issue#3S\x01\x01",
            "[The Flying City Falls! Liberl is Safe Once More!]#2S\x01\x01",
            "Glory to the young bracers who saved us all from crisis!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_B8(0x326, 0xFF)
    Sleep(2000)
    OP_22(0x1CC, 0x1, 0x64)
    OP_1D(0x11)
    OP_6D(3000, 0, -9940, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 3000, 0, -20900, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_386():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2EE0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_386)
    Sleep(1000)

    def lambda_3A6():
        OP_6D(3000, 0, 12200, 6300)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3A6)

    def lambda_3BE():
        OP_67(0, 5500, -10000, 6300)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3BE)

    def lambda_3D6():
        OP_6C(0, 6300)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3D6)

    def lambda_3E6():
        OP_6B(3300, 6300)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_3E6)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    def lambda_445():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_445)

    ChrTalk(    #2
        0x12,
        "#145F#5P#40W*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    def lambda_483():
        OP_6D(4200, 0, 12200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_483)

    def lambda_49B():
        OP_67(0, 6020, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_49B)

    def lambda_4B3():
        OP_6C(50000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4B3)

    def lambda_4C3():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4C3)
    OP_8C(0x12, 180, 300)
    Sleep(300)

    ChrTalk(    #3
        0x12,
        (
            "#144F#5P#3SWhat's taking you so long, Dorothy?!#2S\x02\x03",

            "#3SGet a move on, or I'm gonna leave you behind!#2S\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, 3000, 0, 1100, 0)

    def lambda_578():
        OP_8E(0xFE, 0xBB8, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_578)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #4
        0x13,
        (
            "#152F#3PW-Waaaaaait...\x01",
            "Wait for meeeeee...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C8():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2008, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5C8)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    def lambda_5ED():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2904, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5ED)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    ChrTalk(    #5
        0x12,
        (
            "#144F#5PNo time for waiting! If we take much longer,\x01",
            "the banquet's going to start without us!\x02\x03",

            "#142FWe're talkin' about a big celebration held by\x01",
            "the queen, here!\x02\x03",

            "Being late isn't an option!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x13,
        "#156F#12P#40WB-But I'm so hungry...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x20)
    Sleep(1200)

    def lambda_72D():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_72D)

    ChrTalk(    #7
        0x13,
        "#152F#12P#40WI can't walk another step...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(300)

    ChrTalk(    #8
        0x12,
        (
            "#145F#5P...I have a horrible feeling I know what's going\x01",
            "on here.\x02\x03",

            "#142FYou skipped lunch so you could eat more at the\x01",
            "banquet, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#154F#12PI didn't even eat breakfast... I haven't eaten a\x01",
            "thing since yesterdaaay...\x02\x03",

            "#152FGoing thirty hours without eating is making me \x01",
            "feel all kinds of lightheaded...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x12,
        "#144F#5P#3SWhat the hell were you THINKING?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        "#152F#12PI can't mooove... Carry meee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        "#145F#5PHell no!\x02",
    )

    CloseMessageWindow()

    def lambda_97A():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_97A)
    WaitChrThread(0x12, 0x1)
    Sleep(200)
    OP_8C(0x12, 0, 400)
    Sleep(500)

    ChrTalk(    #13
        0x12,
        (
            "#144F#5PCome on--we're going! There's no way we can\x01",
            "miss an occasion like this! There's gonna be\x01",
            "Aidios-knows-how-many famous people there!\x02\x03",

            "#141FFirst on the agenda is snapping a photo of Her\x01",
            "Majesty and the crown princess, and THEN...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A9D():
        OP_8E(0xFE, 0xBB8, 0x0, 0x32C8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A9D)

    def lambda_AB8():
        OP_8E(0xFE, 0xBB8, 0x0, 0x300C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_AB8)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #14
        0x13,
        "#152F#12P#40WUuuuuuhhh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x13,
        (
            "#153F#12P...H-Huh?\x02\x03",

            "#151FThis actually isn't so bad. ㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B50():
        OP_8E(0xFE, 0xBB8, 0x0, 0x7DC8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B50)

    def lambda_B6B():
        OP_8E(0xFE, 0xBB8, 0x0, 0x57E4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B6B)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x13, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1D4 end

    SaveToFile()

Try(main)
