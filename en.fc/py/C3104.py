from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3104.x',
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
        'ED6_DT06/CH20141 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT06/CH20141P._CP',             # 00
    )

    ScpFunction(
        "Function_0_B2",           # 00, 0
        "Function_1_C6",           # 01, 1
        "Function_2_E4",           # 02, 2
        "Function_3_1B4C",         # 03, 3
        "Function_4_1B4D",         # 04, 4
        "Function_5_1B4E",         # 05, 5
    )


    def Function_0_B2(): pass

    label("Function_0_B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C5")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_C5")

    Return()

    # Function_0_B2 end

    def Function_1_C6(): pass

    label("Function_1_C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3")

    label("loc_DE")

    OP_22(0x1CD, 0x1, 0x64)

    label("loc_E3")

    Return()

    # Function_1_C6 end

    def Function_2_E4(): pass

    label("Function_2_E4")

    ClearMapFlags(0x10000000)
    AddParty(0x5, 0xFF)
    AddParty(0x6, 0xFF)
    AddParty(0xA, 0xFF)
    EventBegin(0x0)
    OP_66(0x0)
    OP_6D(3160, 0, 9050, 0)
    OP_67(-16400, 26840, -56180, 0)
    OP_6B(1000, 0)
    OP_6C(16000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24790, 110, -35590, 270)
    SetChrPos(0x102, 25200, 30, -36550, 270)
    SetChrPos(0x106, 22990, 20, -36670, 90)
    SetChrPos(0x10B, 23610, 10, -37570, 45)
    SetChrPos(0x107, 23250, 30, -35430, 90)
    FadeToBright(2000, 0)

    def lambda_198():
        OP_6D(24300, 60, -35590, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_198)
    Sleep(4000)

    def lambda_1B5():
        OP_67(-16400, 37480, -56180, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5)

    def lambda_1CD():
        OP_6B(800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CD)
    Sleep(4000)
    Fade(1000)
    OP_44(0x101, 0xFF)
    OP_66(0x1)
    OP_6D(24380, 30, -36240, 0)
    OP_67(0, 37430, -45510, 0)
    OP_6B(600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#002F#4PWhew...\x01",
            "We managed to make it out.\x02\x03",

            "Looks like they haven't started\x01",
            "patrolling over here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#010FMajor Cid may be keeping\x01",
            "them busy.\x02\x03",

            "#013FBut if we waste any time here,\x01",
            "we're probably going to have\x01",
            "to deal with a pursuit force.\x02\x03",

            "We've got to get the professor\x01",
            "somewhere safe or else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10B,
        "#102FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#063F#3PE-Estelle...? Joshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#006F#4POh, it's okay.\x01",
            "No need to worry.\x02\x03",

            "I promise, we'll be here\x01",
            "to protect both of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)

    ChrTalk(    #5
        0x106,
        (
            "#050F...No.\x02\x03",

            "You two fall back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #6
        0x101,
        "#580FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#012FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#053FThe Intelligence Division knows my\x01",
            "face all too well by now.\x02\x03",

            "Same goes for Tita and the old man.\x01",
            "But they've got no idea you two are\x01",
            "involved, unless ol' Cid blabs.\x02\x03",

            "#051FSo I'm getting out of here and\x01",
            "taking them with me. We'll lay\x01",
            "low for awhile somewhere safe.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #9
        0x107,
        "#064FAgate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10B,
        (
            "#102FI understand.\x02\x03",

            "The fewer people implicated in this,\x01",
            "the better.\x02\x03",

            "#104FIn fact, I never wanted Tita to get\x01",
            "wrapped up in this in the first place.\x02\x03",

            "When I think about them taking hostages\x01",
            "to force cooperation, it makes the most\x01",
            "sense for us both to get out of here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x10B, 400)

    ChrTalk(    #11
        0x107,
        "#560FGrandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#005FWhoa, whoa, wait just a damn minute!\x02\x03",

            "How can you ask us to turn our backs on you,\x01",
            "just to keep OURSELVES safe?! That's totally\x01",
            "bonkers! We could never agree to that!\x02\x03",

            "Right, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B9():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7B9)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #13
        0x102,
        "#013FActually...I agree with Agate's assessment.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #14
        0x101,
        "#004FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#012FAccording to the theory of retreat and\x01",
            "cover, the more people there are together,\x01",
            "the greater the chance of detection.\x02\x03",

            "Which means that Agate will stand\x01",
            "a better chance of helping them\x01",
            "get away on his own.\x02\x03",

            "#015FI understand how you must feel,\x01",
            "but for now, we really need to do what\x01",
            "Agate says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#580FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#053FNice one, Joshua. Exactly\x01",
            "what I was getting at.\x02\x03",

            "#050FNow, I need you to be a good\x01",
            "girl and withdraw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#003FWait, I...\x02\x03",

            "I get your idea, in theory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x107,
        "#063F#3PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10B,
        (
            "#104FYou don't agree, and I can see it written\x01",
            "all over your face.\x02\x03",

            "#100FSoooo, how about I send you on an important\x01",
            "mission instead? Something I certainly can't\x01",
            "do myself, given the circumstances...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEC():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AEC)

    def lambda_AFA():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFA)

    def lambda_B08():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B08)
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(    #21
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10B,
        (
            "#102FFirst, I want you to go to Grancel.\x02\x03",

            "Then, you must speak with \x01",
            "Her Majesty, Queen Alicia,\x01",
            "in Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        "#005FI must WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#014FWhat's this all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10B,
        (
            "#102FThe aforementioned 'Black Orbment'...\x02\x03",

            "It originally somehow fell into\x01",
            "Colonel Richard's hands.\x02\x03",

            "#104FHe referred to it as the 'Gospel.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#012FGospel? \x01",
            "As in, religious teachings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x106,
        (
            "#053FHeh. That's certainly an ominous-\x01",
            "sounding name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10B,
        (
            "#104FApparently, this 'Gospel' was taken\x01",
            "from the Intelligence Division, but by whom,\x01",
            "I couldn't say.\x02\x03",

            "After that, I'd wager that it was probably sent\x01",
            "out in a package, addressed to Cassius.\x02\x03",

            "However, Intelligence caught wind of our little\x01",
            "...umm...blackout from before.\x02\x03",

            "#102FThey must have realized the Black Orbment was \x01",
            "involved and here in Zeiss. I suspect that was\x01",
            "their true objective in attacking the factory.\x02\x03",

            "They came to retrieve this 'Gospel.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#002FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#012FI see...\x01",
            "That explains a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10B,
        (
            "#102FColonel Richard has some kind\x01",
            "of plan to use it in the capital.\x02\x03",

            "Unless I miss my guess...\x01",
            "something very bad is coming.\x02\x03",

            "Her Majesty must be informed\x01",
            "of this at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#505FYou mean the shutdown\x01",
            "of orbal power?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10B,
        (
            "#104FNo...\x01",
            "Perhaps, if it's used...\x02\x03",

            "#102FI'm sorry. Anything more I say\x01",
            "would be pure conjecture.\x02\x03",

            "Regardless, the queen must be\x01",
            "made aware of this 'Gospel' as\x01",
            "soon as possible.\x02\x03",

            "I'm more concerned with that\x01",
            "than with my own escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#007F*sigh* I swear...\x02\x03",

            "#006FWhen you put it like that, I\x01",
            "feel like a jerk for wanting\x01",
            "to say 'No.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#010FIf you'll allow us, we'll\x01",
            "accept your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10B,
        "#101FI appreciate it.\x02",
    )

    CloseMessageWindow()

    def lambda_11AA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11AA)
    Sleep(400)

    ChrTalk(    #37
        0x107,
        (
            "#063F#3PU-Umm...\x02\x03",

            "Estelle... Joshua...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11E9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11E9)

    def lambda_11F7():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11F7)
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(    #38
        0x102,
        (
            "#010FWe've got to part ways\x01",
            "for a little bit, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#003F#4PI'm sorry... I'd hoped that\x01",
            "we could stay together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        (
            "#065F#3PN-No...\x01",
            "You don't have to apologize.\x02\x03",

            "#562FYou've just helped me so much...\x02\x03",

            "And you've treated me like a\x01",
            "little sister...\x02\x03",

            "#069F*sniffle*... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#004F#4PTita...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_134D():
        OP_6D(25380, 30, -36240, 1000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_134D)

    def lambda_1365():

        label("loc_1365")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1365")

    QueueWorkItem2(0x101, 1, lambda_1365)

    def lambda_1376():

        label("loc_1376")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1376")

    QueueWorkItem2(0x102, 1, lambda_1376)

    def lambda_1387():

        label("loc_1387")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1387")

    QueueWorkItem2(0x106, 1, lambda_1387)

    def lambda_1398():

        label("loc_1398")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1398")

    QueueWorkItem2(0x10B, 1, lambda_1398)
    OP_92(0x107, 0x101, 0x190, 0x1388, 0x0)

    def lambda_13B7():
        OP_94(0x1, 0x107, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13B7)
    OP_48()
    OP_8C(0x107, 0, 0)
    SetChrChipByIndex(0x107, 0)
    SetChrSubChip(0x107, 1)
    SetChrFlags(0x107, 0x20)
    SetChrFlags(0x107, 0x40)
    OP_8C(0x101, 292, 0)
    OP_94(0x1, 0x101, 0xB4, 0x12C, 0x7D0, 0x0)
    WaitChrThread(0x107, 0x3)

    ChrTalk(    #42
        0x107,
        (
            "#069F#3PThanks for helping my grandpa...\x02\x03",

            "A-And...*sniffle*...thank you for\x01",
            "being my friend.\x02\x03",

            "#067FI... I love you both...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#008F#4PI love you too, sweetie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#019F#4PI wish we could take\x01",
            "you with us...\x02\x03",

            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#053F...\x02\x03",

            "#050FParting is such sweet sorrow and\x01",
            "all that, but we have no choice.\x02\x03",

            "Maybe you can save the tears\x01",
            "for when we see each other\x01",
            "again, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#007F#4P*sniffle*\x01",
            "You can be a real jerk...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x10B, 0xFF)
    ClearChrFlags(0x107, 0x20)
    SetChrChipByIndex(0x107, 65535)
    TurnDirection(0x107, 0x101, 0)
    OP_94(0x1, 0x107, 0xB4, 0x258, 0x7D0, 0x0)

    def lambda_15F2():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15F2)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #47
        0x101,
        (
            "#501F#6PBut...I guess this is where\x01",
            "we part ways, too.\x02\x03",

            "A lot's happened, but you've\x01",
            "taught us so much by letting\x01",
            "us work with you.\x02\x03",

            "Thank you, Master Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x106,
        (
            "#055FDon't call me that!\x01",
            "It creeps me out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#001F#6PHa ha ha...\x01",
            "Look who's embarrassed. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        (
            "#551FBah... You really are your father's daughter.\x02\x03",

            "#051FHey, Joshua. Don't let her get too out of\x01",
            "control, you hear me?\x02\x03",

            "She's not half bad in combat, but there's more\x01",
            "to being an adult than just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#009F#6PHmph. Not that it's any of YOUR business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#019F#4PJust leave her to me.\x02\x03",

            "#010FYou take care, as well.\x02\x03",

            "Take care of Tita and\x01",
            "the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x106,
        (
            "#051FI will.\x02\x03",

            "All right, then...\x01",
            "Let's get a move on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10B,
        "#101FFarewell, children of Cassius...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        "#069FS-Stay safe! Both of you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#006F#6PYou too, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#010F#4PAidios be with you!\x01",
            "Be careful out there!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_195D():
        OP_6D(21340, 70, -35800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_195D)
    OP_8C(0x106, 315, 400)

    def lambda_197C():
        OP_8E(0xFE, 0x2878, 0x50, 0xFFFF7DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_197C)
    OP_8C(0x107, 270, 400)

    def lambda_199E():
        OP_8E(0xFE, 0x27EC, 0x5A, 0xFFFF7A2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_199E)
    Sleep(400)
    OP_8C(0x10B, 315, 400)

    def lambda_19C5():
        OP_8E(0xFE, 0x2878, 0x50, 0xFFFF7DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_19C5)
    OP_8C(0x101, 270, 400)
    Sleep(2000)
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(200)
    OP_24(0x1CD, 0x50)
    Sleep(200)
    OP_24(0x1CD, 0x46)
    Sleep(200)
    OP_24(0x1CD, 0x3C)
    Sleep(200)
    OP_24(0x1CD, 0x32)
    Sleep(200)
    OP_24(0x1CD, 0x28)
    Sleep(200)
    OP_24(0x1CD, 0x1E)
    Sleep(200)
    OP_24(0x1CD, 0x14)
    Sleep(200)
    OP_24(0x1CD, 0xA)
    Sleep(200)
    OP_24(0x1CD, 0x0)
    OP_0D()
    Sleep(1000)
    OP_AD(0x40044, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x14, 0x0)
    OP_A2(0x5CE)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC9")
    ShowSaveMenu()

    label("loc_1AC9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x571)
    OP_A2(0x533)
    OP_A2(0x5CF)
    OP_B8(0x6)
    OP_B8(0x5)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0xA, 0xFF)
    OP_28(0x54, 0x4, 0x2)
    OP_28(0x54, 0x4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_1B14")
    Jump("loc_1B3F")

    label("loc_1B14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1B27")
    OP_2B(0x43, 0x1)
    Jump("loc_1B3F")

    label("loc_1B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_1B3A")
    OP_2B(0x43, 0x2)
    Jump("loc_1B3F")

    label("loc_1B3A")

    OP_2B(0x43, 0x3)

    label("loc_1B3F")

    OP_A2(0x3FA)
    NewScene("ED6_DT01/R4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E4 end

    def Function_3_1B4C(): pass

    label("Function_3_1B4C")

    Return()

    # Function_3_1B4C end

    def Function_4_1B4D(): pass

    label("Function_4_1B4D")

    Return()

    # Function_4_1B4D end

    def Function_5_1B4E(): pass

    label("Function_5_1B4E")

    Return()

    # Function_5_1B4E end

    SaveToFile()

Try(main)
