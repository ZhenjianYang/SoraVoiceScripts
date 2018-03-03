from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4163   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4163.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Ambassador Crainagh',                  # 9
        'Prince Olivert',                       # 10
        'Major Vander',                         # 11
        'Secretary Lechter',                    # 12
        'Target Camera',                        # 13
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT27/CH03713 ._CH',             # 02
        'ED6_DT26/CH20805 ._CH',             # 03
        'ED6_DT07/CH00033 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT27/CH03713P._CP',             # 02
        'ED6_DT26/CH20805P._CP',             # 03
        'ED6_DT07/CH00033P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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


    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = 76130,
        TriggerRange        = 1000,
        ActorX              = 4970,
        ActorZ              = 1000,
        ActorY              = 76130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54740,
        TriggerZ            = 0,
        TriggerY            = 65190,
        TriggerRange        = 1000,
        ActorX              = 54740,
        ActorZ              = 1000,
        ActorY              = 65190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_22E",          # 02, 2
        "Function_3_17F6",         # 03, 3
        "Function_4_327D",         # 04, 4
        "Function_5_341D",         # 05, 5
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1E2")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1E2")

    Return()

    # Function_0_1BA end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5")
    OP_6F(0x17, 0)
    Jump("loc_1FC")

    label("loc_1F5")

    OP_6F(0x17, 60)

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E")
    OP_6F(0x18, 0)
    Jump("loc_215")

    label("loc_20E")

    OP_6F(0x18, 60)

    label("loc_215")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D")
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()

    label("loc_22D")

    Return()

    # Function_1_1E3 end

    def Function_2_22E(): pass

    label("Function_2_22E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00#40WOne month after the collapse of the Liber Ark...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#40WThe banquet to celebrate the crisis' successful resolution was\x01",
            "over, with Estelle and her friends having largely left the capital\x01",
            "to go elsewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x00#40WOne of them, however--Prince Olivert Reise Arnor--sat rather\x01",
            "comfortably in the ambassador's office in Grancel's Erebonian\x01",
            "embassy, his work in the country not quite settled.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(1000, 0, 75500, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -4460, 0, 78260, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -4600, 200, 71920, 180)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4460, 200, 68060, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5440, 0, 73080, 180)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #3
        (
            "I-I can't believe that you...\x02\x03",

            "I mean, my deepest apologies for not noticing that\x01",
            "you were His Highness Prince Olivert sooner!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    Sleep(500)

    def lambda_56C():
        OP_6D(-2500, 0, 72000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_56C)

    def lambda_584():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_584)

    def lambda_59C():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_59C)

    def lambda_5AC():
        OP_6B(3128, 4000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_5AC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x0)
    Sleep(500)

    ChrTalk(    #4
        0x11,
        (
            "#030F#5POh I'm not surprised you never realized. I may be a\x01",
            "prince, but my mother was a commoner. What point\x01",
            "is there in bothering to remember my face?\x02\x03",

            "It's not as though I often showed myself in the palace\x01",
            "or attended high society gatherings.\x02\x03",

            "#031FKnowing me certainly isn't going to help you in moving\x01",
            "up the ranks, my friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#1102F#12PHaha...ha...hmm... There's no need to be so humble,\x01",
            "Your Highness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#035F#5PBesides, I'm actually rather grateful to you,\x01",
            "ambassador.\x02\x03",

            "#030FYou gave me all kinds of useful advice during\x01",
            "my stay here at the embassy that I'm sure will\x01",
            "be to my benefit in the future.\x02\x03",

            "#031FWell-meant words such as, 'Act like a man of the \x01",
            "Empire for once in your life!' and, 'Stop idling\x01",
            "here, go home, and try doing some damned work!'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x10,
        "#1103F#12P#3SI...!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        "#1101F#12PY-Your Highness, I was only... I mean, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "#272F#5PYour Highness, I think you've tormented him enough\x01",
            "for one day.\x02\x03",

            "#276FThe ambassador behaved in the same way any other\x01",
            "sane man would in his position.\x02\x03",

            "If anything, I'd say he has every right to be angry at\x01",
            "US for keeping the truth from him for so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#1100F#12PBut, M-Mueller...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#031F#5PAhh, I suppose you're right. I'll spare him any more\x01",
            "teasing for now.\x02\x03",

            "#030FI actually wasn't joking about being grateful to you,\x01",
            "though. You truly have done admirable work over the\x01",
            "past month.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x10,
        "#1101F#12P...I have?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#035F#5PActing as a pipeline with the Empire, checking the\x01",
            "safety of Erebonians residing in Liberl, helping the\x01",
            "international liner service to resume...\x02\x03",

            "And those are only the tip of the iceberg! You've\x01",
            "done so much more.\x02\x03",

            "#030FYou have my deepest thanks as a prince of the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#1102F#12PI-I am not worthy of such praise, Your Highness...\x02\x03",

            "#1100FYou, however, deserve the utmost for braving the\x01",
            "danger you did flying up to the Liber Ark.\x02\x03",

            "All of what happened seems to have caused quite\x01",
            "the commotion in our homeland.\x02\x03",

            "So the people seem to be rather relieved now that\x01",
            "they know the danger has passed.\x02\x03",

            "#1102FIt's all thanks to your courage that they are able\x01",
            "to rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#035F#5POh, there's no point in flattering me, ambassador.\x02\x03",

            "#030FI just did what I could. Nothing more, nothing less.\x02\x03",

            "And I couldn't have done anything alone. All I was\x01",
            "able to accomplish was thanks to the help of those\x01",
            "around me.\x02\x03",

            "#031FI'm fairly removed from the stereotype of Erebonians\x01",
            "as stern, strong, and self-sufficient, if I do say so\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1102F#12PHaha... As rude as it may be to agree, perhaps\x01",
            "you're correct.\x02\x03",

            "#1100FAnd yet I believe your willingness to be flexible\x01",
            "most definitely helped rather than hindered you\x01",
            "here.\x02\x03",

            "I believe people like you are exactly what the\x01",
            "Empire is going to need in the future.\x02\x03",

            "#1102FRegardless of how I may feel about His Excellency\x01",
            "the Chancellor's approach...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        "#276F#5PAmbassador...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#033F#5PWell, this is a surprise. I was under the impression\x01",
            "that you supported the chancellor.\x02\x03",

            "#030FThen again you are a noble... Does that lead you to\x01",
            "oppose his reformist policies, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1102F#12PI may be a noble on paper, but I'm only a baron.\x02\x03",

            "All in all, I generally fall in favor of his reformist\x01",
            "policies.\x02\x03",

            "#1100FBe that as it may, while this may just be the result\x01",
            "of being in Liberl for so long and being influenced\x01",
            "by the ways of its people...\x02\x03",

            "...I do sometimes find myself becoming frightened\x01",
            "by his hardline approach.\x02\x03",

            "#1102FI can't help but wonder exactly what direction he's\x01",
            "trying to take our old nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#032F#5P...Interesting.\x02\x03",

            "#035F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#1100F#12PYour Highness?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#035F#5P...Oh, I was just thinking that I'm quite glad to\x01",
            "have taken the chance to engage in such fruitful\x01",
            "talk with you just before departing the country.\x02\x03",

            "#030FI pray you will continue doing all you can to\x01",
            "ensure the peace of Liberl and its surrounding\x01",
            "nations while I'm gone.\x02\x03",

            "#031FPreferably in cooperation with Ambassador\x01",
            "Cochrane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1102F#12PHmm... Yes. Let's not forget her, I suppose.\x02\x03",

            "#1100FStill, it's true that since the Non-Aggression \x01",
            "Pact was signed, there has been some progress \x01",
            "with regards to the Crossbell Problem.\x02\x03",

            "And given that it was Liberl who proposed said\x01",
            "pact, that makes my role in future negotiations\x01",
            "very important indeed...\x02\x03",

            "#1102FI presume that is what you are trying to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#031F#5PHeh. You're a sharp one, my good man!\x01",
            "Excellent.\x02\x03",

            "#030FNow I can return to the capital with my mind\x01",
            "at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#1102F#12PLeave everything here to me, Your Highness.\x02\x03",

            "#1100FI will be looking forward to hearing what you\x01",
            "achieve back in our homeland.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17D7():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_17D7)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    Call(0, 3)
    Return()

    # Function_2_22E end

    def Function_3_17F6(): pass

    label("Function_3_17F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-41290, 0, 15350, 0)
    OP_67(0, 4350, -10000, 0)
    OP_6B(5360, 0)
    OP_6C(35000, 0)
    OP_6E(164, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -64260, 0, 6540, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -52700, 0, 13800, 0)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -50940, 0, 13800, 270)

    def lambda_18A5():
        OP_6D(-50290, 0, 15350, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_18A5)

    def lambda_18BD():
        OP_6B(5160, 5000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_18BD)

    def lambda_18CD():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_18CD)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    ChrTalk(    #26
        0x11,
        (
            "#035F#6PThis truly is a country like no other.\x02\x03",

            "I never thought the day would come when\x01",
            "I would hear things like that from a noble\x01",
            "of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "#277F#11PIndeed. He's apparently somewhat less of an\x01",
            "obstinate man than I thought he was. \x02\x03",

            "#278FPerhaps this nation's very air has the power\x01",
            "to genuinely change people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#030F#6PIt seems to have had an effect on you, too.\x02\x03",

            "#031FI feel like I'm seeing a lot more smiles from\x01",
            "you these days than I used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#278F#11PHeh. I'm loath to admit it, but that may well be\x01",
            "true.\x02\x03",

            "#270FI still find myself wishing that you would learn\x01",
            "from Liberlians' dignity and sense of restraint,\x01",
            "however...\x02\x03",

            "#274FTwo qualities you don't particularly possess in\x01",
            "any measure. In fact, you have far too much of\x01",
            "their opposites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#035F#6PYou SAY that, but these qualities are the only\x01",
            "weapon that I have.\x02\x03",

            "#032FI don't have much that will allow me to compete\x01",
            "against the chancellor. I need to use what little\x01",
            "happens to be tucked in my corner as best I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x12,
        "#276F#11P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #32
        0x11,
        "#032F#6PHave there been any changes to our plans?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x12,
        (
            "#270F#11PNone. We should we able to proceed as arranged.\x02\x03",

            "#272FThree days ago, the chancellor left the capital on\x01",
            "a tour of eastern Erebonia.\x02\x03",

            "Tomorrow, you will be returning there aboard the\x01",
            "Arseille while he's still out in the east.\x02\x03",

            "All those who need to be made aware of our return\x01",
            "have been given proper notice.\x02\x03",

            "#277FYour arrival in Erebonia will make a real impact--\x01",
            "of that I am certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#035F#6PWhat potential obstructions to the plan are there\x01",
            "at present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#272F#11PNothing major. There have been some movements\x01",
            "in the Intelligence Division's 4th subdivision, but not\x01",
            "much.\x02\x03",

            "#276FThere's a chance that everyone is being cautious\x01",
            "because the Arseille is involved...\x02\x03",

            "#277F...but I'd put greater odds on the idea that everyone\x01",
            "is just treating this is a pompous performance by you\x01",
            "and not taking it seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#034F#6PWell, they'd be right to! It is.\x02\x03",

            "#030FI've no choice but to start here, even if this means\x01",
            "I have to use Liberl.\x02\x03",

            "#031FAnd if I'm going to put on a show, why not put on\x01",
            "the finest one the skies have ever seen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x12,
        "#278F#11P...I suppose I can't argue that.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -45500, -500, 10100, 270)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_21E6():
        OP_6D(-47780, 0, 13150, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_21E6)

    def lambda_21FE():
        OP_67(0, 3750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_21FE)

    def lambda_2216():
        OP_6C(58000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2216)

    def lambda_2226():

        label("loc_2226")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_2226")

    QueueWorkItem2(0x11, 2, lambda_2226)
    Sleep(50)

    def lambda_223C():

        label("loc_223C")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_223C")

    QueueWorkItem2(0x12, 2, lambda_223C)
    WaitChrThread(0x14, 0x0)
    Sleep(500)

    NpcTalk(    #38
        0x13,
        "Young Man's Voice",
        (
            "#5PI'm sorry to trouble you at this late hour,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x13,
        "Young Man's Voice",
        (
            "#5PA message has arrived for you from Heimdallr.\x01",
            "What would you have me do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#030F#6PReally? All right. Come in.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x13,
        "Young Man's Voice",
        "#5P...Pardon me.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_70(0x4, 0x3C)
    OP_73(0x4)

    def lambda_2371():
        OP_6D(-48660, 0, 14480, 3500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2371)

    def lambda_2389():
        OP_6C(62000, 3500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2389)
    SetChrPos(0x13, -44500, 0, 10000, 270)

    def lambda_23AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_23AA)

    def lambda_23BC():
        OP_8E(0xFE, 0xFFFF4868, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23BC)
    Sleep(1000)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    WaitChrThread(0x13, 0x1)

    def lambda_23FA():

        label("loc_23FA")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_23FA")

    QueueWorkItem2(0x13, 2, lambda_23FA)

    def lambda_240B():
        OP_8E(0xFE, 0xFFFF3D50, 0x0, 0x3070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_240B)
    WaitChrThread(0x13, 0x1)
    OP_44(0x13, 0x2)
    WaitChrThread(0x14, 0x2)

    ChrTalk(    #42
        0x11,
        (
            "#031F#6PWell, if it isn't Lechter.\x02\x03",

            "#030FI was wondering where you'd been.\x01",
            "I haven't seen you all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x13,
        (
            "#1885F#11PI've been exceptionally busy with work since this\x01",
            "morning, I'm afraid.\x02\x03",

            "#1880FI'd hoped to be able to come and see you earlier\x01",
            "since you will be leaving tomorrow... I'm terribly\x01",
            "sorry for not being able to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#035F#6PHeh. Oh, never mind that.\x02\x03",

            "#037FIf that work of yours is done now, we three could\x01",
            "always enjoy some...sensual quality time together\x01",
            "for the remainder of the night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "#270F#5PSo, what was the message from the capital,\x01",
            "Secretary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x13,
        (
            "#1884F#11PThey've acknowledged receipt of His Highness'\x01",
            "message.\x02\x03",

            "#1887FHowever, they didn't anticipate that you may be\x01",
            "able to arrive all the way from Grancel in less\x01",
            "than half a day...\x02\x03",

            "As such, they're currently in a minor panic trying\x01",
            "to ensure everything's ready for the ceremony\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12,
        (
            "#278F#5PThat doesn't come as a surprise. There's nothing\x01",
            "like the Arseille when it comes to speed at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "#034F#6P*whine* How cruel you both are for so deftly\x01",
            "ignoring my proposal!\x02\x03",

            "#030FAlthough, it sounds as though the stage will be\x01",
            "set in time.\x02\x03",

            "#031FNow I need to decide on an outfit that will leave\x01",
            "everyone's jaws on the floor to sweeten my arrival.\x02\x03",

            "#037FPerhaps a glistening coat and white loincloth will\x01",
            "do the trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#274F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13,
        (
            "#1881F#11PHaha. That'd make a grand impact, all right.\x02\x03",

            "I almost wish I could go along and see it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        "#276F#5PPlease don't encourage him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "#031F#6PHeh. You show remarkable promise for someone\x01",
            "so young.\x02\x03",

            "#030FWhat do you say to coming back on the Arseille\x01",
            "with me? I'd welcome your company.\x02\x03",

            "Your work here in Liberl is just about done as it\x01",
            "is, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x13,
        (
            "#1885F#11PYour offer's certainly tempting, but I'm afraid\x01",
            "I have another job to take care of soon.\x02\x03",

            "#1887FThe thought is appreciated, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#035F#6PReally? Well, that is a shame.\x02\x03",

            "#030FGood luck with that 'next job' of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13,
        "#1885F#11PThank you. Well, if you'll excuse me...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x13, 90, 400)
    Sleep(300)

    def lambda_2C17():
        OP_6D(-47780, 0, 13150, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2C17)

    def lambda_2C2F():
        OP_6C(58000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2C2F)

    def lambda_2C3F():
        OP_8F(0xFE, 0xFFFF4868, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2C3F)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 400)
    Sleep(500)
    OP_71(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(500)

    def lambda_2C87():
        OP_8E(0xFE, 0xFFFF4E44, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2C87)

    def lambda_2CA2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2CA2)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    Sleep(1000)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    OP_8C(0x12, 135, 0)

    def lambda_2CEB():
        OP_6D(-50290, 0, 15350, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2CEB)

    def lambda_2D03():
        OP_67(0, 4350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2D03)

    def lambda_2D1B():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2D1B)
    Sleep(1000)
    TurnDirection(0x11, 0x12, 400)
    WaitChrThread(0x14, 0x0)
    Sleep(500)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #56
        0x12,
        (
            "#272F#11PSo, that is Second Secretary Lechter Arundel?\x02\x03",

            "#276FIs it safe to assume he's one of the chancellor's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        (
            "#031F#6PAlmost definitely, yes.\x02\x03",

            "#030FHe came through Haken Gate on foot and took up\x01",
            "his new position at the embassy a month ago.\x02\x03",

            "And right around the same time we headed to the\x01",
            "Liber Ark aboard the Arseille, at that.\x02\x03",

            "#035FThere's no way that could possibly be coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#272F#11P...No, it couldn't.\x02\x03",

            "#276FThe most likely possibility seems to be that he's\x01",
            "part of the Intelligence Division.\x02\x03",

            "...Are you sure not doing anything regarding him\x01",
            "all this time was a good idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#035F#6POh, absolutely. We needed some way to find out \x01",
            "what the chancellor was up to, after all.\x02\x03",

            "#030FWe'll probably get some kind of reaction from the\x01",
            "chancellor through his reports at some point.\x02\x03",

            "#031FProbably in about two weeks when the chancellor's\x01",
            "tour has finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12,
        (
            "#278F#11PYou'd planned that far ahead all along, had you?\x02\x03",

            "#277FWell, in that case, I'll be sure that we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "#031F#6PI'll be counting on you,\x01",
            "love.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #62
        0x11,
        "#033F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#273F#11PSomething the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        (
            "#030F#6PNot really. It's just that the moon has come\x01",
            "out.\x02\x03",

            "#031FAnd what a beautiful full moon it is.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_322A():
        OP_6D(-49620, 0, 17860, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_322A)

    def lambda_3242():
        OP_6B(5060, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3242)

    def lambda_3252():
        OP_6C(28000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3252)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_44(0x14, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_17F6 end

    def Function_4_327D(): pass

    label("Function_4_327D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3356")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x611, 1)"), scpexpr(EXPR_END)), "loc_32EB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #65
        "\x07\x05Found \x1F\x11\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BE)
    Jump("loc_3353")

    label("loc_32EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05Found \x1F\x11\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x11\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_3353")

    Jump("loc_340F")

    label("loc_3356")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #67
        (
            "\x07\x05(10/12) ...apartment and kept to herself most days. *sigh*\x01",
            "She wasn't sure why she sighed. Probably just life catching up with her.\x01",
            "Then, suddenly...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x123, 0x0)

    label("loc_340F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_327D end

    def Function_5_341D(): pass

    label("Function_5_341D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_348B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #68
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BF)
    Jump("loc_34F3")

    label("loc_348B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_34F3")

    Jump("loc_3543")

    label("loc_34F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05You're...not going to kidnap me, are you?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x124, 0x0)

    label("loc_3543")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_341D end

    SaveToFile()

Try(main)
