from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1121   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Lugran',                               # 9
        'Letter',                               # 10
        'Mayor Maybelle',                       # 11
        'Anelace',                              # 12
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


    AddCharChip(
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT27/CH03093 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT07/CH02363 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT27/CH03093P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT07/CH02363P._CP',             # 03
    )

    DeclNpc(
        X                   = 180,
        Z                   = 0,
        Y                   = 4400,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966082,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1B1",          # 01, 1
        "Function_2_1B2",          # 02, 2
        "Function_3_D4F",          # 03, 3
        "Function_4_D9E",          # 04, 4
        "Function_5_DC7",          # 05, 5
        "Function_6_1349",         # 06, 6
        "Function_7_30DB",         # 07, 7
        "Function_8_3938",         # 08, 8
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_175")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_191")

    label("loc_175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_191")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1B0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_1B0")

    Return()

    # Function_0_14A end

    def Function_1_1B1(): pass

    label("Function_1_1B1")

    Return()

    # Function_1_1B1 end

    def Function_2_1B2(): pass

    label("Function_2_1B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27740, 200, -2390, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 25400, 800, -3800, 0)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05Anelace Elfead was a bracer affiliated with the\x01",
            "Bose branch of the Bracer Guild.\x02\x03",

            "For her achievements during the Liber Ark crisis,\x01",
            "she was promoted to D rank, and was now seen as \x01",
            "one of the guild's most promising youngsters.\x02\x03",

            "But the peaceful days that followed were shattered\x01",
            "by the sudden arrival of a letter...\x02\x03",

            "A letter she now sat staring at inside the somber\x01",
            "afternoon guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_1D(0xB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #1
        0x10A,
        (
            "#810F#5PHmm...\x02\x03",

            "Hmm...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_400():
        OP_6D(28150, 0, 630, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_400)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(200)

    ChrTalk(    #2
        0x10,
        (
            "#630FWhat's up with you, Anelace?\x02\x03",

            "You haven't made yourself sick by eating too much\x01",
            "ice cream again, have you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00◆Anelace looks over at Lugran.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #4
        0x10A,
        (
            "#810FY-You were supposed to forget about that!\x02\x03",

            "Anyway, I got a letter from my granddad, you\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_55E():
        OP_6D(27760, 200, -1960, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_55E)

    def lambda_576():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_576)
    OP_43(0x10, 0x0, 0x0, 0x4)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #5
        0x10,
        (
            "#630F#5POh, really?\x02\x03",

            "Wasn't your grandfather...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10A,
        (
            "#810FYep, he's a really famous swordsmanship \x01",
            "instructor.\x02\x03",

            "Even now, every time we get the chance to fight, \x01",
            "I feel like I'm just being treated like a child. \x01",
            "He's an old man now, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#630F#5PHaha. He really must be skilled to be treating \x01",
            "an active bracer that way.\x02\x03",

            "...Anyway, what exactly does he want with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#810FW-Well, as surprising as it is...\x02\x03",

            "He actually wants me to go and speak to Cassius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#630F#5PCassius?\x02\x03",

            "As in Brigadier General Bright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        (
            "#810FY-Yeah...\x02\x03",

            "Apparently Granddad is like a master to Cassius...\x02\x03",

            "Apparently he even came to see him when he stopped\x01",
            "fighting with a sword ten years ago, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#630F#5PTen years ago? So around the time of the Hundred\x01",
            "Days War, then.\x02\x03",

            "Back when Cassius left the army and became a\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#810FGranddad seems to have been really disappointed\x01",
            "that Cassius abandoned the path of the sword,\x01",
            "too.\x02\x03",

            "So now that he's returned to the army, Granddad\x01",
            "wants to know whether his feelings have changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#630F#5PHmm... I see...\x02\x03",

            "It really is surprising how people can end up\x01",
            "knowing one another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        (
            "#810FY-Yeah, it is...\x02\x03",

            "Anyway, that said... Umm...\x02\x03",

            "I kind of have a favor to ask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#630F#5PYou want time off, I assume?\x02\x03",

            "Well, I certainly don't mind. You've got good\x01",
            "cause to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        "#810FR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#630F#5PBut in return...\x02\x03",

            "I want you to take care of every single one of the\x01",
            "monster extermination requests on the board.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x10A,
        (
            "#810FE-Every single one?!\x02\x03",

            "Aren't there like five of them in all at the\x01",
            "moment?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#630F#5PI don't want to hear any complaints from someone\x01",
            "who had to take a day off three days ago because\x01",
            "they ate too much ice cream.\x02\x03",

            "Especially considering they were only eating that\x01",
            "many because they wanted the bonus goods that came\x01",
            "with the things...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x10A,
        (
            "#810FA-Aaaaah!\x02\x03",

            "O-Okay, okay, I'll do it! I'll do it! Just stop!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x3E8)
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B2 end

    def Function_3_D4F(): pass

    label("Function_3_D4F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25510, -1750, 5500, 0)

    def lambda_D76():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D76)
    OP_8E(0xFE, 0x70D0, 0x0, 0x14BE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_D4F end

    def Function_4_D9E(): pass

    label("Function_4_D9E")

    OP_8E(0xFE, 0x684C, 0x0, 0x4F6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x681A, 0x0, 0xFFFFF7F4, 0x9C4, 0x0)
    Return()

    # Function_4_D9E end

    def Function_5_DC7(): pass

    label("Function_5_DC7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27220, 0, -2090, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 25330, 0, -2450, 180)
    Sleep(100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05...Anyway, Granddad.\x02\x03",

            "I'm afraid it doesn't look like Cassius has any\x01",
            "interest at all in taking up a sword again.\x02\x03",

            "Still, going to speak to him wasn't all for \x01",
            "naught. I feel like I've learned more about\x01",
            "swordsmanship myself by doing so.\x02\x03",

            "Up until now, I thought it was all about getting\x01",
            "stronger, or faster, or things like that...\x02\x03",

            "But now I've finally realized that what's far more\x01",
            "important than either of those things is why you\x01",
            "take up your sword -- your soul and your feelings.\x02\x03",

            "I feel like now I finally understand why I was\x01",
            "never able to defeat you, no matter how many \x01",
            "times we fought.\x02\x03",

            "Of course, I hardly expect this revelation will\x01",
            "allow me to suddenly be able to win against you,\x01",
            "but hopefully you'll watch over me until I can.\x02\x03",

            "Hopefully when you end up going to heaven, you'll\x01",
            "watch over me from there, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #22
        0x10A,
        (
            "#810F#2P...That was what the letter I sent said, but he\x01",
            "wasn't too impressed with it.\x02\x03",

            "He got really angry... I wonder why?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x10,
        "#630F#5PI'll give you a clue... It's the last two lines...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")
    OP_28(0xA, 0x4, 0x20)
    OP_3E(0x590, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05Obtained \x1F\x90\x05\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_12F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1331")
    OP_28(0xA, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x05Obtained \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_1331")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5502   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_DC7 end

    def Function_6_1349(): pass

    label("Function_6_1349")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(27740, 200, -2390, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 0)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 26740, 200, -3610, 270)
    FadeToBright(2000, 0)
    OP_6B(2480, 2000)
    OP_0D()
    OP_62(0x10A, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #26
        0x10A,
        (
            "#818F#11PHmm...\x02\x03",

            "#817FInteresting...\x02\x03",

            "#814F...\x02\x03",

            "#1311FWow, that's a surprise...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 25510, -1750, 5500, 0)

    NpcTalk(    #27
        0x10,
        "Old Man's Voice",
        "#2PAnelace!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_14A2():
        OP_6D(28150, 0, 630, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_14A2)
    OP_43(0x10, 0x0, 0x0, 0x3)
    SetChrSubChip(0x10A, 2)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #28
        0x10A,
        "#1310F#12POh, Lugran!\x02",
    )

    CloseMessageWindow()

    def lambda_14F0():
        OP_6D(27760, 200, -1960, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_14F0)

    def lambda_1508():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1508)
    OP_43(0x10, 0x0, 0x0, 0x4)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)

    ChrTalk(    #29
        0x10,
        (
            "#633F#5PIs something the matter?\x02\x03",

            "It's not like you to walk right up to the second\x01",
            "floor without even looking at the board and sit\x01",
            "quietly like this.\x02\x03",

            "#632FYou're not feeling sick from eating too much\x01",
            "ice cream or something, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10A,
        (
            "#819F#12PD-Don't be silly... I'm not a kid anymore,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#633F#5PCould've fooled me!\x02\x03",

            "#631FI swear that you were the one who ate three\x01",
            "full scoops first thing one morning and later had\x01",
            "to go get some stomach medicine from Spence...\x02\x03",

            "Maybe my memory's playing tricks on me?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #32
        0x10A,
        (
            "#1317F#12PHaha! Aha...ha...\x02\x03",

            "L-Let's all pretend that never happened,\x01",
            "okay?\x02\x03",

            "#817FBesides, that was back when I was a junior\x01",
            "bracer! That was forever ago!\x02\x03",

            "#816FI learned my lesson after that, I swear!\x01",
            "Now I never have more than one scoop\x01",
            "each morning!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x10,
        (
            "#634F#5PYou're not supposed to have ice cream in\x01",
            "the morning at all, you know...\x02\x03",

            "#630F...Well, no matter.\x02\x03",

            "So, what've you been doing up here all this \x01",
            "time, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        (
            "#1310F#12POh, right...\x02\x03",

            "#811FWell, you see, I got a letter from my pappy\x01",
            "who lives a long way away this morning.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #35
        0x10,
        (
            "#633F#5PReally, now?\x02\x03",

            "He's a swordsman if I recall, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        (
            "#819F#12PYup. He's an instructor.\x02\x03",

            "#816FHe's real famous among sword practitioners,\x01",
            "actually! Yun Ka-fai of the Eight Leaves One\x01",
            "Blade school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#631F#5PAh, yeah. That's the one.\x02\x03",

            "I was familiar with the name even before\x01",
            "meeting you, but I was quite surprised to\x01",
            "find out you were his granddaughter.\x02\x03",

            "#630FDidn't he used to live here in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#814F#12PI'm surprised you know about that!\x02\x03",

            "#1316FI can't say I have any memories\x01",
            "of when he was here, though.\x02\x03",

            "It was around when I was born,\x01",
            "so how could I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#634F#5PThat long ago? I see...\x02\x03",

            "#630FSo, how's he doing? Well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1314F#12PJudging by his letter, yeah. He's doing fine.\x02\x03",

            "I haven't had the chance to meet him in person\x01",
            "for about a year now...\x02\x03",

            "#819FLast time we had the chance to spar, I felt like\x01",
            "he was totally babying me. Even though he's,\x01",
            "like, seventy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#631F#5PHaha. He really must be skilled to be treating \x01",
            "an active bracer that way.\x02\x03",

            "#632FHmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        "#810F#12PHuh? What's with the sudden serious face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#634F#5POh, it's nothing all that major, but I've been\x01",
            "wondering something for a while.\x02\x03",

            "#630FWhy do you stay here when you could join him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10A,
        "#814F#12PErr... Sorry. I'm lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#630F#5PWell, it's just that you're aiming to improve your\x01",
            "swordsmanship, aren't you?\x02\x03",

            "It feels like if you have a grandfather like that,\x01",
            "the fastest way to do that would be to go with\x01",
            "him and polish your skills at his side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#1317F#12PThat's... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#633F#5PI suppose it's not my place to be telling you\x01",
            "what may or may not be best for you.\x02\x03",

            "#634FSorry, Anelace. You needn't pay any attention\x01",
            "to an old man like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10A,
        (
            "#819F#12PNo, that's not true at all!\x02\x03",

            "#816FI really appreciate your advice, so please don't\x01",
            "think it's not your place to give it.\x02\x03",

            "#813FI can definitely see where you're coming from\x01",
            "on this.\x02\x03",

            "I do have my reasons for being here and all.\x01",
            "They're just a little difficult to explain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#633F#5POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10A,
        (
            "#1316F#12PI DO want to learn more about swordsmanship\x01",
            "and swords in general...\x02\x03",

            "...so in that sense, you're right that continuing\x01",
            "to train under Pappy would be both the best and\x01",
            "fastest course of action.\x02\x03",

            "#813FBut that's not all I want to do with my life.\x01",
            "I want at least as much, if not more, to know\x01",
            "more about what it means to be a bracer.\x02\x03",

            "#812FI guess it's a case of wanting to learn more\x01",
            "about swordsmanship as a bracer rather than\x01",
            "as a swordsman, if that makes sense.\x02\x03",

            "#1316FAm I even doing a good job of explaining this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "#631F#5PNo, no. I think I see where you're coming from now,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10A,
        (
            "#1314F#12PBesides...\x02\x03",

            "#817F...Pappy once told me that he'd taught me all \x01",
            "of the technical side of swordsmanship--forms,\x01",
            "crafts, and that kinda stuff--already.\x02\x03",

            "Whether I can master them or not is all down to\x01",
            "me now.\x02\x03",

            "#816FSo in that sense, I feel like there's no specific\x01",
            "need for me to train under him nowadays.\x02\x03",

            "#819FHeehee... Of course, whether I'm really advancing\x01",
            "in my swordsmanship now is another issue entirely.\x01",
            "I wish I could say for sure I was, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#633F#5PHmm... I see...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#1317F#12PU-Umm... What's with the silent treatment all\x01",
            "of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#634F#5PO-Oh, it's nothing.\x02\x03",

            "#630FYou're just not really one for these kinds of\x01",
            "serious discussions, so I was impressed to see\x01",
            "you were even capable of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#1316F#12PH-Hey! I am SO capable!\x02\x03",

            "#812FBesides, you were the one who kind of pushed\x01",
            "me into talking about all this stuff first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#631F#5PHahaha! I'm glad I did, too.\x02\x03",

            "#630FAnyway, getting back to the point. What did\x01",
            "the letter even say, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#814F#12POh, right...\x02\x03",

            "#819FW-Well, as surprising as it is...\x02\x03",

            "#1314F...it says that I should go and see Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        (
            "#633F#5PCassius...?\x02\x03",

            "The one and only?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10A,
        (
            "#1316F#12PYep! That's right.\x02\x03",

            "#816FSupposedly, Pappy was invited by the Royal Army\x01",
            "to be a guest instructor at some point a long time\x01",
            "ago.\x02\x03",

            "That's when he trained Cassius, too.\x02\x03",

            "#817FSo ever since, they've had this kinda student-\x01",
            "master relationship with one another...\x02\x03",

            "#1314FCassius even went out of his way to go and see\x01",
            "him ten years ago when he decided to stop using\x01",
            "a sword, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "#633F#5PTen years ago?\x02\x03",

            "#634FThat would put that around when he left the\x01",
            "army and became a bracer, then.\x02\x03",

            "#632FWhat exactly prompted him to tell you to go\x01",
            "visit Cassius now, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        (
            "#819F#12PWell, I guess he only just recently found out\x01",
            "that Cassius has returned to the army.\x02\x03",

            "So now he's wondering whether he might take\x01",
            "this opportunity to take up the sword again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#634F#5PHmm...\x02\x03",

            "#630FAhh, I got'cha. He wants you to go and ask\x01",
            "for him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        "#816F#12PAnd let him know what he says, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#630F#5PI see...\x02\x03",

            "#631FPeople really do end up connected in the\x01",
            "strangest places and the funniest ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        (
            "#819F#12PAhaha... Tell me about it.\x02\x03",

            "#816FAnyway, that being said...\x02\x03",

            "...I...kind of have a favor to ask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#631F#5PYou want time off, I assume?\x02\x03",

            "Well, who am I to say no? You've got good cause\x01",
            "to have it.\x02\x03",

            "I can even get in touch with the army and set up\x01",
            "a meeting with Cassius if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10A,
        "#1310F#12PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "#634F#5PReally. Go along and get that truth your \x01",
            "grandfather wants for him.\x02\x03",

            "#630FBut in return...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10A,
        "#814F#12PIn return...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#631F#5PI want you to take care of every single one of the\x01",
            "monster extermination requests on the board first.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x10A,
        (
            "#1317F#12PE-EVERY single one?!\x02\x03",

            "Aren't there, like, five of them right now?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#631F#5PSure, but the monsters in this area will be\x01",
            "no trouble at all for you as you are now.\x02\x03",

            "#630FThey'd be less of a problem if Grant were\x01",
            "around, but I had to lend him to the guild\x01",
            "over in Ruan, and he's still not back.\x02\x03",

            "You're gonna have to pick up the slack here\x01",
            "in his place, especially if you want time off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        "#1316F#12P*sigh* Okaaay...\x02",
    )

    CloseMessageWindow()

    def lambda_306E():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_306E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x00Three days later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1349 end

    def Function_7_30DB(): pass

    label("Function_7_30DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1240, 0, 4560, 0)
    OP_67(0, 5550, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(45000, 0)
    OP_6E(327, 0)
    SetChrPos(0x10A, 0, 0, 2340, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 180, 0, 4400, 180)

    def lambda_3151():
        OP_6B(2320, 2000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3151)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #76
        0x10,
        (
            "#631F#5P...Really? It sounds like that was quite the\x01",
            "fruitful experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10A,
        (
            "#819F#12PIt sure was.\x02\x03",

            "#1314FI'm guessing this was Pappy's plan all along.\x01",
            "He knew exactly what would happen if I went to\x01",
            "ask Cassius what I did, and that's why he asked.\x02\x03",

            "I must've sounded a little unsure of myself in the\x01",
            "last letter I wrote him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#634F#5PI see... Like master, like pupil.\x02\x03",

            "#630FIncidentally, while I hate to spring this on you\x01",
            "before you've even had a chance to settle back in,\x01",
            "a lot of work built up while you were away.\x02\x03",

            "There's even a request from the mayor, too,\x01",
            "so I really need you to get right on it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        "#1317F#12PAck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#631F#5PHaha... If anything, you should be grateful!\x02\x03",

            "All this work'll give you a chance to refine\x01",
            "your skills with that new mindset of yours,\x01",
            "won't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        "#819F#12PAhaha... That's one way of looking at it, sure.\x02",
    )

    CloseMessageWindow()

    def lambda_34CF():
        OP_6B(2220, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_34CF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x0C#40WSo, Pappy...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #83
        (
            "\x07\x0C#40WWhile I bet you knew all along, it looks like Cassius\x01",
            "has no intentions of taking up the way of the sword\x01",
            "ever again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x0C#40WBut thanks to seeing him, I ended up being given a\x01",
            "chance to reexamine my own swordsmanship.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x0C#40WUp until now, I thought it was all about getting \x01",
            "stronger. Or faster. Things like that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #86
        (
            "\x07\x0C#40WBut now, I've finally realized that what's far more\x01",
            "important than either of those things is why you \x01",
            "take up your sword in the first place. Your feelings.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40WI feel like now I finally understand why I was never\x01",
            "able to defeat you, no matter how many times we\x01",
            "fought.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x0C#40WI might not be the best student in the world, but I'll\x01",
            "keep giving my training all I've got.\x01",
            "                                   Love, Anelace\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x5, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x00Side Story [Swordsmanship] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 6)), scpexpr(EXPR_END)), "loc_38DF")
    OP_28(0xA, 0x4, 0x20)
    OP_3E(0x590, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #90
        "\x07\x05Received \x1F\x90\x05\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_38DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3920")
    OP_28(0xA, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #91
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_3920")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5502   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_7_30DB end

    def Function_8_3938(): pass

    label("Function_8_3938")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(27170, 0, -2020, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, 26740, 200, -3610, 270)
    SetChrPos(0x13, 24060, 200, -3580, 90)
    FadeToBright(2000, 0)
    OP_6B(2500, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #92
        0x13,
        (
            "#1317F#6PU-Umm... Mayor Maybelle?\x02\x03",

            "#819FCan I ask you to go over what you want me to do\x01",
            "one more time? Just so I'm not misunderstanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        (
            "#615F#11P*cough* W-Well...\x02\x03",

            "#618FAs I said, I would like to investigate...erm...\x01",
            "exactly what relationship those two have...\x02\x03",

            "#612F...as well as what kind of person the gentleman\x01",
            "in question is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x13,
        (
            "#1316F#6PSo, to put it in simpler terms...\x02\x03",

            "...you want me to check out whether they're\x01",
            "dating and do a background check on the man,\x01",
            "right?\x02\x03",

            "#812FIs that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x12,
        (
            "#615F#11PY-Yes... Yes, it is.\x02\x03",

            "#612FI-Is there something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x13,
        (
            "#1316F#6P...\x02\x03",

            "#813FWell, kinda...\x02\x03",

            "#1314FI mean, we bracers do at times do background\x01",
            "checks on people...\x02\x03",

            "...but that's when we suspect or know for sure\x01",
            "they're involved in a crime.\x02\x03",

            "If they're not, doing so would be an invasion of\x01",
            "their privacy, and that doesn't exactly fly with\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x12,
        "#613F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#817F#6PObviously, if you have reason to believe the\x01",
            "man Lila appears to be dating is involved in\x01",
            "illegal activity, I'd be happy to help...\x02\x03",

            "#812FIs that the case, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x12,
        (
            "#618F#11PN-No...\x02\x03",

            "On the contrary, actually. He appears to be\x01",
            "a good, honest man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x13,
        (
            "#1316F#6PI-I see...\x02\x03",

            "#1314FThere's obviously going to be the chance that's\x01",
            "just a facade and he's not the kind of person he\x01",
            "appears to be...\x02\x03",

            "...but as it stands, I don't see any grounds for\x01",
            "the guild to make their move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x12,
        (
            "#615F#11PThat is unfortunate...but I can certainly see\x01",
            "where you're coming from.\x02\x03",

            "#610FI'm sorry for troubling you with this. I don't know\x01",
            "what came over me.\x02\x03",

            "#617FPlease, forget this conversation ever happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x13,
        (
            "#1317F#6PU-Umm...\x02\x03",

            "#819F...Forgive me for asking this, but you're all in\x01",
            "favor of them dating, right? You're not trying \x01",
            "to break them up or something?\x02\x03",

            "So why are you so concerned with finding all\x01",
            "this out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        "#615F#11P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #104
        0x12,
        (
            "#618F#11PAs I think you're aware, Lila lost her mother\x01",
            "and father during the Hundred Days War.\x02\x03",

            "As far as I can tell, the scars that left on her\x01",
            "heart still haven't truly healed, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x13,
        "#1317F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x12,
        (
            "#615F#11PAnd I believe this is her first foray into romantic\x01",
            "relationships, too...\x02\x03",

            "I'm just so worried about her getting hurt as a\x01",
            "result of this.\x02\x03",

            "#618FI'm not the slightest concerned about how noble\x01",
            "the man's family is or how much money they have.\x01",
            "Nothing superficial like that.\x02\x03",

            "All I want to know is whether he genuinely cares\x01",
            "for her well-being and will make her happy.\x02\x03",

            "#610FThat's all that matters to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x13,
        "#813F#6PI see where you're coming from...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x12,
        (
            "#617F#11PStill, at the end of the day, that doesn't give\x01",
            "me the excuse to invade the man's privacy or\x01",
            "meddle in their affairs.\x02\x03",

            "#611FI'm sure Lila will eventually tell me about what's\x01",
            "going on when she feels the time is right.\x02\x03",

            "I can ask her all of my questions then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x13,
        "#817F#6P...Nah. This is good stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        "#613F#11PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x13,
        (
            "#816F#6PI COMPLETELY understand where you're coming\x01",
            "from here!\x02\x03",

            "#815FI'd be MORE than happy to accept your request!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #112
        0x12,
        (
            "#618F#11PWait. I thought...erm...\x02\x03",

            "#612FAre you sure? Wouldn't doing so violate the\x01",
            "bracer code?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x13,
        (
            "#816F#6POh, no worries! The bracer code's totally open\x01",
            "to individual interpretation, so it leaves a lot to\x01",
            "each bracer's personal judgment.\x02\x03",

            "#1316FI feel trying to follow the code to the letter and\x01",
            "ignoring the feelings of those we're trying to\x01",
            "serve misses the point of being a bracer, too.\x02\x03",

            "#1310FSo I don't think it's unfair to dismiss your well-\x01",
            "meaning intentions as trying to invade someone's\x01",
            "privacy, either!\x02\x03",

            "#811FYou leave all of this to me! I'll get you aaall kinds\x01",
            "of answers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12,
        (
            "#611F#11PThank you so much...\x02\x03",

            "#617FI appreciate you agreeing to do this for me. Really.\x02\x03",

            "#610FJust know that I completely understand where you\x01",
            "were coming from earlier, so I do want to ask that\x01",
            "you invade his privacy no more than necessary.\x02\x03",

            "Is that fair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x13,
        (
            "#816F#6PPerfect-o!\x02\x03",

            "#819FHeehee. I hope this turns out to be something\x01",
            "that'll really make her happy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49A9():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_49A9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x00#40WAnd that was the day Anelace agreed to accept the\x01",
            "mayor's request, immediately--and enthusiastically--\x01",
            "beginning her investigation.\x02\x03",

            "Naturally, she was very cautious not to make both Lila\x01",
            "and her presumed partner suspicious in the process.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1131   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3938 end

    SaveToFile()

Try(main)
