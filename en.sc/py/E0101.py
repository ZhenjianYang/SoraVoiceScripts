from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0101   ._SN',
        MapName             = 'event',
        Location            = 'E0101.x',
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
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
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT26/CH20370 ._CH',             # 02
        'ED6_DT26/CH20400 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT27/CH03015 ._CH',             # 05
        'ED6_DT26/CH20401 ._CH',             # 06
        'ED6_DT27/CH03101 ._CH',             # 07
        'ED6_DT26/CH20398 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT26/CH20370P._CP',             # 02
        'ED6_DT26/CH20400P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT27/CH03015P._CP',             # 05
        'ED6_DT26/CH20401P._CP',             # 06
        'ED6_DT27/CH03101P._CP',             # 07
        'ED6_DT26/CH20398P._CP',             # 08
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        "Function_0_152",          # 00, 0
        "Function_1_161",          # 01, 1
        "Function_2_181",          # 02, 2
        "Function_3_154F",         # 03, 3
        "Function_4_155F",         # 04, 4
        "Function_5_1574",         # 05, 5
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_160")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_160")

    Return()

    # Function_0_152 end

    def Function_1_161(): pass

    label("Function_1_161")

    OP_22(0x79, 0x1, 0x3C)
    OP_22(0x1C3, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180")

    Return()

    # Function_1_161 end

    def Function_2_181(): pass

    label("Function_2_181")

    EventBegin(0x0)
    ClearParty()
    AddParty(0x1, 0xF6, 0xFF)
    SetChrFlags(0x102, 0x80)
    OP_DB()
    OP_48()
    OP_6D(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    OP_6B(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    StopSound(0xD6D8, 0x7A120, 0x0)
    OP_EB(0xD5, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    OP_BD()
    FadeToBright(2000, 0)
    StopSound(0xD6D8, 0x33450, 0x32C8)

    def lambda_200():
        OP_6D(-99550, 5550, -94010, 13000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_200)

    def lambda_218():
        OP_6B(2800, 13000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_218)

    def lambda_228():
        OP_6E(334, 13000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_228)
    Sleep(7000)
    OP_72(0x3, 0x20)

    def lambda_242():
        OP_6C(35000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_242)
    OP_67(0, 7540, -10000, 6000)
    OP_22(0x6A, 0x0, 0x64)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(1000)
    SetChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    SetChrPos(0x8, -99440, 5550, -91440, 0)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0xFFFE7B72, 0x15A4, 0xFFFE90F8, 0x7D0, 0x0)
    OP_DC()

    ChrTalk(    #0
        0x8,
        "#213F#3PWhere's...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    Sleep(500)
    SetChrPos(0x102, -100000, 5550, -89500, 0)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 2)
    SetChrSubChip(0x102, 2)
    OP_43(0x8, 0x1, 0x0, 0x5)

    def lambda_334():
        OP_6D(-98020, 5550, -89450, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_334)
    OP_6C(225000, 8000)

    ChrTalk(    #1
        0x8,
        "#210FOooh, there you are.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #2
        0x102,
        (
            "#1031F...I can see the moon more\x01",
            "clearly from here.\x02\x03",

            "And I can feel the breeze on my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#211FHaha! Ooooh, you're being soooo\x01",
            "mysterious, Joshua!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_449():
        OP_6D(-99380, 5550, -89500, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_449)

    def lambda_461():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_461)

    def lambda_471():
        OP_8E(0x8, 0xFFFE7D34, 0x15AE, 0xFFFEA296, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_471)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x102, 0x1)
    Fade(250)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #4
        0x8,
        (
            "#210FHup!\x02\x03",

            "#413FOkay, looks like you AREN'T just\x01",
            "trying to be cool.\x02\x03",

            "#215FThis is the sort of thing your job\x01",
            "takes, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(500)

    ChrTalk(    #5
        0x102,
        (
            "#1035F#4PThe moonlight. The position of the clouds.\x01",
            "The flow of the wind. Every detail is vital.\x02\x03",

            "#1031FI wish to lower the possibility of failure\x01",
            "as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "#212FLower the...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 4)
    Sleep(300)

    ChrTalk(    #7
        0x8,
        (
            "#214FLower the...!\x01",
            "Don't say it like THAT, you idiot!\x02\x03",

            "If you 'fail,' you'll die, you know?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1035F#4PDon't worry. The possibility of my\x01",
            "failure is very remote.\x02\x03",

            "Back...in my previous life, I used to\x01",
            "conduct missions like this every day.\x02\x03",

            "#1033FThe real danger will come if I succeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#212F...\x02\x03",

            "#413F...Hey, Joshua?\x02\x03",

            "Do you really, absolutely need to do all this?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #10
        0x102,
        "#1034F#4PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#215FYou're Erebonian, same as us.\x02\x03",

            "#413FI mean, yeah, circumstances mean that\x01",
            "none of us can really go home, but...\x02\x03",

            "#212FI just don't get it. Why do you feel like\x01",
            "you owe this piddly little backwater\x01",
            "anything?\x02\x03",

            "Just let these 'Ouroboros' idiots do\x01",
            "whatever they want to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1033F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#210FAnd, hey, it's still not too late, you know!\x02\x03",

            "You can come with us, away from Liberl!\x02\x03",

            "We can head out to some independent state\x01",
            "and raise our flag there, y'know?\x02\x03",

            "And, hey, if you really don't like the whole 'sky\x01",
            "bandit' gig, we can try and find something else\x01",
            "to do!\x02\x03",

            "#211FI was talking to Kyle and Don, and we were\x01",
            "thinking the Bobcat could make a good legit\x01",
            "shipping vessel. You know, speed and all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(75)
    SetChrSubChip(0x102, 6)
    Sleep(400)

    ChrTalk(    #14
        0x102,
        (
            "#1035F#4PAn airship delivery service?\x02\x03",

            "I could see it having some potential.\x01",
            "Demand for that kind of service is\x01",
            "certainly going up.\x02\x03",

            "It'd be a safer job than sky banditry,\x01",
            "at any rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#210FW-Well, then! Technically, we, uh,\x01",
            "do have some berths open...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #16
        0x102,
        (
            "#1031F#4PThat you do...\x02\x03",

            "Once I've crushed the society's plan,\x01",
            "and if I manage to survive, I'll think it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#213F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1034F#4PAh, you needn't worry, this completes\x01",
            "our contract.\x02\x03",

            "#1031FAs promised, your cooperation here means\x01",
            "I'll consider the favor you owe me redeemed.\x02\x03",

            "You can depart whenever, I won't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "#215F...orget it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1034F#4PMm?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_8C(0x8, 270, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x8,
        (
            "#214FYOU IDIOT! MORON! JERK!\x01",
            "Who the hell was talking about DEBTS?!\x02\x03",

            "#215FForget it! Who cares about you!\x02\x03",

            "Just go leap into danger and die,\x01",
            "if that's all you wanna do!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x8, 90, 600)
    SetChrChipByIndex(0x8, 7)
    OP_8E(0x8, 0xFFFE8E3C, 0x15AE, 0xFFFEA070, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFE8DA6, 0x15AE, 0xFFFE94FE, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFE7BC2, 0x15AE, 0xFFFE910C, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x10)
    Sleep(500)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(800)
    SetChrSubChip(0x102, 1)
    Sleep(140)
    SetChrSubChip(0x102, 2)
    Sleep(800)

    ChrTalk(    #22
        0x102,
        "#1035F#6P...I'm sorry, Josette.\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x9, 0x20)
    SetChrPos(0x9, -103120, 13050, -91360, 10)
    OP_6F(0x1, 35)
    Sleep(500)

    NpcTalk(    #23
        0x9,
        "Young Man's Voice",
        (
            "#6PAidios' mercy... Not easy playing dumb,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(50)
    SetChrSubChip(0x102, 0)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x9, -103120, 9050, -91360, 10)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x9, 0x80)
    Fade(500)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_F91():
        OP_6D(-100330, 5550, -92350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F91)

    def lambda_FA9():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FA9)

    def lambda_FC1():
        OP_6C(144000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_FC1)

    def lambda_FD1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FD1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #24
        0x102,
        "#1034F#1PKyle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#200FI do wish she'd finally grow out of her\x01",
            "more childish tendencies...\x02\x03",

            "Even so, I think you could've handled\x01",
            "that better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1035F#1P...It's true.\x02\x03",

            "#1033FI cannot apologize, but I do feel sorry\x01",
            "for what I've...done to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "#203FMan...you sure have an odd\x01",
            "way of being nice, Astray.\x02\x03",

            "#200FYou want to make it up to her, give that\x01",
            "offer some serious thought.\x02\x03",

            "Assuming, of course, you won't be joining\x01",
            "up again with your nice, young bracer lady\x01",
            "after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1031F#1PHaha... No, that won't be happening.\x02\x03",

            "In the end, the worlds we live in are\x01",
            "too different.\x02\x03",

            "She and I should never meet again.\x01",
            "It's for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#200FHmmmmm... Well, if that's how you think.\x02\x03",

            "#202FIn that case, Josette's offer does have\x01",
            "some appeal, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1031F#1PIt does... I am going to give it\x01",
            "some thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAB, 0x1, 0x50)
    Sleep(500)
    OP_20(0x3E8)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x9,
        "#201FLook who's decided to show themselves!\x02",
    )

    CloseMessageWindow()

    def lambda_1381():
        OP_8F(0xFE, 0xFFFE6D30, 0x2198, 0xFFFE9B20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1381)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x9, 0x1)
    OP_1D(0x56)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #32
        0x9,
        "#201F#3PDon, is that them?!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -103120, 6550, -91360, 270)

    NpcTalk(    #33
        0xA,
        "Don's Voice",
        (
            "#3PYeah! It's just like the lad predicted!\x02\x03",

            "They're approaching from the northeast!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_144F():
        OP_8F(0xFE, 0xFFFE6D30, 0x235A, 0xFFFE9B20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_144F)
    OP_8C(0x9, 10, 400)
    WaitChrThread(0x9, 0x1)
    Sleep(300)

    ChrTalk(    #34
        0x9,
        "#206FYou heard the man. To the bridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1032F#1PGot it.\x02",
    )

    CloseMessageWindow()

    def lambda_14BD():
        OP_6D(-100000, 5550, -89480, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BD)

    def lambda_14D5():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14D5)

    def lambda_14ED():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_14ED)

    def lambda_14FD():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14FD)

    def lambda_150D():
        OP_6E(262, 1500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_150D)
    OP_8C(0x9, 270, 400)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_23(0xAB)
    OP_6F(0x1, 35)
    OP_70(0x1, 0x0)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_A2(0x1C00)
    OP_D6(0x0)
    WaitChrThread(0x102, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_181 end

    def Function_3_154F(): pass

    label("Function_3_154F")

    Sleep(800)
    OP_22(0xE6, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_3_154F end

    def Function_4_155F(): pass

    label("Function_4_155F")

    OP_8F(0xFE, 0xFFFE6D30, 0x17A2, 0xFFFE9B20, 0x7D0, 0x0)
    Return()

    # Function_4_155F end

    def Function_5_1574(): pass

    label("Function_5_1574")

    OP_8E(0xFE, 0xFFFE8F54, 0x15AE, 0xFFFE951C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8EC8, 0x15AE, 0xFFFE9FC6, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8C52, 0x15AE, 0xFFFEA0FC, 0x5DC, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_1574 end

    SaveToFile()

Try(main)
