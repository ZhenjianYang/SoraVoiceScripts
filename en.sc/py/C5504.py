from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5504   ._SN',
        MapName             = 'Other',
        Location            = 'C5504.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        "Anelace's Head",                       # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12180 ._CH',             # 00
        'ED6_DT29/CH12181 ._CH',             # 01
        'ED6_DT29/CH12230 ._CH',             # 02
        'ED6_DT29/CH12231 ._CH',             # 03
        'ED6_DT29/CH12270 ._CH',             # 04
        'ED6_DT29/CH12271 ._CH',             # 05
        'ED6_DT29/CH12360 ._CH',             # 06
        'ED6_DT29/CH12361 ._CH',             # 07
        'ED6_DT26/CH20268 ._CH',             # 08
        'ED6_DT26/CH20266 ._CH',             # 09
        'ED6_DT27/CH03005 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT29/CH12180P._CP',             # 00
        'ED6_DT29/CH12181P._CP',             # 01
        'ED6_DT29/CH12230P._CP',             # 02
        'ED6_DT29/CH12231P._CP',             # 03
        'ED6_DT29/CH12270P._CP',             # 04
        'ED6_DT29/CH12271P._CP',             # 05
        'ED6_DT29/CH12360P._CP',             # 06
        'ED6_DT29/CH12361P._CP',             # 07
        'ED6_DT26/CH20268P._CP',             # 08
        'ED6_DT26/CH20266P._CP',             # 09
        'ED6_DT27/CH03005P._CP',             # 0A
    )

    DeclNpc(
        X                   = -19520,
        Z                   = -200,
        Y                   = -19050,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1F8,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -8610,
        Z                   = 0,
        Y                   = 35650,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 890,
        Z                   = 0,
        Y                   = 17280,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24590,
        Z                   = 0,
        Y                   = 17330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19740,
        Z                   = 0,
        Y                   = 29560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16170,
        Z                   = 0,
        Y                   = 8880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 24590,
        TriggerZ            = 0,
        TriggerY            = 35090,
        TriggerRange        = 1000,
        ActorX              = 25030,
        ActorZ              = 0,
        ActorY              = 35520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28980,
        TriggerZ            = 0,
        TriggerY            = -18140,
        TriggerRange        = 800,
        ActorX              = -28980,
        ActorZ              = 1000,
        ActorY              = -18140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_38B",          # 03, 3
        "Function_4_494",          # 04, 4
        "Function_5_19F0",         # 05, 5
        "Function_6_1A04",         # 06, 6
        "Function_7_1CF4",         # 07, 7
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_20B")

    Return()

    # Function_0_1F6 end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E")
    OP_6F(0x0, 0)
    Jump("loc_225")

    label("loc_21E")

    OP_6F(0x0, 60)

    label("loc_225")

    Return()

    # Function_1_20C end

    def Function_2_226(): pass

    label("Function_2_226")

    OP_EA(0x2, 0x8E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x104, 1)"), scpexpr(EXPR_END)), "loc_297")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x04\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1120)
    Jump("loc_2FB")

    label("loc_297")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x04\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x04\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2FB")

    Jump("loc_379")

    label("loc_2FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Look, I know I don't have anything, but we can\x01",
            "still hang out, right? Wait, come baaaaaaack!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_379")

    Sleep(30)
    Call(0, 3)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_226 end

    def Function_3_38B(): pass

    label("Function_3_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493")

    ChrTalk(    #3
        0x101,
        (
            "#1004FHey!\x02\x03",

            "Do you think this could be\x01",
            "our equipment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        (
            "#811FSure looks like it! ♪\x02\x03",

            "#1310FThe rest of our stuff might be\x01",
            "hidden around like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1006FCool. I'd kinda like to avoid fighting\x01",
            "the monsters, but we do need to find\x01",
            "our stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    label("loc_493")

    Return()

    # Function_3_38B end

    def Function_4_494(): pass

    label("Function_4_494")

    EventBegin(0x0)
    OP_20(0xBB8)
    FadeToDark(0, 0, -1)
    OP_3F(0x9, 1)
    OP_3F(0x104, 1)
    OP_3F(0x125, 1)
    OP_3F(0xCF, 1)
    OP_3F(0x104, 1)
    OP_3F(0x125, 1)
    OP_6D(-19290, 0, -16309, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18710, 0, -16030, 268)
    SetChrPos(0x10A, -19980, 0, -19410, 243)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x10A, 9)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x10A, 0x1)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)

    ChrTalk(    #6
        0x101,
        (
            "#5P#1007FHnnmmnn...\x02\x03",

            "#1003FMornin' already...?\x02\x03",

            "Feels too...ear...\x02\x03",

            "#1020FWHA?!\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1000, 0)
    OP_0D()
    OP_99(0x101, 0x0, 0x2, 0x1F4)
    Sleep(500)
    SetChrSubChip(0x101, 5)
    Sleep(200)
    SetChrSubChip(0x101, 2)
    Sleep(200)
    SetChrSubChip(0x101, 5)
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        (
            "#6P#1020FWhat the heck...?\x02\x03",

            "Where in the Goddess' name...?\x02\x03",

            "I remember...an attack, and then...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 5)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(800)
    SetChrSubChip(0x101, 5)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    Sleep(500)
    SetChrSubChip(0x101, 4)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 180, 0)
    OP_0D()
    Sleep(500)
    OP_8E(0x101, 0xFFFFB776, 0x0, 0xFFFFB79E, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x101,
        (
            "#2P#1002FAnelace!\x02\x03",

            "Wake up, Anelace! Oh, no...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#1311F#5PHrmrlrml... Ehehehehe...\x02\x03",

            "A stuffed bunny, aaand...\x01",
            "a stuffed teddy beaaaar...\x02\x03",

            "...Oooooh, which one to piiiick...\x01",
            "Can I take 'em aaaaall, Grandpa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#2P#1007FWhat the heck kind of dream...\x02\x03",

            "#1005FAnelace! Come on, wake UP!\x01",
            "This is NOT the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        "#1316F#5PHaaaauuuh?\x02",
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x0, 0x2, 0x3E8)
    OP_99(0x10A, 0x2, 0x0, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0x0, 0x3, 0x3E8)

    ChrTalk(    #12
        0x10A,
        (
            "#1314F#5POh, mooornin', Estelle...\x02\x03",

            "Oh, riiight...thime f'r mornin' phractice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#2P#1007FGeh... No, it is not time for morning practice.\x02\x03",

            "#1014FJust WAKE UP already! Get it together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#813F#5PHauh...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_99(0x10A, 0x0, 0x3, 0x3E8)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    SetChrFlags(0x8, 0x80)
    OP_99(0x10A, 0x3, 0x7, 0x3E8)
    Sleep(1000)
    OP_99(0x10A, 0x7, 0x9, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0x9, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0xD, 0x13, 0x3E8)
    OP_99(0x10A, 0x10, 0x13, 0x3E8)

    ChrTalk(    #15
        0x10A,
        (
            "#814F#5PWait...\x02\x03",

            "Umm, Estelle? What's going on?\x01",
            "This isn't my bedroom.\x02\x03",

            "That attack thing WAS just\x01",
            "a bad nightmare...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#2P#1007FBoy, don't I wish...\x02\x03",

            "If we both remember it, though,\x01",
            "I kinda doubt it was a dream.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x7, 0x9, 0x3E8)

    ChrTalk(    #17
        0x10A,
        (
            "#819F#5POoooh...yyyyyeah, that's a good point.\x02\x03",

            "Wowwee... Man, looks like we lost\x01",
            "the match. No points for meeeee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#2P#1019FAnelace, why do I get the sense\x01",
            "you're still half-asleep?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x10A, 0x2)
    SetChrFlags(0x10A, 0x1)
    SetChrPos(0x101, -20730, 0, -19460, 68)
    SetChrPos(0x10A, -19800, 0, -18290, 159)
    ClearMapFlags(0x1)
    OP_6D(-24650, 0, -20010, 0)
    OP_67(0, 12770, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(179000, 0)
    OP_6E(262, 0)
    OP_1D(0x15)
    OP_C8(0x200, 0x46, "C_PLAC02._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_C42():
        OP_6D(-19150, 0, -18900, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_C42)

    def lambda_C5A():
        OP_67(0, 12770, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C5A)

    def lambda_C72():
        OP_6C(15000, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C72)

    def lambda_C82():
        OP_8C(0x101, 190, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C82)

    def lambda_C90():
        OP_8C(0x10A, 90, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C90)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    Sleep(100)

    def lambda_CAD():
        OP_8C(0x101, 245, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CAD)

    def lambda_CBB():
        OP_8C(0x10A, 92, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBB)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    Fade(1000)
    OP_6D(-21320, 0, -19030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_8C(0x10A, 172, 500)
    Sleep(100)
    OP_8C(0x101, 102, 500)
    Sleep(500)

    ChrTalk(    #19
        0x10A,
        (
            "#817F#4PA-Anyway, let's go over what we\x01",
            "know. Get our bearings and stuff.\x02\x03",

            "#812FSo last night, a group of men who looked\x01",
            "just a BIT like jaegers attacked the lodge...\x02\x03",

            "I remember Kurt...was wounded,\x01",
            "and right after we arrived an enemy\x01",
            "jumped in through the window...\x02\x03",

            "And right after that, it was\x01",
            "lights out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F#6PYeah, that matches what I remember.\x02\x03",

            "The question is, how the heck\x01",
            "did we wind up here?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_FDE")

    ChrTalk(    #21
        0x10A,
        (
            "#812F#4PGooood question. That is kind of weird.\x02\x03",

            "It looks like they left most\x01",
            "of our stuff on us, but...\x02\x03",

            "Yeah, all my training equipment\x01",
            "is missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1004F#6POh, yeah, mine too.\x02\x03",

            "#1015FSo that means we were\x01",
            "probably brought here by...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D8")

    label("loc_FDE")


    ChrTalk(    #23
        0x10A,
        (
            "#812F#4PGooood question. That is kind of weird.\x02\x03",

            "It looks like they left most\x01",
            "of our stuff on us, but...\x02\x03",

            "Yeah, all my new combat gear\x01",
            "is missing. Man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1004F#6POh, yeah, mine too.\x02\x03",

            "#1015FSo that means we were probably\x01",
            "brought here by...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D8")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x18\x07\x05Who brought Estelle and Anelace into the forest?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Kurt\x01",                       # 0
            "The Attacking Jaegers\x01",      # 1
            "Some Third Party\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11A3"),
        (1, "loc_1321"),
        (2, "loc_13E1"),
        (SWITCH_DEFAULT, "loc_14D1"),
    )


    label("loc_11A3")


    ChrTalk(    #26
        0x10A,
        (
            "#813F#4PSomehow, I kinda doubt that...\x02\x03",

            "Kurt was injured. I don't think he could've\x01",
            "carried the both of us far in his condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1003F#6PYeah...\x02\x03",

            "Besides, Kurt wouldn't leave\x01",
            "us defenseless out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        (
            "#812F#4PThe most likely answer is the jaegers, but...\x02\x03",

            "In that case, why didn't they tie us\x01",
            "up or, I dunno, stab us or something?\x01",
            "They just left us in the open...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_1321")

    OP_2B(0x7E, 0x3)

    ChrTalk(    #29
        0x10A,
        (
            "#812F#4PYeah, that's the obvious answer.\x01",
            "One thing's bugging me, though.\x02\x03",

            "It's just, why didn't they tie us up or,\x01",
            "I dunno, stab us or something?\x01",
            "They just left us in the open...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_13E1")


    ChrTalk(    #30
        0x10A,
        (
            "#1316F#4PHmm... It's not out of the question,\x01",
            "I guess. But...\x02\x03",

            "#812FPersonally, I think the most\x01",
            "likely answer is the jaegers.\x02\x03",

            "Although, why didn't they tie us up or,\x01",
            "I dunno, stab us or something?\x01",
            "They just left us in the open...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_14D1")


    ChrTalk(    #31
        0x101,
        (
            "#1002F#6PWell, let's see...\x01",
            "After knocking us out and disarming us...\x02\x03",

            "Something happened and they had to quickly\x01",
            "retreat somewhere else, leaving us behind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#816F#4PYeah, that's pretty believable.\x02\x03",

            "In that case, sticking around here is\x01",
            "like asking to get our heads cut off.\x02\x03",

            "Estelle, you still have that map?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1004F#6POh, yeah! We still have\x01",
            "some of our stuff, so...\x02\x03",

            "#1006FYeah, here it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x2400A0, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #34
        (
            "\x07\x00#810FYeah, I thought so.\x02\x03",

            "There's Saint-Croix Forest, where\x01",
            "we were training last night. I'm\x01",
            "guessing that's where we are now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 340, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #35
        (
            "\x07\x00#1015FSo in that case...\x02\x03",

            "Our first goal should be getting out of the\x01",
            "forest and checking on the lodge, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #36
        (
            "\x07\x00#813FYeah. I wanna see if we can find\x01",
            "Kurt and make sure he's okay...\x02\x03",

            "Like you said, we gotta get\x01",
            "out of this stupid forest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    OP_AE(0x3E8)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_18FC")

    ChrTalk(    #37
        0x10A,
        (
            "#810F#4PAll right, then, let's get out of here.\x02\x03",

            "I'll bet my ribbon there's still enemies around,\x01",
            "as well, so we need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1002F#6PGot it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19D2")

    label("loc_18FC")


    ChrTalk(    #39
        0x10A,
        (
            "#810F#4PAll right, then, let's get out of here.\x02\x03",

            "We're basically sitting ducks without our\x01",
            "gear, remember, so we need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1002F#6PGot it!\x02\x03",

            "It'd be nice if we could reclaim\x01",
            "our gear somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D2")

    OP_A2(0x100D)
    OP_28(0x7F, 0x1, 0x2)
    OP_28(0x7F, 0x1, 0x4)
    OP_28(0x7F, 0x1, 0x8)
    OP_28(0x7F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_494 end

    def Function_5_19F0(): pass

    label("Function_5_19F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FF")
    Call(0, 6)
    Jump("loc_1A03")

    label("loc_19FF")

    Call(0, 7)

    label("loc_1A03")

    Return()

    # Function_5_19F0 end

    def Function_6_1A04(): pass

    label("Function_6_1A04")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-28980, 0, -18140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -27880, 0, -18520, 325)
    SetChrPos(0x10A, -28610, 0, -19090, 350)
    OP_0D()

    ChrTalk(    #41
        0x101,
        "#1002FWhat's this? A jaeger tent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#812FThat'd be my guess.\x02\x03",

            "Let's take a peek inside.\x01",
            "We might find something useful.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00Found #502i x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1F6, 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #44
        "\x07\x00Found #510i x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1FE, 2)

    ChrTalk(    #45
        0x101,
        (
            "#1007FWell, looks like that's everything.\x02\x03",

            "#1015FDarn it, I was hoping we'd\x01",
            "find our gear in there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        (
            "#1316FMan, I wish it was that easy.\x02\x03",

            "#810FStill, the tent's in good shape.\x01",
            "We could probably nap here if\x01",
            "we needed to take a quick rest.\x02\x03",

            "We don't have time to just lounge\x01",
            "around, but if we really need\x01",
            "a rest, we should keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1011FGood idea.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x100E)
    EventEnd(0x0)
    Return()

    # Function_6_1A04 end

    def Function_7_1CF4(): pass

    label("Function_7_1CF4")

    TalkBegin(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Rest For A Bit]\x01",      # 0
            "[Don't Rest]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D64"),
        (1, "loc_1E39"),
        (SWITCH_DEFAULT, "loc_1E3C"),
    )


    label("loc_1D64")

    OP_1F(0x0, 0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    OP_6D(-28380, 0, -18660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -28380, 0, -18660, 135)
    SetChrPos(0x10A, -28380, 0, -18660, 135)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05Regained HP and EP.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1F(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1E3C")

    label("loc_1E39")

    Jump("loc_1E3C")

    label("loc_1E3C")

    TalkEnd(0xFF)
    Return()

    # Function_7_1CF4 end

    SaveToFile()

Try(main)
