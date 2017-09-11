from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4112   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60081",
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
        'Olivier',                              # 9
        'Mueller',                              # 10
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02190 ._CH',             # 01
        'ED6_DT07/CH00133 ._CH',             # 02
        'ED6_DT07/CH00035 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02190P._CP',             # 01
        'ED6_DT07/CH00133P._CP',             # 02
        'ED6_DT07/CH00035P._CP',             # 03
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


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_11A",          # 01, 1
        "Function_2_12B",          # 02, 2
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    SoundLoad(137)
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_10A end

    def Function_1_11A(): pass

    label("Function_1_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_12A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A")

    Return()

    # Function_1_11A end

    def Function_2_12B(): pass

    label("Function_2_12B")

    ClearMapFlags(0x10000000)
    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_24(0x1C9, 0x4B)
    OP_77(0xC9, 0xC9, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -940, 0, 4500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(370, 0, 5650, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "#6P#035FA dark cloud looms over the\x01",
            "royal city, and yea, it signals\x01",
            "a passion most black...\x02\x03",

            "#030FHeh heh... But so fascinating\x01",
            "a shade of black it seems.\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 30)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x9, 6430, 0, -20, 270)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #1
        0x9,
        "Man's Voice",
        "You are such an idiot...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2DC():

        label("loc_2DC")

        TurnDirection(0x8, 0x9, 400)
        OP_48()
        Jump("loc_2DC")

    QueueWorkItem2(0x8, 3, lambda_2DC)

    def lambda_2ED():
        OP_6D(2800, 0, 3250, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ED)

    def lambda_305():
        OP_6E(318, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_305)
    OP_8E(0x9, 0xFE6, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8C(0x9, 270, 400)
    Sleep(1000)

    ChrTalk(    #2
        0x8,
        (
            "#033F#6PAm I perchance...dreaming?\x02\x03",

            "#031FMueller, my boon companion!\x02\x03",

            "Have you come all this way, all the\x01",
            "long roads from the Imperial capital,\x01",
            "just to see me? How delicious!\x02\x03",

            "On what wind did you fly hither?\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_71(0x0, 0x10)
    OP_70(0x0, 0x0)

    def lambda_421():
        OP_6D(490, 0, 4019, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_421)
    OP_8E(0x9, 0xFFFFFD94, 0x0, 0xA3C, 0xBB8, 0x0)
    OP_8C(0x9, 0, 400)
    OP_44(0x8, 0x3)

    ChrTalk(    #3
        0x9,
        (
            "#4P#270FWind?\x01",
            "What are you talking about?\x02\x03",

            "I'm here because I've had to\x01",
            "follow your stupid ass all\x01",
            "over Aidios' damned creation.\x02\x03",

            "Do you have any idea how much\x01",
            "time this has cost me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#035F#6PPlease, my dear. Don't hide behind\x01",
            "such base profanities.\x02\x03",

            "Your lips spit venom, but the fire in \x01",
            "your eyes show the depths of worry\x01",
            "that drove you onward to my side.\x02\x03",

            "Love... It is truly blind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "#4P#273FThat doesn't even make...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#031F#6PNo more words, dear Mueller!\x01",
            "Fly! Fly to my embrace!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#4P#272FI came here because I'm trying to bring\x01",
            "you information...that YOU asked for.\x02\x03",

            "But I'm guessing you'd rather hug than\x01",
            "talk.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #8
        0x8,
        (
            "#036F#6PLo! I am hoist with my\x01",
            "own petard!\x02\x03",

            "#035FVery well. Let us talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "#4P#270FYes. Like SANE people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#030F#6P*sigh* As you wish.\x02\x03",

            "#035FAhem!...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 1)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_62(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x8,
        (
            "#031F#6PWhat news, milord? ☆\x02\x03",

            "#031FWhat news for your humble Olivier? ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x9)
    Sleep(500)
    OP_63(0x8)

    ChrTalk(    #12
        0x8,
        (
            "#033F#6PNo? No.\x02\x03",

            "#035FAll right. No clowning, then.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x8,
        (
            "#039F#3S#6PDon't play like that, brother.\x01",
            "Give a man some information.\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #14
        0x8,
        "#039F#3S#6PLay it on me, man!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #15
        0x9,
        (
            "#4P#274FYou're making me stupider\x01",
            "just by being around you.\x02\x03",

            "Okay, I'll tell you. Just stop\x01",
            "opening your mouth and making\x01",
            "sounds come out of it. \x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #16
        0x8,
        "#031F#6PHuzzah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#4P#270FRegarding the guy we were talking\x01",
            "about before... I managed to pick\x01",
            "up his trail.\x02\x03",

            "From what I found, he was at\x01",
            "one of the Erebonian Bracer Guilds\x01",
            "until about a month ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#033F#6POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#4P#270FOver the past several months, all\x01",
            "of the guild branches in the Empire\x01",
            "have been attacked, one after another.\x02\x03",

            "Seems he was supposed to\x01",
            "be investigating why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#030F#6PAttacked, you say...\x02\x03",

            "I should think it unlikely, but\x01",
            "might these have been perpetrated\x01",
            "by some military unit, somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "#4P#272FYou picked up on it, too...\x01",
            "It's not the world of ten years\x01",
            "ago anymore, though.\x02\x03",

            "As far as I know, no military force\x01",
            "has been given marching orders.\x02\x03",

            "I'd bet that someone hired\x01",
            "jaegers to pull this off.\x02\x03",

            "#270FAnyway, our boy's trail stopped\x01",
            "for a while, right when that\x01",
            "case was solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#034F#6PHmmmm...\x01",
            "Oh dear, oh dear.\x02\x03",

            "I took such pains coming to Liberl,\x01",
            "and 'twould seem that I was\x01",
            "following a wild goose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#4P#270FI guess so.\x02\x03",

            "But if the man we're after isn't\x01",
            "here, there's no real reason to\x01",
            "stick around, is there?\x02\x03",

            "That storm you were talking\x01",
            "about is going to be worse\x01",
            "than expected. A lot worse.\x02\x03",

            "You should come back to the\x01",
            "Imperial capital before you\x01",
            "get caught in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#031F#6PHa ha ha... Ever a jester!\x02\x03",

            "How could I bear to part with\x01",
            "the opportunity to play a role\x01",
            "in the finest opera ever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#4P#273F...What?\x02\x03",

            "#271FTell me you're not actually\x01",
            "thinking of...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F8D():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8D)

    def lambda_F9B():
        OP_6E(290, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F9B)
    OP_6D(-250, 0, 5610, 1500)

    ChrTalk(    #26
        0x8,
        (
            "#035F#6PI am, you might say, already in\x01",
            "costume.\x02\x03",

            "Sadly, the lead is unavailable,\x01",
            "so the understudies must be used.\x02\x03",

            "#030FI have the utmost faith that\x01",
            "between the two of them, they\x01",
            "will put on a grand performance.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x100000)
    Sleep(1000)
    OP_AD(0x40040, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12B end

    SaveToFile()

Try(main)
